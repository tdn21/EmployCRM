from students.forms import RequestOfferLetter
from django.urls import path
from .views import (
    CompletionLetterRequestListView,
    IssueCompletionLetterView,
    IssueOfferLetterView,
    OfferLetterRequestListView,
    RequestCompletionLetterView,
    RequestOfferLetterView,
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentMyDetailView,
    StudentUpdateDetailView,
    StudentUpdateView,
    StudentsUploadView
)

from .letter_generation_views.views import (
    GeneratePdf,
    DownloadOfferLetterView,
    DownloadCompletionLetterView
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
    path('upload/', StudentsUploadView.as_view(), name='student-upload'),
    path('offer-letter-requests', OfferLetterRequestListView.as_view(), name='student-offer-letter-request-list'),
    path('completion-letter-requests', CompletionLetterRequestListView.as_view(), name='student-completion-letter-request-list'),
    path('offer-letter-requests/<int:pk>', IssueOfferLetterView.as_view(), name='student-issue-offer-letter'),
    path('completion-letter-requests/<int:pk>', IssueCompletionLetterView.as_view(), name='student-issue-completion-letter'),
    path('download-offer-letter', DownloadOfferLetterView.as_view(), name='student-download-offer-letter'),
    path('download-completion-letter', DownloadCompletionLetterView.as_view(), name='student-download-completion-letter'),
    path('download-pdf', GeneratePdf.as_view(), name='download-pdf')
]