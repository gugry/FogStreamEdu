from django.db import models

class Book(models.Model):
    name = models.CharField('Название', max_length=32)
    author = models.ManyToManyField('Author', verbose_name='Автор', related_name='author_book')
    genre = models.ForeignKey('Genre', verbose_name='Жанр', on_delete='CASCADE', related_name='genre_book')
    # Жанр оставил один-ко-многим для примера

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Author(models.Model):
    name = models.CharField('Имя',max_length=32)
    sername = models.CharField('Фамилия',max_length=32)
    patronymic = models.CharField('Отчество ',max_length=32)

    def __str__(self):
        return self.sername

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Genre(models.Model):
    name = models.CharField('Жанр', max_length=32)
    description = models.CharField('Описание', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
