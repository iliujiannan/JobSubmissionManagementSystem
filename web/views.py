from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from web.controller.json_tool import dict_to_json
from web.controller.dologin import login_service
import json
from web.controller.SubmitJobService import submit_job
from django.views.decorators.csrf import csrf_exempt
from web.controller.getWorkInfo import *

# Create your views here.

@csrf_exempt
def f(request):
    id = request.GET.get('id')
    print(1111111)
    print(type(id))
    return render_to_response('submitjob.html',{'id':id})


@csrf_exempt
def c(request):
    return render_to_response('createjob.html')

def hide(request):
    return render_to_response('admin.html')

@csrf_exempt
def view_submit_job(request):
    student_id = request.session.get('student_id')
    # job_id = request.POST.get('job_id')
    #student_id = 1
    print('qqqq')
    print(request.POST.get('id'))
    job_id = int(request.POST.get('id'))
    file = request.FILES['file']
    result = json.dumps(submit_job(student_id, job_id, file))
    return render_to_response('index.html')


def login(request):
    return render_to_response('login.html')


def doLogin(request):
    array = login_service(request)
    if array['state'] == 1:
       return HttpResponse(dict_to_json(array))
    else:
       return HttpResponse(dict_to_json(array))


def work_list(request):
    student_id = request.session.get('student_id')
    array = {
        'UserNumber': request.session['student_id'],
        'data': getAllJobInfoAsList(),
    }
    return render_to_response('worklist.html',array)



def allwork(request):
    return render_to_response('showwork.html',{'data':getAllJobInfoAsList()})
def restUser(request):
    print(request.GET.get('job_id'))
    return HttpResponse(json.dumps(getRestUser(request.GET.get('job_id'))))
def showreset(request):
    r = getRestUser(request.GET.get('job_id'))
    return render_to_response('restuser.html',{'data':r})