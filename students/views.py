import datetime
import csv
import io
from builtins import next, Exception
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminAndLoginRequiredMixin
from .forms import IssueCompletionLetter, IssueOfferLetter, NewStudentModelForm, RequestCompletionLetter, RequestOfferLetter, StudentModelForm, CustomUserCreationForm, StudentUpdateDetailForm

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


class StudentUpdateDetailView(LoginRequiredMixin, generic.UpdateView):
    template_name = "students/student_update_detail.html"
    form_class = StudentUpdateDetailForm
    context_object_name = "student"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        return queryset

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_updated = True 
        user.save()

        return super(StudentUpdateDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse("students:student-my-detail", kwargs={'pk': self.kwargs['pk']})


class StudentMyDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "students/student_my_detail.html"
    context_object_name = "student"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        return queryset


class RequestOfferLetterView(LoginRequiredMixin, generic.UpdateView):
    template_name = "students/student_request_offer_letter.html"
    form_class = RequestOfferLetter
    context_object_name = "student"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        return queryset

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_offer_letter_requested = True 
        user.save()

        return super(RequestOfferLetterView, self).form_valid(form)

    def get_success_url(self):
        return reverse("students:student-request-offer-letter", kwargs={'pk': self.kwargs['pk']})


class RequestCompletionLetterView(LoginRequiredMixin, generic.UpdateView):
    template_name = "students/student_request_completion_letter.html"
    form_class = RequestCompletionLetter
    context_object_name = "student"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        return queryset

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_completion_letter_requested = True 
        user.save()

        return super(RequestCompletionLetterView, self).form_valid(form)

    def get_success_url(self):
        return reverse("students:student-request-completion-letter", kwargs={'pk': self.kwargs['pk']})


class OfferLetterRequestListView(AdminAndLoginRequiredMixin, generic.ListView):
    template_name = "students/student_offer_letter_request_list.html"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        queryset = queryset.filter(is_offer_letter_requested = True)
        queryset = queryset.filter(is_offer_letter_issued = False)
        return queryset


class IssueOfferLetterView(AdminAndLoginRequiredMixin, generic.UpdateView):
    template_name = "students/student_issue_offer_letter.html"
    form_class = IssueOfferLetter
    context_object_name = "student"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        return queryset

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_offer_letter_issued = True 
        user.offer_letter_issue_date = datetime.date.today()
        user.save()

        return super(IssueOfferLetterView, self).form_valid(form)

    def get_success_url(self):
        return reverse("students:student-offer-letter-request-list")


class CompletionLetterRequestListView(AdminAndLoginRequiredMixin, generic.ListView):
    template_name = "students/student_completion_letter_request_list.html"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        queryset = queryset.filter(is_completion_letter_requested = True)
        queryset = queryset.filter(is_completion_letter_issued = False)
        return queryset


class IssueCompletionLetterView(AdminAndLoginRequiredMixin, generic.UpdateView):
    template_name = "students/student_issue_completion_letter.html"
    form_class = IssueCompletionLetter
    context_object_name = "student"

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = queryset.filter(is_admin = False)
        return queryset

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_completion_letter_issued = True 
        user.completion_letter_issue_date = datetime.date.today()
        user.save()

        return super(IssueCompletionLetterView, self).form_valid(form)

    def get_success_url(self):
        return reverse("students:student-completion-letter-request-list")


class StudentsUploadView(AdminAndLoginRequiredMixin, generic.CreateView):
    def get(self, request):
        template="students/student_upload.html"
        context={
            'file_description': 'Order of CSV file should be First Name, Last Name, Roll Number, Phone Number, Email Address.'
        }
        return render(request,template,context)
    def post(self,request):
        template = "students/student_upload.html"
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
                        first_name=data[0],
                        last_name=data[1],
                        college_roll_number=data[2],
                        phone_number=data[3],
                        email=data[4],
                    )
                    user.username = f"{user.first_name}_{user.college_roll_number}"
                    user.is_admin=False
                    user.set_password(user.phone_number)
                    user.save()
                # messages.error(request,"Your data")
                return reverse("students:student-list")
            except Exception as e:
                messages.error(request, e)
                return render(request,template)
        except:
            messages.error(request,"Choose a CSV File.")
            return render(request,template)