from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse
from django.views import generic
from students.mixins import AdminAndLoginRequiredMixin
from students.models import Profile
from .forms import ProfileModelForm

User = get_user_model()

class ProfileListView(AdminAndLoginRequiredMixin, generic.ListView):
    template_name = "profiles/profile_list.html"

    def get_queryset(self):
        return Profile.objects.all()


class ProfileCreateView(AdminAndLoginRequiredMixin, generic.CreateView):
    template_name = "profiles/profile_create.html"
    form_class = ProfileModelForm

    def get_success_url(self):
        return reverse("profiles:profile-list")


class ProfileDetailView(AdminAndLoginRequiredMixin, generic.DetailView):
    template_name = "profiles/profile_detail.html"
    context_object_name = "profile"

    def get_queryset(self):
        return Profile.objects.all()


class ProfileUpdateView(AdminAndLoginRequiredMixin, generic.UpdateView):
    template_name = "profiles/profile_update.html"
    form_class = ProfileModelForm

    def get_queryset(self):
        return Profile.objects.all()

    def get_success_url(self):
        return reverse("profiles:profile-list")


class ProfileDeleteView(AdminAndLoginRequiredMixin, generic.DeleteView):
    template_name = "profiles/profile_delete.html"
    context_object_name = "profile"

    def get_queryset(self):
        return Profile.objects.all()

    def get_success_url(self):
        return reverse("profiles:profile-list")