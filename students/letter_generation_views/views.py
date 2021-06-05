import datetime
from io import BytesIO

from xhtml2pdf import pisa
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import get_template

User = get_user_model()

def render_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()

     #This part will create the pdf.
     pdf = pisa.pisaDocument(BytesIO(html.encode("utf8")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None


# Creating our view, it is a class based view
class GeneratePdf(View):
    def get(self, request):
        try:
            student = request.user
            context = {
                "student":student
            }
            folder_name=str(request.session.get('folder_name'))
            template_name = str(request.session.get('template_name'))
            page_name=folder_name+"/"+template_name
            print(page_name)
            pdf = render_to_pdf(page_name,context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename =  student.username + ".pdf"
                content = "inline; filename=%s" % (filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=%s" % (filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")
        except Exception as e:
            print("Error")
            print(e)
            return HttpResponse("Some Error Occured!!")


class DownloadOfferLetterView(LoginRequiredMixin, generic.DetailView):
    def get(self,request):
        student=request.user
        if student.is_offer_letter_issued:
            request.session['folder_name']='offer_letter'
            request.session['template_name'] ='offer_letter_template.html'
            return redirect('students:download-pdf')
        else:
            if not student.is_offer_letter_requested:
                msg="PLEASE REQUEST FOR OFFER LETTER"
                return HttpResponse(msg)
            else:
                msg="PLEASE WAIT FOR ADMIN TO ALLOW OFFER LETTER REQUEST"
                return HttpResponse(msg)


class DownloadCompletionLetterView(LoginRequiredMixin,View):
    def get(self,request):
        student=request.user
        student.internship_completion_date = student.get_end_date()
        student.save()
        if student.is_completion_letter_issued:
            request.session['folder_name']='completion_letter'
            request.session['template_name'] ='completion_letter_template.html'
            return redirect('students:download-pdf')
        else:
            if not student.is_completion_letter_requested:
                msg="PLEASE REQUEST FOR COMPLETION LETTER"
                return HttpResponse(msg)
            else:
                msg="PLEASE CLICK ON ENABLE DOWNLOAD COMPLETION LETTER BUTTON IN PREVIEW COMPLETION LETTER SECTION TO DOWNLOAD COMPLETION LETTER"
                return HttpResponse(msg)