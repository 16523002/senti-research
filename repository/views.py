from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from repository import models
from repository import forms
from datetime import datetime
from datetime import timedelta
from openpyxl import Workbook
from django.http import HttpResponse
import json


# Create your views here.
def workspace(request):
     user = is_auth(request)
     if(user == None):
          return redirect('signin')
     projects_count = models.ResearchProject.objects.filter(rp_of_company=user.company).count()
     # company = models.Company.objects.get(registerer_email=user.email)
     return render(request, 'repository/workspace.html', {'user': user, 'projects_count': projects_count}) 

def is_auth(request):
     id_user = request.session.get('authenticated_user_id', 0)
     if id_user == 0:
          print(id_user)
          return None 
     user = models.User.objects.get(pk=id_user)     
     return user

def logout(request):
     request.session.modified = True
     try:
          print(request.session['authenticated_user_id'])
          del request.session['authenticated_user_id']
     except KeyError:
          pass
     return redirect('signin')

def profileview(request): 
     user = is_auth(request)
     if(user == None):
          return redirect('signin')
     profile_view = models.User.objects.get(id=user.id)
     role = models.Role.objects.get(id=user.role_id)
     researchproject_list = models.ResearchProject.objects.filter(rp_pic=user.id)
     project_pic_count = models.ResearchProject.objects.filter(rp_pic=user.id).count()
     return render(request, 'repository/profile-view.html', {'profile_view': profile_view, 'researchproject_list': researchproject_list, 'role':role, 'project_pic_count':project_pic_count, 'user': user}) 
     # return render(request, 'repository/profile-view.html')

def profileedit(request):
     user = is_auth(request)
     if(user == None):
          return redirect('signin')
     return render(request, 'repository/profile-view.html', {'user':user})

def researchintro(request):
     user = is_auth(request)
     if(user == None):
          return redirect('signin')
     requests = models.Request.objects.filter(company=user.company)
     return render(request, 'repository/research-intro.html', {'requests':requests, 'user':user})

def researchbrief(request):
     user = is_auth(request)
     if(user == None):
          return redirect('signin')
     return render(request, 'repository/research-brief.html', {'user':user})

def researchnew(request):
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
          else :
               company_members = models.User.objects.filter(company=user.company)
               research_form = forms.ResearchProjectForm()
               return render(request, 'repository/research-new.html', {'researchproject_form': research_form, 'user': user, 'company_members':company_members})
     elif request.method == 'POST':
          research_form = forms.ResearchProjectForm(request.POST)
          if research_form.is_valid():
               rp_title = research_form.cleaned_data.get('rp_title')
               rp_desc = research_form.cleaned_data.get('rp_desc')
               rp_time_start = research_form.cleaned_data.get('rp_time_start')
               rp_time_end = research_form.cleaned_data.get('rp_time_end')
               rp_pic = research_form.cleaned_data.get('rp_pic')
               member_hidden = research_form.cleaned_data.get('member_hidden')
               selected_members_id = member_hidden.split(',')
               selected_members_id.pop()
               print(selected_members_id)
               try:
                    pic = models.User.objects.get(email=rp_pic)
                    company = user.company
                    research_project = models.ResearchProject(rp_title=rp_title, rp_desc=rp_desc, rp_time_start=rp_time_start, rp_time_end=rp_time_end)
                    research_project.rp_of_company = company
                    research_project.rp_created_by = user
                    research_project.rp_pic = pic
                    research_project.save()
                    for id_member in selected_members_id:
                         selected_user = models.User.objects.get(pk=id_member)
                         project_member = models.ProjectMember(user=selected_user, research_project=research_project)
                         project_member.save()
                    return redirect('researchlist')
               except models.User.DoesNotExist :
                    research_form = forms.ResearchProjectForm()
                    return render(request, 'repository/research-new.html', {'researchproject_form': research_form, 'user': user, 'message': 'User Email Does Not Exist'})

                    

def researchlist(request):
     user = is_auth(request)
     if(user == None):
          return redirect('signin')
     researchproject = models.ResearchProject.objects.filter(rp_of_company=user.company)
     return render(request, 'repository/research-list.html', {'researchproject_list': researchproject, 'user': user}) 

