from django.contrib import admin

# Register your models here.
from mainapp.models import Book, BookComment, Language, Author, Genre

admin.site.register(Book)
admin.site.register(BookComment)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Genre)

