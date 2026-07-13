from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_code', 'course_name', 'description', 'duration', 'fee', 'image')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_course_code(self):
        code = self.cleaned_data.get('course_code')
        if not code.strip():
            raise forms.ValidationError('Course code is required.')
        return code
