from web.models import Job
import datetime
import os

def create_job(job_title, end_time, total_num):
    try:
        path = 'C:\\' + job_title
        os.mkdir(path)
        j = Job()
        j.job_title = job_title
        j.start_time = datetime.datetime.now()
        j.end_time = end_time
        j.total_num = total_num
        j.submit_num = 0
        j.save()
        result = {
            'statues': 1,
            'msg': 'OK',
        }
        return result
    except Exception as e:
        print('create error')
        print(e)
        result = {
            'statues': 0,
            'msg': 'error',
        }
        return result
