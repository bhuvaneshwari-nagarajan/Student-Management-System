from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'duration', 'fee', 'created_at')
    search_fields = ('course_code', 'course_name')
    list_filter = ('created_at', 'fee')
