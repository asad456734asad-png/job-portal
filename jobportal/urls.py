"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django .contrib import admin
from django.urls import path ,include
from job.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',index,name="index"),
    path('admin_login',admin_login,name="admin_login"),
    path('user_login',user_login,name="user_login"),
    path('recruiter_login',recruiter_login,name="recruiter_login"),
    path('user_signup',user_signup,name="user_signup"),
    path('user_home',user_home,name="user_home"),
    path('Logout',Logout,name="Logout"),
    path('recruiter_signup',recruiter_signup,name="recruiter_signup"),
    path('admin_home',admin_home,name="admin_home"),
    path('view_users', view_users, name="view_users"),
    path('recruiter_pending', recruiter_pending, name="recruiter_pending"),
    path('recruiter_home', recruiter_home, name="recruiter_home"),
    path('delete_user/<int:pid>/', delete_user, name="delete_user"),
    path('delete_job/<int:pid>/', delete_job, name="delete_job"),
    path('change_status/<int:pid>/',change_status, name="change_status"),
    path('recruiter_accepted',recruiter_accepted, name="recruiter_accepted"),
    path('recruiter_rejected', recruiter_rejected, name="recruiter_rejected"),
    path('recruiter_all', recruiter_all, name="recruiter_all"),
    path('delete_recruiter/<int:pid>/', delete_recruiter, name="delete_recruiter"),
    path('change_passwordadmin', change_passwordadmin, name="change_passwordadmin"),
    path('change_passworduser', change_passworduser, name="change_passworduser"),
    path('change_passwordrecruiter', change_passwordrecruiter, name="change_passwordrecruiter"),
    path('job_list', job_list, name="job_list"),
    path('add_job', add_job, name="add_job"),
    path('latestjobs', latestjobs, name="latestjobs"),
    path('user_latestjobs', user_latestjobs, name="user_latestjobs"),
    path('faqs', faqs, name="faqs"),
    path('edit_job/<int:pid>/', edit_job, name="edit_job"),
    path('applyforjob/<int:pid>/', applyforjob, name="applyforjob"),
    path('job_detail/<int:pid>/', job_detail, name="job_detail"),

    path('appliedcandidates', appliedcandidates, name="appliedcandidates"),
    path('user_jobdetail/<int:pid>/', user_jobdetail, name="user_jobdetail"),

    path('change_companylogo/<int:pid>/', change_companylogo, name="change_companylogo"),
    path('search/', search_jobs, name='search_jobs'),
path('main_search/', main_search_jobs, name='main_search_jobs'),


    path('', include('job.urls')),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)