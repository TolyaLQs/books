from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from books_project.mainapp.models import Book


def index(request):
    if request.POST:
        if 'search' in request.POST and request.POST['search']:
            search_text = request.POST['search']
            request.session['search'] = search_text
            return HttpResponseRedirect(reverse('mainapp:search'))

    books_new = Book.objects.all().order_by('-year_publishing')
    context = {
        'books_new': books_new,
    }
    return render(request, 'mainapp/main_page.html', context)


def genres(request):
    context = {}
    return render(request, 'mainapp/top_gen_new_pop_pages.html')


def genre(request, genre=None):
    context = {}
    return render(request, 'mainapp/top_gen_new_pop_pages.html')


def top(request, top=None):
    context = {}
    return render(request, 'mainapp/top_gen_new_pop_pages.html')


def pop(request, top=None):
    context = {}
    return render(request, 'mainapp/top_gen_new_pop_pages.html')


def new(request):
    context = {}
    return render(request, 'mainapp/top_gen_new_pop_pages.html', context)


def search(request):
    search_text = request.session.get('search', '-')
    books = Book.objects.filter(name=search_text)
    context = {
        'books': books,
    }
    return render(request, 'mainapp/search_page.html')


def book(request, book=None):
    context = {}
    return render(request, 'mainapp/book_page.html')
