from django.urls import path

from . import views

urlpatterns = [
    path('',  views.index, name='index'),
    path('<str:sort_field>/',  views.index, name='index'),
    path('author/<int:author_id>/',  views.author, name='author'),
    path('genre/<int:genre_id>/',  views.genre, name='genre'),

#? Я хочу, чтобы переходя в корень сайта я попадал на страницу авторов с сортировкой по имени
]