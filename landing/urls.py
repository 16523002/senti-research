from django.urls import include, path, re_path
from landing import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'), 
    path('company-register/', views.register, name='register'), #This is to register/create new company's workspace
    path('company-join/', views.join, name='join'), #This is to join certain company's workspace
    
]