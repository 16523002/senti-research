from django import forms
from landing.auth import AuthBackend


class RegisterForm(forms.Form):
    role_choices = [
        (0, 'Job Title'),
        (2,  'Project Manager/Owner'),
        (4,  'Researcher'),
    ]
 
    company_name = forms.CharField(label='Company Name', max_length=255, required=True)
    registerer_role = forms.ChoiceField(choices=role_choices, required=True, initial={'':'Job Title'})

    company_name.widget.attrs.update({'class': 'input-text', 'placeholder': 'Company Name'})

class UserSignUpForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=True, help_text = 'Required')
    last_name = forms.CharField(label='Last Name', max_length=100, required=True, help_text = 'Required')
    email = forms.EmailField(label='Email', required=True, help_text="Required, Inform a valid email address")
    password =  forms.CharField(label='Password', max_length=255, required=True, help_text = 'Required',  widget=forms.TextInput(attrs={'type':'password'}))
    

    first_name.widget.attrs.update({'class':'input-text', 'placeholder':'First Name'})
    last_name.widget.attrs.update({'class':'input-text', 'placeholder':'Last Name'})
    email.widget.attrs.update({'class':'input-text', 'placeholder':'Email'})
    password.widget.attrs.update({'class':'input-text', 'placeholder':'Create a Password'})

class UserSignInForm(forms.Form):
    email = forms.EmailField(label='Email', required=True, help_text="Required, Inform a valid email address")
    password = forms.CharField(label='Password', max_length=255, required=True, help_text = 'Required',  widget=forms.TextInput(attrs={'type':'password'}))

    email.widget.attrs.update({'class':'input-text', 'placeholder':'Your Email'})
    password.widget.attrs.update({'class':'input-text', 'placeholder':'Password'})

class JoinForm(forms.Form):
    role_choices = [
        (0, 'Job Title'),
        (1,  'Board of Directors'),
        (2,  'Project Manager/Owner'),
        (3,  'Engineer/Developer'),
        (4,  'Researcher'),
        (5,  'Designer'),
        (6,  'Finance Officer'),
        (7,  'Human Resource'),
        (8,  'QA/Tester')
    ]

    company_code = forms.CharField(label='Company Code', max_length=255, required=True)
    user_role = forms.ChoiceField(choices=role_choices, required=True, initial={'':'Job Title'})
    
    company_code.widget.attrs.update({'class': 'input-text', 'placeholder': 'Company Code'})
