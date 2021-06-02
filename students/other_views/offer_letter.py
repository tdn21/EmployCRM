from django.shortcuts import render,redirect
from django.http import request, HttpResponse
from django.views import View
from base.models.employee import Employee
from base.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class OfferLetterView(AdminAndLoginRequiredMixin,View):
    def get(self,request):
        try:
            employee_id=request.session.get('employee_id')
            employee=Employee.get_employee_by_id(employee_id)
            data={}
            data['employee']=employee
            return render(request,'offer_letter.html',data)
        except Exception as e:
            print(e)
            return HttpResponse("Something Went Wrong. Please Try it Again!!.")

    def post(self,request):
        try:
            employee_id=request.session.get('employee_id')
            employee=Employee.get_employee_by_id(employee_id)
            if employee.request_for_offer_letter:
                if employee.offer_letter_granted:
                    request.session['page_name']='offer_letter_template.html'
                    return redirect('pdf')
                else:
                    message = "Please ask the admin to Enable The Permission To Download Offer Letter."
                    data = {}
                    data['employee'] = employee
                    data['message']=message
                    return render(request, 'offer_letter.html', data)
            else:
                employee.request_for_offer_letter = True
                employee.update_employee()
                message = "Please ask the admin to Enable The Permission To Download Offer Letter."
                data = {}
                data['employee'] = employee
                data['message'] = message
                return render(request, 'offer_letter.html', data)
        except Exception as e:
            print(e)
            return HttpResponse("Something Went Wrong. Please Try it Again!!.")

