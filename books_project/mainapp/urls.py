from django.urls import re_path
import mainapp.views as main

app_name = 'mainapp'

urlpatterns = [
    re_path('$', main.index, name='index'),
    re_path('genre/(?P<genre>.*\s*)/$', main.genre, name='genre'),
    re_path('top/(?P<top>.*\s*)/$', main.top, name='top'),
    re_path('search/(?P<search>.*\s*)/$', main.search, name='search'),
    re_path('book/(?P<book>.*\s*)/$', main.book, name='book'),
]
