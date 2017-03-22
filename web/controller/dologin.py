from web.models import User
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import response

def login_service(request):
    num = request.GET.get('num')
    PassWord = request.GET.get('PassWord')
    u = User.objects.filter(num=num).first()
    print(num)
    if u is not None and u.num == PassWord:
        request.session['student_id'] = u.student_id
        print(request.session['student_id'])
        msg = '学生登陆'
        state = 1
    else:
        request.session['num'] = ""
        msg = '账号或密码错误'
        state = 0
    array = {
        'msg': msg,
        'state': state
    }
    return array