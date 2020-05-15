from django.shortcuts import render, redirect
from wordcloud import WordCloud
from django.http import HttpResponse
from repository import models
from repository import views
from openpyxl import Workbook
from sentiment import analysissentiment
from repository.views import is_auth
from senti_research.settings import BASE_DIR, MEDIA_ROOT, STATIC_URL, STATICFILES_DIRS
import base64
import os

def generate_sentiment(request, pk):
    user = is_auth(request)
    if request.method == 'GET':
        if(user == None):
            return redirect('signin')
        researchproject = models.ResearchProject.objects.get(pk=pk)
        total_hasil_positif, total_hasil_negatif, total_hasil_sentiment, nilai, data_for_word_cloud = analysissentiment.counting_sentiment(researchproject)
        wordcloud_image = create_wordcloud_image(data_for_word_cloud, researchproject.id)
        if(wordcloud_image):
            print(wordcloud_image)
        return render(request, 'sentiment/research-analysis.html', {'nilai':nilai, 'total_hasil_positif':total_hasil_positif, 'total_hasil_negatif':total_hasil_negatif, 
        'total_hasil_sentiment':total_hasil_sentiment, 'researchproject':researchproject, 'user':user, 'wordcloud_image':'sentiment/'+wordcloud_image })

def create_wordcloud_image(data, project_id):
    background_color = "#FFFFFF"
    height = 720
    width = 1080

    word_cloud = WordCloud(
        background_color=background_color,
        width=width,
        height=height
    )

    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static','sentiment')
    word_cloud.generate_from_frequencies(data)

    image_name ='wordcloud_' + str(project_id) + '.png'
    word_cloud.to_file(STATICFILES_DIRS[0] + "/sentiment/"+ image_name )
    
    # with open(url, "rb") as image_file:
    #     encoded_image = base64.b64encode(image_file.read())
    #     return encoded_image
    return image_name