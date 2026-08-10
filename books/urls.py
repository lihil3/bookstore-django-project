from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='books.index'),
    path('list_books/', views.list_books, name='books.list_books'),
    path('add_book/', views.add_book, name='books.add_book'),
    path('search/', views.search_books, name='books.search'),
    path('<int:book_id>/', views.view_book, name='books.view_book'),
]