from web.models import JobSubmission
import datetime
import os

def submit_job(student_id, job_id, file):
    try:
        j = JobSubmission()
        j.job_id =  job_id
        j.student_id = student_id
        j.sub_time = datetime.datetime.now()
        j.file_name = file.name
        path = 'E:\\upload'
        destination = open(os.path.join(path, file.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in file.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        j.save()
        result = {
            'statues': 1,
            'msg': 'OK'
        }
        return result
    except Exception as e:
        print("sub_error")
        print(e)
        result = {
            'statues': 0,
            'msg': 'error'
        }
        return result


