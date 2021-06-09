from django.urls import path
from .views import (
    TaskCreateView, TaskDeleteView, TaskDetailView, TaskUpdateView, TaskListView
)
from .other_views.offer_letter import (
    OfferLetterView,
    PreviewOfferLetterView,
    DownloadOfferLetterView
)
from .other_views.completion_certificate import (
    PreviewCompletionLetter,
    DownloadCompletionLetterView,
)
from .other_views.generate_pdf import (
    GeneratePdf
)
app_name = "tasks"

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('offer_letter/',OfferLetterView.as_view(),name='offer-letter'),
    path('preview_offer_letter/',PreviewOfferLetterView.as_view(),name='preview-offer-letter'),
    path('generate_pdf/',GeneratePdf.as_view(),name='download-pdf'),
    path('download_offer_letter/',DownloadOfferLetterView.as_view(),name='download-offer-letter'),
    path('preview_completion_letter/',PreviewCompletionLetter.as_view(),name='preview-completion-letter'),
    path('download_completion_letter/',DownloadCompletionLetterView.as_view(),name='download-completion-letter'),
]