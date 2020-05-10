from django.shortcuts import render, redirect
from django.http import HttpResponse
from repository import models
from repository import views
from openpyxl import Workbook
from sentiment import analysissentiment
from repository.views import is_auth

def generate_sentiment(request, pk):
    user = is_auth(request)
    if request.method == 'GET':
        if(user == None):
            return redirect('signin')
        researchproject = models.ResearchProject.objects.get(pk=pk)
        total_hasil_positif, total_hasil_negatif, total_hasil_sentiment, nilai = analysissentiment.counting_sentiment(researchproject)
        return render(request, 'sentiment/research-analysis.html', {'nilai':nilai, 'total_hasil_positif':total_hasil_positif, 'total_hasil_negatif':total_hasil_negatif, 'total_hasil_sentiment':total_hasil_sentiment, 'user':user })