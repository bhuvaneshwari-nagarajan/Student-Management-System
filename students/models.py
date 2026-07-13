from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.student_id:
            last_student = Student.objects.order_by('-id').first()
            if last_student and last_student.student_id:
                prefix = last_student.student_id[:3]
                number = int(last_student.student_id[3:]) + 1
            else:
                prefix = 'STU'
                number = 1
            self.student_id = f'{prefix}{number:04d}'
        super().save(*args, **kwargs)
