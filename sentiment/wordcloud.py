# from django.contrib.staticfiles.storage import staticfiles_storage
# from sentiment import analysissentiment
# from nltk.tokenize import sent_tokenize, word_tokenize
# from wordcloud import WordCloud, STOPWORDS 

# # image configurations
# background_color = "#101010"
# height = 720
# width = 1080


# def word_cloud(research_project):
#     answers = models.ResearchAnswer.objects.filter(research_project=research_project)
#     for answer in answers:
#         dataStatis = answer.answer
#         hasilToken = tokenization(dataStatis)
#         ngramPositif, ngramNegatif, ngram1 = sentiWordBeforeStem(hasilToken)
#         hasilStem = stemmingWord(ngram1)
#         hasilNoPuct = punctuationRemoval(hasilStem)
#         hasilStopWord = stopwordRemoval(hasilNoPuct)
#         hasilPraprosesCoding = hasilStopWord

#         answer[answer] = answer.get(answer, 0) + 1

#     word_cloud = WordCloud(
#         background_color=background_color,
#         width=width,
#         height=height
#     )
#     word_cloud.generate_from_frequencies(answer)
