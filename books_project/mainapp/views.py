from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/main_page.html')


def genres(request):
    return render(request, 'mainapp/top_gen_new_pop_pages.html')


def genre(request, genre=None):
    return render(request, 'mainapp/top_gen_new_pop_pages.html')


def top(request, top=None):
    return render(request, 'mainapp/top_gen_new_pop_pages.html')


def pop(request, top=None):
    return render(request, 'mainapp/top_gen_new_pop_pages.html')


def new(request):
    context = {}
    return render(request, 'mainapp/top_gen_new_pop_pages.html', context)


def search(request, search=None):
    return render(request, 'mainapp/search_page.html')


def book(request, book=None):
    return render(request, 'mainapp/book_page.html')

