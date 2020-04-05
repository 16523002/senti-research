from django.urls import include, path, re_path
from repository import views

urlpatterns = [
    path('', views.index, name='repo-index'),
    
]