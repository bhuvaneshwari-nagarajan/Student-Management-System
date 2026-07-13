import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import StudentForm
from .models import Student


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if query:
            return Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query)).order_by('-created_at')
        return Student.objects.all().order_by('-created_at')


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        messages.success(self.request, 'Student added successfully.')
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        messages.success(self.request, 'Student updated successfully.')
        return super().form_valid(form)


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('students:student_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Student deleted successfully.')
        return super().delete(request, *args, **kwargs)


@login_required
def export_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    writer = csv.writer(response)
    writer.writerow(['student_id', 'name', 'email', 'phone', 'address', 'created_at'])

    students = Student.objects.all().order_by('name')
    for student in students:
        writer.writerow([student.student_id, student.name, student.email, student.phone, student.address, student.created_at])
    return response
