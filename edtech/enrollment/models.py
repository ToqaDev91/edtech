from django.db import models
from .constants import TYPES_STATUS, PENDING


class Process(models.Model):
    raw_data = models.JSONField(default=dict, blank=True, null=True)
    status= models.CharField(max_length=128, null=False, blank=False, choices=TYPES_STATUS, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)

class Enrollment(models.Model):
    """enrollment main table"""
    student_id = models.CharField(max_length=128, null=False, blank=False)
    region = models.CharField(max_length=128, null=False, blank=False)
    grade = models.CharField(max_length=128, null=False, blank=False)
    enrollment_date = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        unique_together = ('student_id', 'region', 'grade')
        indexes = [
            models.Index(fields=['region', 'grade']),
        ]
   