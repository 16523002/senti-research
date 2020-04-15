from django.shortcuts import render, redirect
from repository import models
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
     return render(request, 'repository/research-new.html')

def researchlist(request):
     return render(request, 'repository/research-list.html') 

def researchview(request):
     return render(request, 'repository/research-view.html') 

def researchedit(request):
     return render(request, 'repository/research-edit.html') 

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


