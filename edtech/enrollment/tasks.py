import logging
import json
from datetime import datetime
from django.db import transaction
from celery import Task
from config.celery import app
from .models import Process, Enrollment
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
    processed_at = datetime.now()
    try:
        with transaction.atomic():
            Enrollment.objects.bulk_create(enrollment_objs, ignore_conflicts=True)
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