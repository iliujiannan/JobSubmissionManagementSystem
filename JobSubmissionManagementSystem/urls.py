"""JobSubmissionManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from web.views import login, doLogin, f, view_submit_job, hide, c, job_create, allwork,work_list

from web.views import login, doLogin, f, view_submit_job, hide, c, allwork, restUser, showreset, work_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login', login),
    url(r'^dologin', doLogin),
    url(r'^hide', hide),
    url(r'^e', f),
    url(r'^submit_job', view_submit_job),
    url(r'^c', c),
    url(r'^jobcreating', job_create),
    url(r'^allwork',allwork),
    url(r'^therest',restUser),
    url(r'^showreset',showreset),
    url(r'^worklist', work_list),
]
