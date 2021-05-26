from django import contrib
from django.contrib import messages
from django.core.mail import send_mail
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic

from .models import Task
from .forms import TaskForm, TaskModelForm, CustomUserCreationForm


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class TaskListView(LoginRequiredMixin, generic.ListView):
    template_name = "tasks/task_list.html"
    queryset = Task.objects.all()
    context_object_name = "tasks"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "tasks/task_detail.html"
    queryset = Task.objects.all()
    context_object_name = "task"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "tasks/task_create.html"
    form_class = TaskModelForm

    def get_success_url(self):
        return reverse("tasks:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "tasks/task_update.html"
    queryset = Task.objects.all()
    form_class = TaskModelForm

    def get_success_url(self):
        return reverse("tasks:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "tasks/task_delete.html"
    queryset = Task.objects.all()

    def get_success_url(self):
        return reverse("tasks:task-list")


# def task_update(request, pk):
#     task = Task.objects.get(id=pk)
#     form = TaskForm()
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             project_name = form.cleaned_data['project_name']
#             task_name = form.cleaned_data['task_name']
#             description = form.cleaned_data['description']
#             task.project_name = project_name
#             task.task_name = task_name
#             task.description = description
#             task.save()
#             return redirect("/tasks/")
#     context = {
#         "task": task,
#         "form": form
#     }
#     return render(request, "tasks/task_update.html", context)


# def task_update(request, pk):
#     task = Task.objects.get(id=pk)
#     form = TaskModelForm(instance=task)
#     if request.method == "POST":
#         form = TaskModelForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect(f"/tasks/{pk}/")
#     context = {
#         "form": form,
#         "task": task
#     }
#     return render(request, "tasks/task_update.html", context)
