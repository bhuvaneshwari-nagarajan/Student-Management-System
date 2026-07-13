from django.shortcuts import render
from students.models import Student
from courses.models import Course
from enrollments.models import Enrollment


def dashboard(request):
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    total_enrollments = Enrollment.objects.count()
    recent_students = Student.objects.order_by('-created_at')[:5]
    recent_courses = Course.objects.order_by('-created_at')[:5]
    return render(request, 'dashboard.html', {
        'total_students': total_students,
        'total_courses': total_courses,
        'total_enrollments': total_enrollments,
        'recent_students': recent_students,
        'recent_courses': recent_courses,
    })
