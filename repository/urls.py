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
    path('workspace/research-view/<str:pk>', views.researchview, name='researchview'), #TABLE:  this is the page to see the details of certain research project
    path('workspace/research-edit/<str:pk>', views.researchedit, name='researchedit'), #FORM:  this is the page to edit the research project 
    path('workspace/research-delete/<str:pk>', views.researchdelete, name='researchdelete'), #this is to delete research project
    path('workspace/respondent-new/', views.respondentnew, name='respondentnew'), #FORM:  this is the form to create new research respondent
    path('workspace/respondent-list/', views.respondentlist, name='respondentlist'), #TABLE:  this is the table to see the entire list of research respondents
    path('workspace/respondent-view/<str:pk>', views.respondentview, name='respondentview'), #TABLE:  this is the page to see the details of certain respondent
    path('workspace/respondent-edit/<str:pk>', views.respondentedit, name='respondentedit'), #FORM: this is the page to edit the research project
    path('workspace/respondent-delete/<str:pk>', views.respondentdelete, name='respondentdelete'), #this is to delete respondent
    path('workspace/projectrespondent-delete/<str:pk>', views.rprespondentdelete, name='rprespondentdelete'),
    path('workspace/question-add/<str:pk>', views.questionadd, name='questionadd'),#FORM: this is the page to add questions to the project
    path('workspace/question-delete/<str:pk>', views.questiondelete, name='questiondelete'), #FORM: this is the delete to edit questions
    path('workspace/calendar/', views.calendar, name='calendar'), #this is the calendar page
    path('logout/', views.logout, name='logout'), #logout
]