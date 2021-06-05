from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from students.mixins import AdminAndLoginRequiredMixin
from students.models import Link
from .forms import LinkModelForm

User = get_user_model()

class LinkListView(LoginRequiredMixin, generic.ListView):
    template_name = "links/link_list.html"

    def get_queryset(self):
        return Link.objects.all()


class LinkCreateView(AdminAndLoginRequiredMixin, generic.CreateView):
    template_name = "links/link_create.html"
    form_class = LinkModelForm

    def get_success_url(self):
        return reverse("links:link-list")


class LinkDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "links/link_detail.html"
    context_object_name = "link"

    def get_queryset(self):
        return Link.objects.all()


class LinkUpdateView(AdminAndLoginRequiredMixin, generic.UpdateView):
    template_name = "links/link_update.html"
    form_class = LinkModelForm

    def get_queryset(self):
        return Link.objects.all()

    def get_success_url(self):
        return reverse("links:link-list")


class LinkDeleteView(AdminAndLoginRequiredMixin, generic.DeleteView):
    template_name = "links/link_delete.html"
    context_object_name = "link"

    def get_queryset(self):
        return Link.objects.all()

    def get_success_url(self):
        return reverse("links:link-list")