def researchview(request, pk):
     #  return render(request, 'repository/research-view.html')
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
          projectrespondent_form = forms.ProjectRespondentForm(initial={'rp_id':pk})
          researchproject = models.ResearchProject.objects.get(pk=pk)
          projectmember = models.ProjectMember.objects.filter(research_project_id=pk)
          question = models.ResearchQuestion.objects.filter(research_project_id=pk)
          projectrespondents = models.ProjectRespondent.objects.filter(research_project_id=pk)
          return render(request, 'repository/research-view.html', {'researchproject': researchproject, 'projectmember':projectmember, 'projectrespondent_form': projectrespondent_form, 'user': user, 'question_list': question, 'projectrespondents':projectrespondents})     
     elif request.method == 'POST':
          print("Hello")
          projectrespondent_form = forms.ProjectRespondentForm(request.POST)
          if projectrespondent_form.is_valid():
               print("Valid")
               rp_respondent = projectrespondent_form.cleaned_data.get('rp_respondent')
               rp_id = projectrespondent_form.cleaned_data.get("rp_id")
               try:
                    research_project = models.ResearchProject.objects.get(pk=rp_id)
                    respondent = models.ResearchRespondent.objects.get(rr_name=rp_respondent)
                    project_respondent = models.ProjectRespondent(respondent=respondent, research_project=research_project)
                    project_respondent.save()
               except models.ResearchRespondent.DoesNotExist :
                    if(user == None):
                         return redirect('signin')
                    projectrespondent_form = forms.ProjectRespondentForm()
                    researchproject = models.ResearchProject.objects.get(pk=pk)
                    question = models.ResearchQuestion.objects.filter(research_project_id=pk)
                    projectrespondents = models.ProjectRespondent.objects.filter(research_project_id=pk)
                    return render(request, 'repository/research-view.html', {'researchproject': researchproject, 'projectrespondent_form': projectrespondent_form, 'user': user, 'question_list': question, 'projectrespondents':projectrespondents, 'message':'Respondent Not found'})     
     return redirect('researchview', pk)

def researchedit(request, pk):
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
          else :
               member_hidden = ''
               company_members = models.User.objects.filter(company=user.company)
               researchproject = models.ResearchProject.objects.get(pk=pk)
               projectmembers = models.ProjectMember.objects.filter(research_project=researchproject)
               selectedUsers = []
               for projectmember in projectmembers:
                    # print(projectmember.user.id)
                    selectedUsers.append(projectmember.user)
                    member_hidden = member_hidden + str(projectmember.user.id) + ','
               print(member_hidden)
               research_form = forms.ResearchProjectForm(initial={
                    'rp_title': researchproject.rp_title,
                    'rp_desc' : researchproject.rp_desc,
                    'rp_time_start' : researchproject.rp_time_start,
                    'rp_time_end' : researchproject.rp_time_end,
                    'rp_pic' : user.email,
                    'member_hidden': member_hidden  })
               return render(request, 'repository/research-edit.html', {'researchproject_form': research_form, 'user': user, 'company_members':company_members, 'selected_users': selectedUsers, 'researchproject':researchproject})
     elif request.method == 'POST':
          rp_form = forms.ResearchProjectForm(request.POST)
          if rp_form.is_valid():
               rp_title = rp_form.cleaned_data.get('rp_title')
               rp_desc = rp_form.cleaned_data.get('rp_desc')
               rp_time_start = rp_form.cleaned_data.get('rp_time_start')
               rp_time_end = rp_form.cleaned_data.get('rp_time_end')
               rp_pic = rp_form.cleaned_data.get('rp_pic')
               member_hidden = rp_form.cleaned_data.get('member_hidden')
               selected_members_id = member_hidden.split(',')
               selected_members_id.pop()
               try:
                    researchproject = models.ResearchProject.objects.get(pk=pk)
                    pic = models.User.objects.get(email=rp_pic)
                    company = user.company
                    researchproject.rp_of_company = company
                    researchproject.rp_created_by = user
                    researchproject.rp_pic = pic
                    researchproject.rp_title = rp_title 
                    researchproject.rp_desc = rp_desc 
                    researchproject.rp_time_start = rp_time_start
                    researchproject.rp_time_end = rp_time_end
                    researchproject.rp_pic = pic
                    researchproject.save()
                    models.ProjectMember.objects.filter(research_project=researchproject).delete()
                    for id_member in selected_members_id:
                         selected_user = models.User.objects.get(pk=id_member)
                         project_member = models.ProjectMember(user=selected_user, research_project=researchproject)
                         project_member.save()
                    return redirect('researchlist')
               except models.User.DoesNotExist :
                    rp_form = forms.ResearchProjectForm()
                    return render(request, 'repository/research-edit.html', {'researchproject_form': rp_form, 'user': user, 'message': 'User Email Does Not Exist'})


