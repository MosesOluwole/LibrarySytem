# library/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('members/', views.member_list, name='member_list'),
    path('members/add/', views.add_member, name='add_member'),
    path('members/edit/<int:member_id>/',
         views.edit_member, name='edit_member'),
    path('members/delete/<int:member_id>/',
         views.delete_member, name='delete_member'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('return/', views.return_book, name='return_book'),
]
