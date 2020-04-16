from django.shortcuts import render, redirect
from repository import models
from repository import forms

# Create your views here.
def workspace(request):
     user = is_auth(request)
     if(user == None):
          return redirect('signin')
     projects_count = models.ResearchProject.objects.filter(rp_of_company=user.company).count()
     
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
     return render(request, 'repository/research-list.html', {'researchproject_list': researchproject}) 

def researchview(request, pk):
     # ambil riset projek get(pk=pk)
     return render(request, 'repository/research-view.html') 

def researchedit(request):
     # research = ambil database
     # forms = forms.ResearchProjectForm()
     # forms.rp_desc.initial = research.pic
     # action = 'researchedit'
     return render(request, 'repository/research-edit.html') 

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