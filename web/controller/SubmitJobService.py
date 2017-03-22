from web.models import JobSubmission, Job, User
import datetime
import os

def submit_job(student_id, job_id, file):
    try:
        j1 = Job.objects.filter(job_id=job_id).first()
        j2 = JobSubmission.objects.filter(student_id=student_id, job_id=job_id).first()
        u = User.objects.filter(student_id=student_id).first()
        if not j2:
            j1.submit_num = j1.submit_num + 1
            j = JobSubmission()
            j.job_id = job_id
            j.student_id = student_id
            j.sub_time = datetime.datetime.now()
            file.name = '软件工程一班_' + u.num + '_' + u.name + '_实验2.txt'
            j.file_name = file.name
            path = 'C:\\' + j1.job_title
            destination = open(os.path.join(path, file.name), 'wb+')  # 打开特定的文件进行二进制的写操作
            for chunk in file.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            j.save()
            j1.save()
            result = {
                'statues': 1,
                'msg': 'OK'
            }
        else:
            file.name = '软件工程一班_' + u.num + '_' + u.name + '_实验2.txt'
            j2.job_id = job_id
            j2.student_id = student_id
            j2.sub_time = datetime.datetime.now()
            j2.file_name = file.name
            j2.save()
            path = 'C:\\' + j1.job_title
            destination = open(os.path.join(path, file.name), 'wb+')  # 打开特定的文件进行二进制的写操作
            for chunk in file.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
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


