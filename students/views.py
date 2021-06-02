import csv
import io
from builtins import next, Exception

from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse,redirect
from django.views import generic
from .mixins import AdminAndLoginRequiredMixin
from django.contrib import messages


from tasks.models import Student
from .forms import NewStudentModelForm, StudentModelForm

User = get_user_model()

class StudentListView(AdminAndLoginRequiredMixin, generic.ListView):
    template_name = "students/student_list.html"

    def get_queryset(self):
        return Student.objects.all()


class StudentCreateView(AdminAndLoginRequiredMixin, generic.CreateView):
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

class UploadStudents(AdminAndLoginRequiredMixin, generic.CreateView):
    def get(self, request):
        template="students/upload_students.html"
        context={
            'file_description': 'Order of CSV fil should be First Name, Last Name, Roll Number, Phone Number, Email Address.'
        }
        return render(request,template,context)
    def post(self,request):
        template = "students/upload_students.html"
        try:
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'THIS IS NOT A CSV FILE')
            try:
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                for data in csv.reader(io_string, delimiter=',', quotechar="|"):
                    user = User(
                        username=data[2],
                        first_name=data[0],
                        last_name=data[1],
                        phone_number=data[3],
                        email=data[4],
                    )
                    user.is_admin=False
                    user.set_password(user.phone_number)
                    user.save()
                    _, created = Student.objects.update_or_create(
                        user=user,
                        first_name=data[0],
                        last_name=data[1],
                        phone_number=data[3],
                        email=data[4],
                        college_roll_number=data[2],
                    )
                messages.error(request,"Your data")
                return reverse("students:student-list")
            except Exception as e:
                messages.error(request, e)
                return render(request,template)
        except:
            messages.error(request,"Choose a CSV File.")
            return render(request,template)

class StudentDetailView(AdminAndLoginRequiredMixin, generic.DetailView):
    template_name = "students/student_detail.html"
    context_object_name = "student"

    def get_queryset(self):
        return Student.objects.all()


class StudentUpdateView(AdminAndLoginRequiredMixin, generic.UpdateView):
    template_name = "students/student_update.html"
    form_class = StudentModelForm

    def get_queryset(self):
        return Student.objects.all()

    def get_success_url(self):
        return reverse("students:student-list")


class StudentDeleteView(AdminAndLoginRequiredMixin, generic.DeleteView):
    template_name = "students/student_delete.html"
    context_object_name = "student"

    def get_queryset(self):
        return Student.objects.all()

    def get_success_url(self):
        return reverse("students:student-list")