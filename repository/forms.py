from django import forms
from django.forms import ModelForm, formset_factory, modelformset_factory
from repository import models
import datetime

# class ResearchProjectForm(ModelForm):
#     class Meta:
#         model = ResearchProject
#         fields = '__all__'

class DatePicker(forms.DateInput):
    input_type = 'date'


class ResearchProjectForm(forms.Form):
    rp_title = forms.CharField(label='Title', max_length=255, required=True, help_text='Required')
    rp_desc = forms.CharField(label='Description', required=True, help_text='Required', widget=forms.Textarea)
    rp_time_start = forms.DateField(label='Date Start', required=True, help_text='Required', widget=DatePicker())
    rp_time_end = forms.DateField(label='Date End', required=True, help_text='Required', widget=DatePicker())
    rp_pic = forms.EmailField(label='PIC Email', required=True, help_text='Required')
    member_hidden = forms.CharField(required=True, widget=forms.HiddenInput)
    # rp_member = forms.EmailField(label='Member Email', required=True, help_text='Required')
    
    rp_title.widget.attrs.update({'class': 'form-control', 'placeholder': 'Name Your Research Project'})
    rp_desc.widget.attrs.update({'class':'form-control', 'placeholder':'Decribe Your Research Project' })
    rp_time_start.widget.attrs.update({'class': 'form-control', 'type': 'date'})
    rp_time_end.widget.attrs.update({'class': 'form-control', 'type': 'date'})
    rp_pic.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter PIC\'s Email'})
    member_hidden.widget.attrs.update({'id':'member-hidden'})
    # rp_member.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Member\'s Email'})

class RespondentForm(forms.Form):
    gender_choices = [
        ('', 'Gender'),
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    rr_name = forms.CharField(label='Name', max_length=255, required=True, help_text='Required')
    rr_phone = forms.CharField(label='Phone', max_length=50, required=True, help_text='Required')
    rr_email = forms.CharField(label='Email')
    rr_occupation = forms.CharField(label='Occupation', max_length=255, required=True, help_text='Required')
    rr_gender = forms.ChoiceField(choices=gender_choices, required=True, initial={'':'Gender'})
    rr_birth = forms.DateField(label='Birth', required=True, help_text='Required', widget=DatePicker())

    rr_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Respondent\'s Name'})
    rr_phone.widget.attrs.update({'class': 'form-control', 'placeholder': 'Respondent\'s Phone Number'})
    rr_email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Respondent\'s Email'})
    rr_occupation.widget.attrs.update({'class': 'form-control', 'placeholder': 'Respondent\'s Occupation'})
    rr_birth.widget.attrs.update({'class': 'form-control', 'type': 'date'})

class QuestionForm(forms.Form):
    question = forms.CharField(required=True, widget=forms.HiddenInput)

    question.widget.attrs.update({'id':'question-hidden'})

class AnswerForm(forms.Form):
    answer_hidden = forms.CharField(required=True, widget=forms.HiddenInput)
    # question = forms.CharField(required=True, widget=forms.HiddenInput)

    answer_hidden.widget.attrs.update({'type':'hidden'})
    # question.widget.attrs.update({'type':'hidden'})

class ProjectRespondentForm(forms.Form):
    rp_respondent = forms.CharField(label='Respondent', max_length=255, required=True, help_text='Required')
    rp_id = forms.CharField(required=True, widget=forms.HiddenInput)

    rp_respondent.widget.attrs.update({'class': 'form-control', 'placeholder': 'Respondent\'s Name'})
    rp_id.widget.attrs.update({'type':'hidden'})
