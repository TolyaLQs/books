from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/main_page.html')


def genre(request, genre=None):
    pass


def top(request, top=None):
    pass


def search(request, search=None):
    pass


def book(request, book=None):
    pass

