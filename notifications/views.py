from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse
from django.views import generic
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from students.mixins import AdminAndLoginRequiredMixin
from students.models import Message
from .forms import AdminCreateMessageForm, CreateMessageForm, StudentCreateMessageForm

User = get_user_model()


# class MessageListView(LoginRequiredMixin, generic.ListView):
#     template_name = "notifications/message_list.html"

#     def get_queryset(self):
#         user = self.request.user
#         pk = self.kwargs.get('pk')
#         other_user = User.objects.get(id=pk)
#         queryset = Message.objects.all()
#         queryset = queryset.filter(Q(origin=user, destination=other_user) | Q(origin=other_user, destination=user))
#         return queryset.order_by('date')


class MessageListView(LoginRequiredMixin, generic.CreateView):
    template_name = "notifications/create_message_copy.html"
    form_class = CreateMessageForm

    def get_success_url(self):
        return reverse("notifications:conversation-list")

    def form_valid(self, form):
        message = form.save(commit=False)
        message.origin = self.request.user
        message.destination = User.objects.get(id=self.kwargs.get('pk'))
        message.save()

        return super(MessageListView, self).form_valid(form)

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs.get('pk')
        other_user = User.objects.get(id=pk)
        queryset = Message.objects.all()
        queryset = queryset.filter(Q(origin=user, destination=other_user) | Q(origin=other_user, destination=user))
        return queryset.order_by('date')

    def get_context_data(self, *args, **kwargs):
        context = super(MessageListView, self).get_context_data(**kwargs)
        context.update({
            "object_list": self.get_queryset(),
            "other_user": User.objects.get(id=self.kwargs.get('pk'))
        })
        return context


class ConversationListView(LoginRequiredMixin, generic.ListView):
    template_name = "notifications/conversations_list.html"

    def get_queryset(self):
        user = self.request.user
        queryset = user.origin.all()
        destination_queryset = user.destination.all()
        queryset = queryset.union(destination_queryset)

        users = set()
        for message in queryset:
            if message.origin == user :
                users.add(message.destination)
            else :
                users.add(message.origin)

        return users


class StudentCreateMessageView(LoginRequiredMixin, generic.CreateView):
    template_name = "notifications/create_message.html"
    form_class = StudentCreateMessageForm

    def get_success_url(self):
        return reverse("notifications:message-list")

    def form_valid(self, form):
        message = form.save(commit=False)
        message.origin = self.request.user
        message.save()

        return super(StudentCreateMessageView, self).form_valid(form)


class AdminCreateMessageView(AdminAndLoginRequiredMixin, generic.CreateView):
    template_name = "notifications/create_message.html"
    form_class = AdminCreateMessageForm

    def get_success_url(self):
        return reverse("notifications:message-list")

    def form_valid(self, form):
        message = form.save(commit=False)
        message.origin = self.request.user
        message.save()

        return super(AdminCreateMessageView, self).form_valid(form)


class CreateMessageView(LoginRequiredMixin, generic.CreateView):
    template_name = "notifications/create_message.html"
    form_class = CreateMessageForm

    def get_success_url(self):
        return reverse("notifications:message-list")

    def form_valid(self, form):
        message = form.save(commit=False)
        message.origin = self.request.user
        message.destination = User.objects.get(id=self.kwargs.get('pk'))
        message.save()

        return super(CreateMessageView, self).form_valid(form)