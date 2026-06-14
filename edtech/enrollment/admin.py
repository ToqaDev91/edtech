from django.contrib import admin
from .models import Enrollment, Process

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
    

