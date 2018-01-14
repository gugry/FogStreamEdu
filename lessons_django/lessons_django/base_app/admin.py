from django.contrib import admin

from lessons_django.base_app.models import Author, Book, Genre
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
