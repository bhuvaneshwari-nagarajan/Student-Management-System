from django.db import models


class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=50, blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['course_name']

    def __str__(self):
        return self.course_name
