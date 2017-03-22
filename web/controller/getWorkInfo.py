from web.models import JobSubmission, Job, User
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import response

def getnumberbyid(jobId):
    allJob = getAllSubInfoById(jobId)
    return len(allJob),55-len(allJob)

def getAllJobInfoAsList():
    datalist = []

    for i in getAllJobInfo():
        arr = {
            'job_id': i.job_id,
            'job_title': i.job_title,
            'start_time': i.start_time,
            'end_time': i.end_time,
            'total_num': i.total_num,
            'submit_num': i.submit_num,
            'other_num':i.total_num - i.submit_num
        }
        datalist.append(arr)
    return datalist

def getAllSubInfoById(jobId):

    return JobSubmission.objects.filter(job_id=int(jobId)).all()

def getAllUser():
    return User.objects.filter().all()

def getRestUser(jobId):
    datalist = []
    result = []
    for i in getAllUser():
        datalist.append(i.student_id)
    print(len(datalist))
    print(len(getAllSubInfoById(jobId)))
    for i in getAllSubInfoById(jobId):
        if i.student_id in datalist:
            datalist.remove(i.student_id)
    for i in datalist:
        arr = {
            'username':User.objects.filter(student_id= i).first().name
        }
        result.append(arr)
    return result
def getAllJobInfo():
    print(Job.objects.filter)
    return Job.objects.filter()