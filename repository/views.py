from django.shortcuts import render, redirect
from repository import models
from repository import forms

# Create your views here.
def workspace(request):
     user = is_auth(request)
     if(user == None):
          return redirect('signin')
     projects_count = models.ResearchProject.objects.filter(rp_of_company=user.company).count()
     company = models.Company.objects.get(registerer_email=user.email)
     return render(request, 'repository/workspace.html', {'user': user, 'projects_count': projects_count, 'company':company}) 

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
     return render(request, 'repository/profile-view.html')


def researchbrief(request):
     return render(request, 'repository/research-brief.html')

def researchnew(request):
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
          else :
               research_form = forms.ResearchProjectForm()
               return render(request, 'repository/research-new.html', {'researchproject_form': research_form, 'user': user})
     elif request.method == 'POST':
          research_form = forms.ResearchProjectForm(request.POST)
          if research_form.is_valid():
               rp_title = research_form.cleaned_data.get('rp_title')
               rp_desc = research_form.cleaned_data.get('rp_desc')
               rp_time_start = research_form.cleaned_data.get('rp_time_start')
               rp_time_end = research_form.cleaned_data.get('rp_time_end')
               rp_pic = research_form.cleaned_data.get('rp_pic')
               try:
                    pic = models.User.objects.get(email=rp_pic)
                    company = user.company
                    research_project = models.ResearchProject(rp_title=rp_title, rp_desc=rp_desc, rp_time_start=rp_time_start, rp_time_end=rp_time_end)
                    research_project.rp_of_company = company
                    research_project.rp_created_by = user
                    research_project.rp_pic = pic
                    research_project.save()
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

def researchview(request):
     # ambil riset projek get(pk=pk)
     return render(request, 'repository/research-view.html') 

def researchedit(request, pk):
     user = is_auth(request)
     if request.method == 'GET':
          if(user == None):
               return redirect('signin')
          else :
               researchproject = models.ResearchProject.objects.get(pk=pk)
               research_form = forms.ResearchProjectForm(initial={
                    'rp_title': researchproject.rp_title,
                    'rp_desc' : researchproject.rp_desc,
                    'rp_time_start' : researchproject.rp_time_start,
                    'rp_time_end' : researchproject.rp_time_end,
                    'rp_pic' : researchproject.rp_pic })
               return render(request, 'repository/research-edit.html', {'researchproject_form': research_form, 'user': user})
     elif request.method == 'POST':
          rp_form = forms.ResearchProjectForm(request.POST)
          if rp_form.is_valid():
               rp_title = rp_form.cleaned_data.get('rp_title')
               rp_desc = rp_form.cleaned_data.get('rp_desc')
               rp_time_start = rp_form.cleaned_data.get('rp_time_start')
               rp_time_end = rp_form.cleaned_data.get('rp_time_end')
               rp_pic = rp_form.cleaned_data.get('rp_pic')
               try:
                    researchproject = models.ResearchProject.objects.get(pk=pk)
                    pic = models.User.objects.get(email=rp_pic)
                    company = user.company
                    researchproject.rp_of_company = company
                    researchproject.rp_created_by = user
                    researchproject.rp_title = rp_title 
                    researchproject.rp_desc = rp_desc 
                    researchproject.rp_time_start = rp_time_start
                    researchproject.rp_time_end = rp_time_end
                    researchproject.rp_pic = rp_pic
                    researchproject.save()
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
     return render(request, 'repository/respondent-new.html') 

def respondentlist(request):
     return render(request, 'repository/respondent-list.html') 

def respondentview(request):
     return render(request, 'repository/respondent-view.html') 

def respondentedit(request):
     return render(request, 'repository/research-edit.html') 

def questionadd(request):
    return render(request, 'respository/question-add.html') 

def questionedit(request):
    return render(request, 'respository/question-edit.html') 

def calendar(request):
    return render(request, 'respository/calendar.html') 