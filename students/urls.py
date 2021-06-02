from django.urls import path
from .views import (
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
    UploadStudents
)

app_name = "students"

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('upload_students/', UploadStudents.as_view(), name='upload-students'),
]