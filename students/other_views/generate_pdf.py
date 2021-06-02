from datetime import datetime
from io import BytesIO

from django.shortcuts import redirect
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from base.models.employee import Employee

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
            employee = Employee.get_employee_by_id(request.session.get('employee_id'))
            #if letter.permission_required:
            #    return redirect('index_page')
            context = {
                "employee":employee
            }
            context['DateofissuedCertificate']=datetime.today().date()
            page_name=request.session.get('page_name')
            pdf = render_to_pdf(page_name,context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = employee.StudentName +"_"+page_name+"_from_medicento.pdf"
                content = "inline; filename=%s" % (filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename=%s" % (filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")
        except Exception as e:
            print(e)
            return redirect('index_page')