from web.models import JobSubmission, Job
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import response

def getnumberbyid(jobId):
    allJob = getallinfobyid(jobId)
    return len(allJob),55-len(allJob)


def getallinfobyid(jobId):
    return JobSubmission.objects.filter(job_id=jobId)