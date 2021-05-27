from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse
from django.views import generic
from students.mixins import AdminAndLoginRequiredMixin

from tasks.models import College
from .forms import CollegeModelForm

User = get_user_model()

class CollegeListView(AdminAndLoginRequiredMixin, generic.ListView):
    template_name = "colleges/college_list.html"

    def get_queryset(self):
        return College.objects.all()


class CollegeCreateView(AdminAndLoginRequiredMixin, generic.CreateView):
    template_name = "colleges/college_create.html"
    form_class = CollegeModelForm

    def get_success_url(self):
        return reverse("colleges:college-list")


class CollegeDetailView(AdminAndLoginRequiredMixin, generic.DetailView):
    template_name = "colleges/college_detail.html"
    context_object_name = "college"

    def get_queryset(self):
        return College.objects.all()


class CollegeUpdateView(AdminAndLoginRequiredMixin, generic.UpdateView):
    template_name = "colleges/college_update.html"
    form_class = CollegeModelForm

    def get_queryset(self):
        return College.objects.all()

    def get_success_url(self):
        return reverse("colleges:college-list")


class CollegeDeleteView(AdminAndLoginRequiredMixin, generic.DeleteView):
    template_name = "colleges/college_delete.html"
    context_object_name = "college"

    def get_queryset(self):
        return College.objects.all()

    def get_success_url(self):
        return reverse("colleges:college-list")