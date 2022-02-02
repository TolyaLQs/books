from django.urls import re_path
import mainapp.views as main

app_name = 'mainapp'

urlpatterns = [
    re_path('$', main.index, name='index'),
    re_path('genre/(?P<genre>.*\s*)/$', main.ganre, name='genre'),
]
