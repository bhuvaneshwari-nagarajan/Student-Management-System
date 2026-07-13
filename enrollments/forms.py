from django import forms
from .models import Enrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ('student', 'course', 'status')

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        course = cleaned_data.get('course')
        if student and course and Enrollment.objects.filter(student=student, course=course).exists():
            raise forms.ValidationError('This student is already enrolled in this course.')
        return cleaned_data
