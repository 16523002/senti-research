from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    registerer_name = models.CharField(max_length=255)
    registerer_email = models.EmailField()
    company_code = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    company_registered_at = models.DateField('registered at', auto_now_add=True)

    def __str__(self):
        return self.company_name 

class Role(models.Model):
    role_title = models.CharField(max_length=50)

class User(models.Model):
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = "repository/assets/images/", null=True)
    google_id = models.CharField(max_length=255, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    user_registered_at = models.DateField('registered at', auto_now_add=True)
    user_updated_at = models.DateTimeField(auto_now=True)


class Request(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    activate_status = models.BooleanField(default=False)
    request_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)


class ResearchProject(models.Model):
    rp_title = models.CharField(max_length=255)
    rp_desc = models.TextField()
    rp_time_start = models.DateField()
    rp_time_end = models.DateField()
    rp_created_at = models.DateField('created at', auto_now_add=True)
    rp_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rp_updated_at = models.DateTimeField(auto_now=True)
    rp_of_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    rp_pic = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='PIC')
    
class ProjectMember(models.Model):
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
    rr_birth = models.DateField(null=True)
    rr_phone = models.CharField(max_length=50)
    rr_email = models.EmailField(null=True)
    rr_occupation = models.CharField(max_length=255)
    rr_gender = models.CharField(
        max_length=2,
        choices=gender
    )
    rr_of_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    rr_registered_at = models.DateField('registered at', auto_now_add=True)
    rr_updated_at = models.DateTimeField(auto_now=True)
    research_project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE, null=True)

class ProjectRespondent(models.Model):
    respondent = models.ForeignKey(ResearchRespondent, on_delete=models.CASCADE)
    research_project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)

class ResearchQuestion(models.Model):
    question = models.TextField()
    research_project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)

class ResearchAnswer(models.Model):
    answer = models.TextField()
    research_question = models.OneToOneField(ResearchQuestion, on_delete=models.CASCADE)
    research_respondent = models.OneToOneField(ResearchRespondent, on_delete=models.CASCADE)
        

