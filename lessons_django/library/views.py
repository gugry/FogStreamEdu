from django.shortcuts import render
from .models import Author, Book, Genre
from django.http import HttpResponse
from django.template import loader

# def index(request, sort_field):
#     author_list = Author.objects.order_by(sort_field)
#     output = ', '.join([author.name + ' ' + author.sername for author in author_list])
#     return HttpResponse(output)

def index(request, sort_field='id'):
    author_list = Author.objects.order_by(sort_field)
    template = loader.get_template('library/index.html')
    # output = ', '.join([author.name + ' ' + author.sername for author in author_list])
    context = {
        'author_list': author_list,
    }
    return HttpResponse(template.render(context, request))

# def author(request, author_id):
#     author_qset = Author.objects.get(id= author_id)
#     books_qset = author_qset.author_book.all()
#     books = []
#     for book in books_qset:
#         books.append([book, book.genre])
#     return HttpResponse(books[0])

def author(request, author_id):
    author_qset = Author.objects.get(id=author_id)
    books_qset = author_qset.author_book.all()
    template = loader.get_template('library/author.html')
    context = {
        'author': author_qset,
        'books': books_qset
    }
    return HttpResponse(template.render(context, request))

def genre(request, genre_id):
    genre_qset = Genre.objects.get(id=genre_id)
    books_qset = genre_qset.genre_book.all()
    template = loader.get_template('library/genre.html')
    context = {
        'genre': genre_qset,
        'books': books_qset
    }
    return HttpResponse(template.render(context, request))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))



# def index(request):
#     return HttpResponse("Hello, world.")
