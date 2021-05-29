from django import contrib
from django.contrib import messages
from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic

from .models import Task, Student
from .forms import TaskForm, TaskModelForm, CustomUserCreationForm


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class TaskListView(LoginRequiredMixin, generic.ListView):
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = Task.objects.all()
        if not self.request.user.is_admin:
            queryset = queryset.filter(student__user = self.request.user)
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "tasks/task_detail.html"
    context_object_name = "task"

    def get_queryset(self):
        queryset = Task.objects.all()
        if not self.request.user.is_admin:
            queryset = queryset.filter(student__user = self.request.user)
        return queryset


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "tasks/task_create.html"
    form_class = TaskModelForm

    def get_success_url(self):
        return reverse("tasks:task-list")

    def form_valid(self, form):
        task = form.save(commit=False)
        task.student = Student.objects.get(user=self.request.user)
        task.save()
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "tasks/task_update.html"
    form_class = TaskModelForm

    def get_queryset(self):
        queryset = Task.objects.all()
        if not self.request.user.is_admin:
            queryset = queryset.filter(student__user = self.request.user)
        return queryset

    def get_success_url(self):
        return reverse("tasks:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "tasks/task_delete.html"

    def get_queryset(self):
        queryset = Task.objects.all()
        if not self.request.user.is_admin:
            queryset = queryset.filter(student__user = self.request.user)
        return queryset

    def get_success_url(self):
        return reverse("tasks:task-list")