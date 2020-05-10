from django.urls import include, path, re_path
from sentiment import views

urlpatterns = [
    path('generate/<str:pk>/', views.generate_sentiment, name='generate_sentiment'),
]