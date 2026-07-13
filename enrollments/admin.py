from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'enrollment_date')
    search_fields = ('student__name', 'course__course_name')
    list_filter = ('status', 'enrollment_date')
