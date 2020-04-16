from django import forms
import datetime


class DatePicker(forms.DateInput):
    input_type = 'date'


class ResearchProjectForm(forms.Form):
    rp_title = forms.CharField(label='Title', max_length=255, required=True, help_text='Required')
    rp_desc = forms.CharField(label='Description', required=True, help_text='Required', widget=forms.Textarea)
    rp_time_start = forms.DateField(label='Date Start', required=True, help_text='Required', widget=DatePicker())
    rp_time_end = forms.DateField(label='Date End', required=True, help_text='Required', widget=DatePicker())
    rp_pic = forms.EmailField(label='PIC Email', required=True, help_text='Required')

    
    rp_title.widget.attrs.update({'class': 'form-control', 'placeholder': 'Name Your Research Project'})
    rp_desc.widget.attrs.update({'class':'form-control', 'placeholder':'Decribe Your Research Project' })
    rp_time_start.widget.attrs.update({'class': 'form-control', 'type': 'date'})
    rp_time_end.widget.attrs.update({'class': 'form-control', 'type': 'date'})
    rp_pic.widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter PIC\'s Email'})

    # first_name.widget.attrs.update({'class':'input-text', 'placeholder':'First Name'})
    # last_name.widget.attrs.update({'class':'input-text', 'placeholder':'Last Name'})
    # email.widget.attrs.update({'class':'input-text', 'placeholder':'Email'})
    # password.widget.attrs.update({'class':'input-text', 'placeholder':'Create a Password'})