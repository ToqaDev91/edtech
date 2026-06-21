import logging
import json
from datetime import datetime
from django.utils import timezone
from django.db import transaction
from celery import Task
from config.celery import app
from .models import Process, Enrollment, EnrollmentCounter
from .constants import FAILED, PROCESSED

logger = logging.getLogger("enrollment")

@app.task(bind=True, default_retry_delay=15)
def handle_enrollment(self: Task, items):
    """
    Processes a batch of enrollment items efficiently using bulk operations.
    """
    items = json.loads(items)
    processes = [Process(raw_data=item) for item in items]
    Process.objects.bulk_create(processes)
    enrollment_objs = [Enrollment(**item) for item in items]
    processed_at = timezone.now()
    try:
        with transaction.atomic():
            Enrollment.objects.bulk_create(enrollment_objs, ignore_conflicts=True)
            loop_enrollment(enrollment_objs)
            for process in processes:
                process.status = PROCESSED
                process.processed_at = processed_at
            Process.objects.bulk_update(processes, ['status', 'processed_at'])
    except Exception as e:
        logger.error(f"Batch processing error: {str(e)}")
        for process in processes:
            process.status = FAILED
            process.error_message = str(e)
            process.processed_at = processed_at
        Process.objects.bulk_update(processes, ['status', 'error_message', 'processed_at'])
    
        
def loop_enrollment(items):
    for item in items:
        region = item.region
        grade = item.grade
        update_enrollment_counter("region", region, 1)
        update_enrollment_counter("grade", grade, 1)

def update_enrollment_counter(key_type, key_value, count):
    counter, created = EnrollmentCounter.objects.get_or_create(
        key_type=key_type,
        key_value=key_value,
        defaults={"count": count},
    )
    if not created:
        counter.count = counter.count + count
        counter.save()