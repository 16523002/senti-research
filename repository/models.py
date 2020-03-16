from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    registerer_name = models.CharField(max_length=255)
    registerer_email = models.EmailField()
    registerer_role = models.CharField(max_length=100)
    company_domain = models.CharField(max_length=255)

class Role(models.Model):
    role_title = models.CharField(max_length=50)

class Employee(models.Model):
    employee_first_name = models.CharField(max_length=100)
    employee_last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    photo = models.ImageField()
    google_id = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)


class ResearchProject(models.Model):
    rp_title = models.CharField(max_length=255)
    rp_desc = models.TextField()
    rp_time_start = models.DateField()
    rp_time_end = models.DateField()
    rp_created_at = models.DateField('created at')
    rp_created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    
    
class ResearchRespondent(models.Model):
    male = 'M'
    female = 'F'
    gender = (
        (male, 'Male'),
        (female, 'Female'),
    )
    rr_name = models.CharField(max_length=255)
    rr_phone = models.CharField(max_length=50)
    rr_email = models.EmailField(null=True)
    rr_occupation = models.CharField(max_length=255)
    rr_gender = models.CharField(
        max_length=2,
        choices=gender
    )
    research_project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)
    

class ResearchQuestions(models.Model):
    question = models.TextField()
    research_project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)

class ResearchAnswer(models.Model):
    answer = models.TextField()
    research_question = models.OneToOneField(ResearchQuestions, on_delete=models.CASCADE)
    research_respondent = models.OneToOneField(ResearchRespondent, on_delete=models.CASCADE)
        

