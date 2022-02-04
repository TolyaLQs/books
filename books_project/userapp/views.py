from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from userapp.forms import MyUserCreationForm, MyUserChangeForm, MyUserChangeAvatarForm
from userapp.models import User, UserFriend
from django.http import JsonResponse


def user_login(request):
    if request.is_ajax():
        print('AJAX login', request.META['HTTP_REFERER'])
        context = {
            'login': reverse('userapp:login'),
        }
        return JsonResponse(context)

    if request.POST:
        if 'email' in request.POST and request.POST['email']:
            email = request.POST['email']
            password = request.POST['psw']
            user = authenticate(email=email, password=password)
            if user is not None:
                print('пользователь найден: ', user)
                login(request, user)
                message = f'Пользователь с емайлом {email} залогинелся'
                # send_mail(
                #     'GurSdGames',
                #     message,
                #     'testyatesttest@yandex.ru',
                #     [u'sdtolya@gmail.com'],
                # )
                return HttpResponseRedirect(reverse('index'))

    return render(request, 'authapp/login.html')


def user_logout(request):
    logout(request)  # стираем токен аутентификации из cookie
    return HttpResponseRedirect(reverse('index'))


def user_register(request):
    if request.method == "POST":
        register_form = MyUserCreationForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            email = request.POST['email']
            message = f'Пользователь с емайлом {email} зарегистрировался'
            send_mail(
                'GurSdGames',
                message,
                'testyatesttest@yandex.ru',
                [u'sdtolya@gmail.com'],
            )
            password = request.POST['password1']
            user = authenticate(email=email, password=password)
            if user is not None:
                print('пользователь найден: ', user)
                login(request, user)

                return HttpResponseRedirect(reverse('index'))
    else:
        register_form = MyUserCreationForm()
    context = {
        'register_form': register_form,
    }

    return render(request, 'userapp/register.html', context)


def user_edit(request):
    if request.method == "POST":
        edit_form = MyUserChangeForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('userapp:edit'))

    else:
        edit_form = MyUserChangeForm(instance=request.user)

    context = {
        'edit_form': edit_form
    }

    return render(request, 'userapp/edit.html', context)


def user_profile(request, id=None):

    if request.method == 'GET':
        print(id)
        if id:
            profile = User.objects.filter(id=id)
            context = {
                'profile': profile,

            }
            return render(request, 'userapp/user_profile.html', context)

    if request.method == "POST":
        if 'avatar' in request.POST and request.POST['avatar']:
            edit_for = MyUserChangeAvatarForm()
            if edit_for.is_valid():
                edit_for.save()
                return HttpResponseRedirect(f'/user/profile/{id}')