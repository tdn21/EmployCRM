import datetime

from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Student


class PreviewCompletionLetter(LoginRequiredMixin,View):

    def get(self, request):
        student = Student.get_student_object_by_user(request.user)
        student.completion_letter_issue_date = datetime.date.today()
        student.internship_completion_date=student.get_end_date()
        student.save()
        data = {'student': student}
        return render(request, 'completion_letter/preview_completion_letter.html', data)

    def post(self,request):
        student = Student.get_student_object_by_user(request.user)
        if not student.request_for_completion_letter:
            if student.is_properly_updated():
                student.request_for_completion_letter = True
                student.save()
                return redirect('tasks:preview-completion-letter')
            else:
                messages.info(request, 'PLEASE FILL YOUR DETAILS PROPERLY')
                return redirect('tasks:preview-completion-letter')
        else:
            if student.is_offer_letter_issued:
                student.enable_completion_letter_download = True;
                student.save()
                messages.info(request, 'NOW YOU CAN DOWNLOAD YOUR COMPLETION CERTIFICATE')
                return redirect('tasks:preview-completion-letter')
            else:
                return redirect('tasks:preview-completion-letter')

class DownloadCompletionLetterView(LoginRequiredMixin,View):
    def get(self,request):
        student=Student.get_student_object_by_user(request.user)
        if student.enable_offer_letter_download or student.enable_completion_letter_download_urgent:
            request.session['folder_name']='completion_letter'
            request.session['template_name'] ='completion_letter_template.html'
            return redirect('tasks:download-pdf')
        else:
            if not student.request_for_offer_letter:
                msg="PLEASE REQUEST FOR COMPLETION LETTER"
                return HttpResponse(msg)
            else:
                msg="PLEASE CLICK ON ENABLE DOWNLOAD COMPLETION LETTER BUTTON IN PREVIEW COMPLETION LETTER SECTION TO DOWNLOAD COMPLETION LETTER"
                return HttpResponse(msg)

