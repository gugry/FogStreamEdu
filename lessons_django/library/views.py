from django.shortcuts import render
from .models import Author, Book, Genre
from django.http import HttpResponse
from django.template import loader

def index(request, sort_field='id'):
    author_list = Author.objects.order_by(sort_field)
    template = loader.get_template('library/index.html')
    context = {
        'author_list': author_list,
    }
    return render(request, 'library/index.html', context)

def author(request, author_id):
    author_qset = Author.objects.get(id=author_id)
    books_qset = author_qset.author_book.all()
    template = loader.get_template('library/author.html')
    context = {
        'author': author_qset,
        'books': books_qset
    }
    return render(request, 'library/index.html', context)

    return HttpResponse(template.render(context, request))

def genre(request, genre_id):
    genre_qset = Genre.objects.get(id=genre_id)
    books_qset = genre_qset.genre_book.all()
    template = loader.get_template('library/genre.html')
    context = {
        'genre': genre_qset,
        'books': books_qset
    }

    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))




