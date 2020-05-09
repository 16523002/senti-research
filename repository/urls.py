from django.urls import include, path, re_path
from repository import views

urlpatterns = [
    path('workspace/', views.workspace, name='workspace'), #this is the dashboard page
    path('profile/', views.profileview, name='profileview'), #this is to see the user's profile
    path('profile-edit/', views.profileedit, name='profileedit'), #FORM:  this is to edit user's profile 
    path('request-join/', views.requestjoin, name='requestjoin'), #TABLE:  this is to see and activicate user's company joining request 
    path('workspace/research-brief/', views.researchbrief, name='researchbrief'), #this is the static page for research brief
    path('workspace/research-new/', views.researchnew, name='researchnew'),  #FORM:  this is the form to create new research project
    path('workspace/research-list/', views.researchlist, name='researchlist'), #TABLE:  this is the table to see the entire list of research projects
    path('workspace/<str:pk>/research-view/', views.researchview, name='researchview'), #TABLE:  this is the page to see the details of certain research project
    path('workspace/<str:pk>/research-edit/', views.researchedit, name='researchedit'), #FORM:  this is the page to edit the research project 
    path('workspace/<str:pk>/research-delete/', views.researchdelete, name='researchdelete'), #this is to delete research project
    path('workspace/respondent-new/', views.respondentnew, name='respondentnew'), #FORM:  this is the form to create new research respondent
    path('workspace/respondent-list/', views.respondentlist, name='respondentlist'), #TABLE:  this is the table to see the entire list of research respondents
    path('workspace/<str:pk>/respondent-view/', views.respondentview, name='respondentview'), #TABLE:  this is the page to see the details of certain respondent
    path('workspace/<str:pk>/respondent-edit/', views.respondentedit, name='respondentedit'), #FORM: this is the page to edit the research project
    path('workspace/<str:pk>/respondent-delete/', views.respondentdelete, name='respondentdelete'), #this is to delete respondent
    path('workspace/<str:pk>/projectrespondent-delete/', views.rprespondentdelete, name='rprespondentdelete'),
    path('workspace/<str:pk>/question-add/', views.questionadd, name='questionadd'),#FORM: this is the page to add questions to the project
    path('workspace/<str:pk>/question-delete/', views.questiondelete, name='questiondelete'), #FORM: this is the delete to edit questions
    path('workspace/<str:pk>/<str:respondent>/answer-add/', views.answeradd, name='answeradd'),
    path('workspace/<str:pk>/<str:respondent>/answer-view/', views.answerview, name='answerview'),
    path('workspace/detail/', views.workspacedetail, name='workspacedetail'),
    path('converttoexcel/<str:pk>', views.converttoexcel, name='converttoexcel'), 
    path('workspace/calendar/', views.calendar, name='calendar'), #this is the calendar page
    path('logout/', views.logout, name='logout'), #logout
]