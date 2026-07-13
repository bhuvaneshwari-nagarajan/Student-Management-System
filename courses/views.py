from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import CourseForm
from .models import Course


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'
    paginate_by = 5

    def get_queryset(self):
        return Course.objects.all().order_by('course_name')


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('courses:course_list')

    def form_valid(self, form):
        messages.success(self.request, 'Course added successfully.')
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('courses:course_list')

    def form_valid(self, form):
        messages.success(self.request, 'Course updated successfully.')
        return super().form_valid(form)


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('courses:course_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Course deleted successfully.')
        return super().delete(request, *args, **kwargs)
