from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'phone', 'address', 'image')
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.strip():
            raise forms.ValidationError('Name is required.')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('A student with this email already exists.')
        return email
