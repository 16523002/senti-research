from django import forms
from landing.auth import AuthBackend

class RegisterForm(forms.Form):
    role_choices = [
        ('', 'Job Title'),
        ('bod',  'Board of Directors'),
        ('projectmanager',  'Project Manager/Owner'),
        ('engineer',  'Engineer/Developer'),
        ('researcher',  'Researcher'),
        ('designer',  'Designer'),
        ('financeofficer',  'Finance Officer'),
        ('humanresource',  'Human Resource'),
        ('qatester',  'QA/Tester')
    ]

    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    company_name = forms.CharField(label='Company Name', max_length=255, required=True)
    # registerer_role = forms.CharField(label='Role', max_length=100, required=True)
    registerer_role = forms.ChoiceField(choices=role_choices, required=True, initial={'':'Job Title'})
    company_domain = forms.CharField(label='Company Domain', max_length=255, required=True)

    first_name.widget.attrs.update({'class': 'input-text', 'placeholder': 'First Name'})
    last_name.widget.attrs.update({'class': 'input-text', 'placeholder': 'Last Name'})
    email.widget.attrs.update({'class': 'input-text', 'placeholder': 'Business Email'})
    company_name.widget.attrs.update({'class': 'input-text', 'placeholder': 'Company Name'})
    company_domain.widget.attrs.update({'class': 'input-text', 'placeholder': 'Company Domain'})

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
