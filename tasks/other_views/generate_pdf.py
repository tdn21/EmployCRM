from datetime import datetime
from io import BytesIO

from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from tasks.models import Student

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
            student=Student.get_student_object_by_user(request.user)
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
                filename =  student.first_name+"_"+student.last_name+".pdf"
                content = "inline; filename=%s" % (filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=%s" % (filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")
        except Exception as e:
            print(e)
            return HttpResponse("Some Error Occured.")