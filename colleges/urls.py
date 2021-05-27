from colleges.views import CollegeCreateView, CollegeDeleteView, CollegeDetailView, CollegeListView, CollegeUpdateView
from django.urls import path

app_name = "colleges"

urlpatterns = [
    path('', CollegeListView.as_view(), name='college-list'),
    path('<int:pk>/', CollegeDetailView.as_view(), name='college-detail'),
    path('<int:pk>/update/', CollegeUpdateView.as_view(), name='college-update'),
    path('<int:pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),
    path('create/', CollegeCreateView.as_view(), name='college-create'),
]