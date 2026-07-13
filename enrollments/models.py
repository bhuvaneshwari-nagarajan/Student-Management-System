from django.db import models
from students.models import Student
from courses.models import Course


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Dropped', 'Dropped'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    class Meta:
        ordering = ['-enrollment_date']
        unique_together = ('student', 'course')

    def __str__(self):
        return f'{self.student.name} -> {self.course.course_name}'
