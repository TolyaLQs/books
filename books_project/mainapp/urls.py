from django.urls import re_path
import mainapp.views as main

app_name = 'mainapp'

urlpatterns = [
    re_path('$', main.index, name='index'),

]
