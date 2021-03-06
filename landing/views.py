from django.shortcuts import render, redirect
from landing.auth import AuthBackend, hashing_password
from landing.forms import UserSignInForm, UserSignUpForm, RegisterForm, JoinForm
from repository.models import User, Company, Request, Role
from django.contrib.auth.hashers import make_password
from django.core import serializers
from repository.views import is_auth
import uuid 


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
			request.session['authenticated_user_id'] = auth.id
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
	user = is_auth(request)
	if request.method == 'GET':
		if(user == None):
			return redirect('signin')
		else :
			forms = RegisterForm()
			return render(request, 'landing/auth-register.html', {'register_form': forms, 'user': user})
	elif request.method == 'POST':
		print("Hello")
		form = RegisterForm(request.POST)
		if form.is_valid():
			registerer_name = user.user_first_name + ' ' + user.user_last_name
			registerer_email = user.email
			company_name = form.cleaned_data.get('company_name')
			registerer_role = form.cleaned_data.get('registerer_role')
			company_code = uuid.uuid4().hex[:6].upper()
			
			company = Company(registerer_name=registerer_name, registerer_email=registerer_email, company_name=company_name, company_code=company_code)
			company.save()
			registerer_role_object = Role.objects.get(pk=registerer_role)
			user.role = registerer_role_object
			user.company = company
			user.save()
			return redirect('workspace')
		else:
			return redirect('register')

def join(request):
	user = is_auth(request)
	if request.method == 'GET':
		if(user == None):
			return redirect('signin')
		else :
			forms = JoinForm()
			return render(request, 'landing/auth-join.html', {'join_form': forms, 'user': user})
	elif request.method == 'POST':
		form = JoinForm(request.POST)
		if form.is_valid():
			user_role = form.cleaned_data.get('user_role')
			company_code = form.cleaned_data.get('company_code')
			company = Company.objects.get(company_code=company_code)
			if(company == None):
				forms = JoinForm()
				return render(request, 'landing/auth-join.html', {'join_form': forms, 'message': 'Company code does not match'})
			role = Role.objects.get(pk=user_role)
			request = Request(company=company, requester=user, request_role=role)
			request.save()
		return redirect('workspace')

	