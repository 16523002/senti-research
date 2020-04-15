from django.urls import include, path, re_path
from landing import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'), #This is for the regular/personal user
    path('register/', views.register, name='register'), #This is for the enterprise/company user employee
    
]