import json
from django.db import models
from .models import Enrollment
from .tasks import handle_enrollment


def bulk_process(raw_data, chunk_size=500):
    for i in range(0, len(raw_data), chunk_size):
        chunk = raw_data[i : i + chunk_size]
        handle_enrollment.delay(items=json.dumps(chunk))
    return 1


def get_enrollment_count(query):
    return Enrollment.objects.values(query).annotate(count=models.Count("id"))
