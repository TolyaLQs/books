from django.urls import re_path
import userapp.views as user

app_name = 'userapp'

urlpatterns = [
    re_path('register/$', user.register, name='register'),
]