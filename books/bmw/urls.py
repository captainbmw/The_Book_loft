from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
path('register/', views.register, name='register'),
path('success/', views.success, name='success'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('books/', views.books, name='books_by_category'),
path('books/author/', views.books_by_author, name='books_by_author'),
    path('pay', views.pay, name='pay'),
    path('stk', views.stk, name="stk"),
    path('token', views.token, name='token'),
]
