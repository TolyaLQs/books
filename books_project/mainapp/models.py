from django.db import models
from userapp.models import User
# Create your models here.


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=16, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Author(models.Model):
    name = models.CharField(verbose_name='Имя автора', max_length=65, unique=True)
    author_photo = models.ImageField(verbose_name='Фото Автора', upload_to='AuthorPhoto')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Language(models.Model):
    name = models.CharField(verbose_name='Язык', max_length=20, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Язык'
        verbose_name_plural = 'Язык'


class Book(models.Model):
    name = models.CharField(verbose_name='Название книги', max_length=64)
    book_photo = models.ImageField(verbose_name='Фото книги', upload_to='BookPhoto')
    genre = models.ForeignKey(Genre, to_field='name', verbose_name='Жанр', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', max_length=2048)
    author = models.ForeignKey(Author, to_field='name', verbose_name='Автор', on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name='Рейтинг', default=0)
    language = models.ForeignKey(Language, to_field='name', verbose_name='Язык', on_delete=models.CASCADE)
    year_publishing = models.DateField(verbose_name='Год издания')
    date_add = models.DateField(verbose_name='Добавлена', auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class BookComment(models.Model):
    book_name = models.ForeignKey(Book, to_field='id', verbose_name='Название', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Коментарий', blank=True, max_length=548)
    date_added = models.DateTimeField(verbose_name='Добавлен комментария', auto_now_add=True)
    avatar = models.ImageField(verbose_name='Фото комментария', blank=True, upload_to='BookCommentPhoto')
    moder_state = models.BooleanField(verbose_name='Проверил', blank=True, default=False)
    complaint_quantity = models.SmallIntegerField(verbose_name='кол-во жалоб', blank=True, default=0)

    def __str__(self):
        return f'{self.date_added} {self.author} {self.book_name}'

    class Meta:
        ordering = ['date_added']
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
