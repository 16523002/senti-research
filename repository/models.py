from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    registerer_name = models.CharField(max_length=255)
    registerer_email = models.EmailField()
    company_domain = models.CharField(max_length=255)
    status_domain = models.BooleanField(default=False)
    # company_registered_at = models.DateField('registered at')

    def __str__(self):
        activate_status =  'Activated' if self.status_domain == True else 'Not Activated' 
        return self.company_name + ' (Company Domain: ' + activate_status + ')'

class Role(models.Model):
    role_title = models.CharField(max_length=50)

class User(models.Model):
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    photo = models.ImageField(null=True)
    google_id = models.CharField(max_length=255, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

class Request(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class ResearchProject(models.Model):
    rp_title = models.CharField(max_length=255)
    rp_desc = models.TextField()
    rp_time_start = models.DateField()
    rp_time_end = models.DateField()
    rp_created_at = models.DateField('created at', auto_now_add=True)
    rp_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rp_updated_at = models.DateTimeField(auto_now=True)
    rp_of_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
class ProjectMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    research_project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)    
    
class ResearchRespondent(models.Model):
    male = 'M'
    female = 'F'
    gender = (
        (male, 'Male'),
        (female, 'Female'),
    )
    rr_name = models.CharField(max_length=255)
    rr_bod = models.DateField(null=True)
    rr_phone = models.CharField(max_length=50)
    rr_email = models.EmailField(null=True)
    rr_occupation = models.CharField(max_length=255)
    rr_gender = models.CharField(
        max_length=2,
        choices=gender
    )
    rr_registered_at = models.DateField('registered at', auto_now_add=True)
    rr_updated_at = models.DateTimeField(auto_now=True)
    research_project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)
    

class ResearchQuestions(models.Model):
    question = models.TextField()
    research_project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)

class ResearchAnswer(models.Model):
    answer = models.TextField()
    research_question = models.OneToOneField(ResearchQuestions, on_delete=models.CASCADE)
    research_respondent = models.OneToOneField(ResearchRespondent, on_delete=models.CASCADE)
        

