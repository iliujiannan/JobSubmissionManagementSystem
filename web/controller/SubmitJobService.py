from web.models import JobSubmission

def submit_job(student_id, job_id, file):
    j = JobSubmission()
    j.job_id =  job_id
    j.student_id = student_id
    j.file_name = file.
