from django.contrib import admin

from library.models import Author, Book, Genre
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
