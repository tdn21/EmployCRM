from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.models import Student
from .forms import NewStudentModelForm, StudentModelForm

User = get_user_model()

class StudentListView(LoginRequiredMixin, generic.ListView):
    template_name = "students/student_list.html"

    def get_queryset(self):
        return Student.objects.all()


class StudentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "students/student_create.html"
    form_class = NewStudentModelForm

    def get_success_url(self):
        return reverse("students:student-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_admin = False
        user.set_password(user.phone_number)
        user.save()

        Student.objects.create(
            user=user,
            first_name=user.first_name,
            last_name=user.last_name,
            phone_number=user.phone_number,
            email=user.email,
            college_roll_number=user.username
        )

        return super(StudentCreateView, self).form_valid(form)


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "students/student_detail.html"
    context_object_name = "student"

    def get_queryset(self):
        return Student.objects.all()


class StudentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "students/student_update.html"
    form_class = StudentModelForm

    def get_queryset(self):
        return Student.objects.all()

    def get_success_url(self):
        return reverse("students:student-list")


class StudentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "students/student_delete.html"
    context_object_name = "student"

    def get_queryset(self):
        return Student.objects.all()

    def get_success_url(self):
        return reverse("students:student-list")