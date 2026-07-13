from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView
from .forms import EnrollmentForm
from .models import Enrollment


class EnrollmentListView(LoginRequiredMixin, ListView):
    model = Enrollment
    template_name = 'enrollment_list.html'
    context_object_name = 'enrollments'
    paginate_by = 5

    def get_queryset(self):
        return Enrollment.objects.select_related('student', 'course').all().order_by('-enrollment_date')


class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollment_form.html'
    success_url = reverse_lazy('enrollments:enrollment_list')

    def form_valid(self, form):
        messages.success(self.request, 'Enrollment created successfully.')
        return super().form_valid(form)


class EnrollmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Enrollment
    template_name = 'enrollment_confirm_delete.html'
    success_url = reverse_lazy('enrollments:enrollment_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Enrollment removed successfully.')
        return super().delete(request, *args, **kwargs)
