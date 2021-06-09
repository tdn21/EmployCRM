from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic
from tasks.models import Student


class OfferLetterView(LoginRequiredMixin,generic.DetailView):
    def get(self, request):
        try:
            return render(request,'offer_letter/terms_condition.html')
        except Exception as e:
            return HttpResponse("Something Went Wrong. Please Try it Again!!.")

class PreviewOfferLetterView(LoginRequiredMixin,generic.DetailView):
    def get(self, request):
        student = Student.get_student_object_by_user(request.user)
        data={'student':student}
        return render(request, 'offer_letter/preview_offer_letter.html', data)

    def post(self,request):
        student=Student.get_student_object_by_user(request.user)
        print (student)
        if not student.request_for_offer_letter:
                if student.is_properly_updated():
                    student.request_for_offer_letter = True
                    student.save()
                    return redirect('tasks:preview-offer-letter')
                else:
                    messages.info(request, 'PLEASE FILL YOUR DETAILS PROPERLY')
                    return redirect('tasks:preview-offer-letter')
        else:
            if student.is_offer_letter_issued:
                student.enable_offer_letter_download=True;
                student.save()
                return redirect('tasks:preview-offer-letter')
            else:
                return redirect('tasks:preview-offer-letter')

class DownloadOfferLetterView(LoginRequiredMixin,generic.DetailView):
    def get(self,request):
        student=Student.get_student_object_by_user(request.user)
        if student.enable_offer_letter_download:
            request.session['folder_name']='offer_letter'
            request.session['template_name'] ='offer_letter_template.html'
            return redirect('tasks:download-pdf')
        else:
            if not student.request_for_offer_letter:
                msg="PLEASE REQUEST FOR OFFER LETTER"
                return HttpResponse(msg)
            else:
                msg="PLEASE CLICK ON ENABLE DOWNLOAD OFFER LETTER BUTTON IN PREVIEW OFFER LETTER SECTION TO DOWNLOAD OFFER LETTER"
                return HttpResponse(msg)