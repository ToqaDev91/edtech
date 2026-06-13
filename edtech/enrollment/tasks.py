import logging
import json
from datetime import datetime
from config.celery import  app
from celery import Task
from .models import Process, Enrollment
from .constants import FAILED, PROCESSED

logger = logging.getLogger("enrollment")

@app.task(bind=True, default_retry_delay=15)
def handle_enrollment(self: Task, item):
    item = json.loads(item)
    process = Process.objects.create(raw_data=item)
    try:
        Enrollment.objects.update_or_create(**item)
        process.status = PROCESSED
    except Exception as e:
        logger.error(str(e))
        process.status = FAILED
        process.error_message = str(e)
    process.processed_at = datetime.now()
    process.save()