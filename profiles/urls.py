from profiles.views import ProfileCreateView, ProfileDeleteView, ProfileDetailView, ProfileListView, ProfileUpdateView
from django.urls import path

app_name = "profiles"

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('<int:pk>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    path('create/', ProfileCreateView.as_view(), name='profile-create'),
]