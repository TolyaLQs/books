from django.urls import re_path
import userapp.views as user

app_name = 'userapp'

urlpatterns = [
    re_path('register/$', user.register, name='register'),
    re_path('login/$', user.user_login, name='login'),
    re_path('logout/$', user.user_logout, name='logout'),
    re_path('edit/$', user.user_edit, name='edit'),
    re_path('profile/(?P<id>.*\s*)/$', user.user_profile, name='profile'),
]

