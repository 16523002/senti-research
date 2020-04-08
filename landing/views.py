from django.shortcuts import render, redirect
from landing.auth import AuthBackend, hashing_password
from landing.forms import RegisterForm, UserSignUpForm, UserSignInForm
from repository.models import Company, User
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
	return render(request, 'landing/landing-page.html')

def signin(request):
	if request.method == 'GET':
		forms = UserSignInForm()
		return render(request, 'landing/auth-signin.html', {'usersignin_form': forms})
	elif request.method == 'POST':
		form = UserSignInForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			auth = AuthBackend().authenticate(request, email=email, password=password)
			if auth == None:
				print("FAILED SIGN IN")
				return redirect('signin')
			return redirect('workspace')
	return redirect('signin')

def signup(request):
	if request.method == 'GET':
		forms = UserSignUpForm()
		return render(request, 'landing/auth-signup.html', {'usersignup_form': forms})
	elif request.method == 'POST':
		form = UserSignUpForm(request.POST)
		if form.is_valid():	
			user_first_name = form.cleaned_data.get('first_name')
			user_last_name = form.cleaned_data.get('last_name')	
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			try:
				user = User.objects.get(email=email)
				forms = UserSignUpForm()
				return render(request, 'landing/auth-signup.html', {'usersignup_form': forms, 'message': 'Your email has been used'})
			except User.DoesNotExist:
				password = hashing_password(password)
				user = User(user_first_name=user_first_name, user_last_name=user_last_name, email=email, password=password)
				user.save()
				return redirect('signin')
		else:
			return redirect('signup')
			

def register(request):
	if request.method == 'GET':
		forms = RegisterForm()
		return render(request, 'landing/auth-register.html', {'register_form': forms})
	elif request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			registerer_name = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
			registerer_email = form.cleaned_data.get('email')
			company_name = form.cleaned_data.get('company_name')
			registerer_role = form.cleaned_data.get('registerer_role')
			company_domain = form.cleaned_data.get('company_domain')
			
			company = Company(registerer_name=registerer_name, registerer_email=registerer_email, company_name=company_name, registerer_role=registerer_role, company_domain=company_domain)
			company.save()
			return redirect('index')
			 

	