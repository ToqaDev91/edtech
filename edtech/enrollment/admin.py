from django.contrib import admin
from .models import Enrollment, Process, EnrollmentCounter

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'region', 'grade', 'enrollment_date')
    search_fields = ('student_id', 'region', 'grade')
    list_filter = ('region', 'grade')
    ordering = ('-enrollment_date',)
    
@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at', 'processed_at')
    search_fields = ('status',)
    list_filter = ('status',)
    ordering = ('-created_at',)
        
@admin.register(EnrollmentCounter)
class EnrollmentCounterAdmin(admin.ModelAdmin):
    list_display = ('key_type', 'key_value', 'count')
    search_fields = ('key_type', 'key_value')
    list_filter = ('key_type',)
    ordering = ('-count',)