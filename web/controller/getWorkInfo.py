from web.models import JobSubmission, Job
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import response

def getnumberbyid(jobId):
    allJob = geAllSubInfoById(jobId)
    return len(allJob),55-len(allJob)

def getAllJobInfoAsList():
    datalist = []

    for i in getAllJobInfo():
        arr = {
            'jobid': i.job_id,
            'job_title': i.job_title,
            'start_time': i.start_time,
            'end_time': i.end_time,
            'total_num': i.total_num,
            'submit_num': i.submit_num
        }
        datalist.append(arr)
    return datalist

def geAllSubInfoById(jobId):
    return JobSubmission.objects.filter(job_id=jobId)

def getAllJobInfo():
    return Job.objects