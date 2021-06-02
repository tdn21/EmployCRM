import datetime

from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.views import View
from base.models.employee import Employee

class CompletionCertificate(AdminAndLoginRequiredMixin,View):

    def get(self,request):
        try:
            employee_id=request.session.get('employee_id')
            employee=Employee.get_employee_by_id(employee_id)
            data={}
            data['employee']=employee
            data['DateofissuedCertificate']=datetime.date.today()
            return render(request,'completion_certificate.html',data)
        except Exception as e:
            print(e)
            return HttpResponse("Something Went Wrong. Please Try it Again!!.")

    def post(self,request):
        try:
            employee_id=request.session.get('employee_id')
            employee=Employee.get_employee_by_id(employee_id)
            if employee.request_for_certificate:
                if employee.certificate_granted:
                    request.session['page_name']='completion_certificate_template.html'
                    return redirect('pdf')
                else:
                    message = "Please ask the admin to Enable The Permission To Download Completion Certificate."
                    data = {}
                    data['employee'] = employee
                    data['message']=message
                    data['DateofissuedCertificate'] = datetime.date.today()
                    return render(request, 'completion_certificate.html', data)
            else:
                employee.request_for_certificate = True
                employee.update_employee()
                message = "Please ask the admin to Enable The Permission To Download Completion Certificate."
                data = {}
                data['employee'] = employee
                data['message'] = message
                data['DateofissuedCertificate'] = datetime.date.today()
                return render(request, 'completion_certificate.html', data)
        except:
            return HttpResponse("Something Went Wrong. Please Try it Again!!.")