def researchdelete(request, pk):
     research = models.ResearchProject.objects.get(pk=pk)
     if research != None:
          research.delete()
     return redirect('researchlist')

def respondentnew(request):
     # return render(request, 'repository/respondent-new.html')
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
          else :
               respondent_form = forms.RespondentForm()
               return render(request, 'repository/respondent-new.html', {'respondent_form': respondent_form, 'user': user})
     elif request.method == 'POST':
          respondent_form = forms.RespondentForm(request.POST)
          if respondent_form.is_valid():
               rr_name = respondent_form.cleaned_data.get('rr_name')
               rr_phone = respondent_form.cleaned_data.get('rr_phone')
               rr_email = respondent_form.cleaned_data.get('rr_email')
               rr_occupation = respondent_form.cleaned_data.get('rr_occupation')
               rr_gender = respondent_form.cleaned_data.get('rr_gender')
               rr_birth = respondent_form.cleaned_data.get('rr_birth')
               try:
                    company = user.company
                    research_respondent = models.ResearchRespondent(rr_name=rr_name, rr_phone=rr_phone,rr_email=rr_email, rr_occupation=rr_occupation, rr_gender=rr_gender, rr_birth=rr_birth)
                    research_respondent.rr_of_company = company
                    research_respondent.save() 
                    return redirect('respondentlist')
               except models.User.DoesNotExist :
                    respondent_form = forms.RespondentForm()
                    return render(request, 'repository/respondent-new.html', {'respondent_form': respondent_form, 'user': user})

def respondentlist(request):
     user = is_auth(request)
     if(user == None):
          return redirect('signin')
     respondent = models.ResearchRespondent.objects.filter(rr_of_company=user.company)
     return render(request, 'repository/respondent-list.html', {'respondent_list': respondent, 'user': user}) 

def respondentview(request, pk):
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
     respondent = models.ResearchRespondent.objects.get(pk=pk)
     return render(request, 'repository/respondent-view.html', {'respondent': respondent, 'user': user})

def respondentedit(request, pk):
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
          else :
               respondent = models.ResearchRespondent.objects.get(pk=pk)
               respondent_form = forms.RespondentForm(initial={
                    'rr_name': respondent.rr_name,
                    'rr_phone' : respondent.rr_phone,
                    'rr_email' : respondent.rr_email,
                    'rr_occupation' : respondent.rr_occupation,
                    'rr_gender' : respondent.rr_gender,
                    'rr_birth' : respondent.rr_birth })
               return render(request, 'repository/respondent-edit.html', {'respondent_form': respondent_form, 'respondent':respondent})
     elif request.method == 'POST':
          rr_form = forms.RespondentForm(request.POST)
          if rr_form.is_valid():
               rr_name = rr_form.cleaned_data.get('rr_name')
               rr_phone = rr_form.cleaned_data.get('rr_phone')
               rr_email = rr_form.cleaned_data.get('rr_email')
               rr_occupation = rr_form.cleaned_data.get('rr_occupation')
               rr_gender = rr_form.cleaned_data.get('rr_gender')
               rr_birth = rr_form.cleaned_data.get('rr_birth')
               try:
                    respondent = models.ResearchRespondent.objects.get(pk=pk)
                    company = user.company
                    respondent.rr_name = rr_name
                    respondent.rr_phone = rr_phone
                    respondent.rr_email = rr_email
                    respondent.rr_occupation = rr_occupation
                    respondent.rr_gender = rr_gender
                    respondent.rr_birth = rr_birth
                    respondent.save() 
                    return redirect('respondentlist')
               except models.User.DoesNotExist :
                    respondent_form = forms.RespondentForm()
                    return render(request, 'repository/respondent-edit.html', {'respondent_form': rr_form, 'user': user})

