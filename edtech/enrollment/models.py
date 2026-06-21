from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from .constants import TYPES_STATUS, PENDING, COUNTER_TYPES


class Process(models.Model):
    raw_data = models.JSONField(default=dict, blank=True, null=True)
    status= models.CharField(max_length=128, null=False, blank=False, choices=TYPES_STATUS, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)

class Enrollment(models.Model):
    """enrollment main table"""
    student_id = models.CharField(max_length=128, null=False, blank=False)
    region = models.CharField(max_length=128, null=False, blank=False, db_index=True)
    grade = models.CharField(max_length=128, null=False, blank=False, db_index=True)
    enrollment_date = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        unique_together = ('student_id', 'region', 'grade')

class EnrollmentCounter(models.Model):
    key_type= models.CharField(max_length=128, null=False, blank=False, choices=COUNTER_TYPES, db_index=True)
    key_value = models.CharField(max_length=128, null=False, blank=False)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['key_type', 'key_value']),
        ]