from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.models import Student
from .forms import StudentModelForm


class StudentListView(LoginRequiredMixin, generic.ListView):
    template_name = "students/student_list.html"

    def get_queryset(self):
        return Student.objects.all()


class StudentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "students/student_create.html"
    form_class = StudentModelForm

    def get_success_url(self):
        return reverse("students:student-list")

    def form_valid(self, form):
        student = form.save(commit=False)
        student.user = self.request.user
        student.save()
        return super(StudentCreateView, self).form_valid(form)