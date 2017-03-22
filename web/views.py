from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from web.controller.json_tool import dict_to_json
from web.controller.dologin import login_service
import json
from web.controller.SubmitJobService import submit_job

# Create your views here.

def view_submit_job(request):
    student_id = request.session.get('student_id')
    job_id = request.POST.get('job_id')
    file = request.FILES['file']
    result = json.dumps(submit_job(student_id, job_id, file))




def login(request):
    return render_to_response('login.html')


def doLogin(request):
    array = login_service(request)
    if array['state'] == 1:
       return HttpResponse(dict_to_json(array))
    else:
       return HttpResponse(dict_to_json(array))