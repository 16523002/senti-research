from django.shortcuts import render

# Create your views here.
def workspace(request): 
    return render(request, 'repository/workspace.html') 

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


