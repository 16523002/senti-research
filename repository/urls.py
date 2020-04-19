from django.urls import include, path, re_path
from repository import views

urlpatterns = [
    path('workspace/', views.workspace, name='workspace'), #this is the dashboard page
    path('profile/', views.profileview, name='profileview'), #this is to see the user's profile
    path('profile-edit/', views.profileedit, name='profileedit'), #this is to edit user's profile (FORM)
    path('workspace/research-brief/', views.researchbrief, name='researchbrief'), #this is the static page for research brief
    path('workspace/research-new/', views.researchnew, name='researchnew'),  #this is the form to create new research project (FORM)
    path('workspace/research-list/', views.researchlist, name='researchlist'), #this is the table to see the entire list of research projects
    path('workspace/research-view/', views.researchview, name='researchview'), #this is the page to see the details of certain research project
    path('workspace/research-edit/<str:pk>', views.researchedit, name='researchedit'), #this is the page to edit the research project (FORM)
    path('workspace/research-delete/<str:pk>', views.researchdelete, name='researchdelete'), #this is to delete research project
    path('workspace/respondent-new/', views.respondentnew, name='respondentnew'), #this is the form to create new research respondent (FORM)
    path('workspace/respondent-list/', views.respondentlist, name='respondentlist'), #this is the table to see the entire list of research respondents
    path('workspace/respondent-view/', views.respondentview, name='respondentview'), #this is the page to see the details of certain respondent
    path('workspace/respondent-edit/', views.respondentedit, name='respondentedit'), #this is the page to edit the research project (FORM)
    path('workspace/question-add/', views.questionadd, name='questionadd'),#this is the page to add questions to the project (FORM)
    path('workspace/question-edit/', views.questionedit, name='questionedit'), #this is the page to edit questions (FORM)
    path('workspace/calendar/', views.calendar, name='calendar'), #this is the calendar page
    path('logout/', views.logout, name='logout'), #logout
]