from links.views import LinkCreateView, LinkDeleteView, LinkDetailView, LinkListView, LinkUpdateView
from django.urls import path

app_name = "links"

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('<int:pk>/', LinkDetailView.as_view(), name='link-detail'),
    path('<int:pk>/update/', LinkUpdateView.as_view(), name='link-update'),
    path('<int:pk>/delete/', LinkDeleteView.as_view(), name='link-delete'),
    path('create/', LinkCreateView.as_view(), name='link-create'),
]