def respondentdelete(request, pk):
     respondent = models.ResearchRespondent.objects.get(pk=pk)
     if respondent != None:
          respondent.delete()
     return redirect('respondentlist')

def questionadd(request, pk):
     # return render(request, 'repository/question-add.html')
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
          else :
               question_form = forms.QuestionForm()
               research_project = models.ResearchProject.objects.get(pk=pk)
               return render(request, 'repository/question-add.html', {'question_form': question_form, 'user': user, 'research_project':research_project})
     elif request.method == 'POST':
          question_form = forms.QuestionForm(request.POST)
          if question_form.is_valid():
               question = question_form.cleaned_data.get('question')
               question_list = question.split(';;')
               question_list.pop()
               print(question_list)         
               try:
                    researchproject =  models.ResearchProject.objects.get(pk=pk)
                    for researchquestion in question_list:
                         project_question = models.ResearchQuestion(question=researchquestion, research_project=researchproject)
                         project_question.save()
                    return redirect('researchview', pk)
               except models.ResearchProject.DoesNotExist :
                    question_form = forms.RespondentForm()
                    return render(request, 'repository/question-add.html', {'question_form': question_form, 'researchproject': researchproject})

def questiondelete(request, pk):
     question = models.ResearchQuestion.objects.get(pk=pk)
     if question != None:
          question.delete()
     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def rprespondentdelete(request, pk):
     projectrespondent = models.ProjectRespondent.objects.get(pk=pk)
     if projectrespondent != None:
          projectrespondent.delete()
     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def answeradd(request, pk, respondent):
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
          else :
               answer_form = forms.AnswerForm()
               research_project = models.ResearchProject.objects.get(pk=pk)
               questions = models.ResearchQuestion.objects.filter(research_project=pk)
               return render(request, 'repository/answer-add.html', {'answer_form':answer_form, 'user': user, 'research_project':research_project, 'questions':questions})
     elif request.method == 'POST':
          answer_form = forms.AnswerForm(request.POST)
          if answer_form.is_valid():
               answer = answer_form.cleaned_data.get('answer_hidden')
               decodedAnswers = json.JSONDecoder().decode(answer)
               #print(type(decodedAnswers))
               for answer in decodedAnswers:
                    question_id = next(iter(answer))
                    value = answer[question_id]
                    research_project = models.ResearchProject.objects.get(pk=pk)
                    research_respondent = models.ResearchRespondent.objects.get(pk=respondent)
                    question = models.ResearchQuestion.objects.get(pk=int(question_id))
                    saved_answer = models.ResearchAnswer(research_question=question, answer=value, research_respondent=research_respondent, research_project=research_project)
                    saved_answer.save()
               return redirect('researchview', pk)          
     return render(request, 'repository/answer-add.html') 

def answerview(request, pk, respondent):
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
     research_project = models.ResearchProject.objects.get(pk=pk)
     research_respondent = models.ResearchRespondent.objects.get(pk=respondent)
     questions = models.ResearchQuestion.objects.filter(research_project=pk)
     answers = models.ResearchAnswer.objects.filter(research_respondent=research_respondent, research_project=pk)
     return render(request, 'repository/answer-view.html', {'research_project':research_project, 'research_respondent': research_respondent, 'questions': questions, 'answers':answers, 'user':user})

def requestjoin(request):
     user = is_auth(request)
     if(user == None):
          return redirect('signin')
     company = models.Company.objects.get(id=user.company_id)
     requests = models.Request.objects.filter(company_id=company.id)
     return render(request, 'repository/requestjoin-list.html', {'company':company, 'requests':requests, 'user':user})

def workspacedetail(request):
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
     company = models.Company.objects.get(id=user.company_id)
     users = models.User.objects.filter(company_id=company.id)
     roles = models.Role.objects.filter(id=user.role_id)
     return render(request, 'repository/workspace-view.html', {'company':company, 'users':users, 'roles':roles, 'user':user}) 

def calendar(request):
     return render(request, 'repository/calendar.html') 