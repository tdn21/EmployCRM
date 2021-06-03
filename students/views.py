from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse
from django.views import generic
from .mixins import AdminAndLoginRequiredMixin
from .forms import NewStudentModelForm, StudentModelForm, CustomUserCreationForm

User = get_user_model()


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class StudentListView(AdminAndLoginRequiredMixin, generic.ListView):
    template_name = "students/student_list.html"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        return queryset


class StudentCreateView(AdminAndLoginRequiredMixin, generic.CreateView):
    template_name = "students/student_create.html"
    form_class = NewStudentModelForm

    def get_success_url(self):
        return reverse("students:student-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = f"{user.first_name}_{user.college_roll_number}"
        user.is_admin = False
        user.set_password(user.phone_number)
        user.save()

        return super(StudentCreateView, self).form_valid(form)


class StudentDetailView(AdminAndLoginRequiredMixin, generic.DetailView):
    template_name = "students/student_detail.html"
    context_object_name = "student"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        return queryset


class StudentUpdateView(AdminAndLoginRequiredMixin, generic.UpdateView):
    template_name = "students/student_update.html"
    form_class = StudentModelForm
    context_object_name = "student"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        return queryset

    def get_success_url(self):
        return reverse("students:student-list")


class StudentDeleteView(AdminAndLoginRequiredMixin, generic.DeleteView):
    template_name = "students/student_delete.html"
    context_object_name = "student"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        return queryset

    def get_success_url(self):
        return reverse("students:student-list")