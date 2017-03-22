from django.http import HttpResponse
import json

# Create your views here.

def submit_job(request):
    student_id = request.session.get('student_id')
    job_id = request.POST.get('job_id')
    file = request.FILES['file']


