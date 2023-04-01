from django.urls import re_path
from views import resume_detail, resume_list
from django.shortcuts import render
urlpatterns = [
    
    re_path(r'^resumes/$',resume_list,none,'first commit'),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', render(resume_detail)),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/basic/', views.basic_detail),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/profiles/', views.profile_list),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/work/', views.work_list),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/volunteer/', views.volunteer_list),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/education/', views.education_list),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/awards/', views.awards_list),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/publications/', views.publications_list),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/skills/', views.skills_list),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/languages/', views.languages_list),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/interests/', views.interests_list),
    # re_path(r'^resumes/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/references/', views.references_list),
]
