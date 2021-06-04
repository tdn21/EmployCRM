from students.forms import RequestOfferLetter
from django.urls import path
from .views import (
    RequestCompletionLetterView,
    RequestOfferLetterView,
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentMyDetailView,
    StudentUpdateDetailView,
    StudentUpdateView
)

app_name = "students"

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('<int:pk>/my-detail', StudentMyDetailView.as_view(), name='student-my-detail'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('<int:pk>/update-detail/', StudentUpdateDetailView.as_view(), name='student-update-detail'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('<int:pk>/request-offer-letter/', RequestOfferLetterView.as_view(), name='student-request-offer-letter'),
    path('<int:pk>/request-completion-letter/', RequestCompletionLetterView.as_view(), name='student-request-completion-letter'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
]