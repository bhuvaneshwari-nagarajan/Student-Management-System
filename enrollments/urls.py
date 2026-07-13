from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    path('', views.EnrollmentListView.as_view(), name='enrollment_list'),
    path('add/', views.EnrollmentCreateView.as_view(), name='enrollment_add'),
    path('<int:pk>/delete/', views.EnrollmentDeleteView.as_view(), name='enrollment_delete'),
]
