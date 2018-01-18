from django.db import models

class Book(models.Model):
    name = models.CharField('Название', max_length=32)
    # author = models.ForeignKey('Author', verbose_name='Автор', on_delete='CASCADE', related_name='author')
    author = models.ManyToManyField('Author', verbose_name='Автор', related_name='author')
    genre = models.ForeignKey('Genre', verbose_name='Жанр', on_delete='CASCADE', related_name='genre')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Author(models.Model):
    name = models.CharField('Имя',max_length=32)
    sername = models.CharField('Фамилия',max_length=32)
    patronymic = models.CharField('Отчество ',max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-sername',)
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Genre(models.Model):
    name = models.CharField('Жанр', max_length=32)
    description = models.CharField('Описание', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
