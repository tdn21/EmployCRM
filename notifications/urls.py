from .views import AdminCreateMessageView, CreateMessageView, StudentCreateMessageView, ConversationListView, MessageListView
from django.urls import path

app_name = "notifications"

urlpatterns = [
    path('', ConversationListView.as_view(), name='conversation-list'),
    path('<int:pk>/', MessageListView.as_view(), name='message-list'),
    path('<int:pk>/create', CreateMessageView.as_view(), name='create-message'),
    path('a_start_conversation/', AdminCreateMessageView.as_view(), name='admin-start-conversation'),
    path('s_start_conversation/', StudentCreateMessageView.as_view(), name='student-start-conversation'),
]