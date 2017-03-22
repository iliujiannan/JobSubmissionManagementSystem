from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import json

# Create your views here.

def submit_job(request):
    student_id = request.session.get('student_id')
    job_id = request.POST.get('job_id')
    file = request.FILES['file']



def login(request):
    return render_to_response('login.html')


def doLogin(request):
    pass