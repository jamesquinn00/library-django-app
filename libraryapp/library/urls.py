from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='library-home'),
    path('about/', views.about, name='library-about'),
    path('books/', views.get_books, name='library-books'),
    path('login/', views.get_books, name='library-index'),
    path('books/<int:id>/', views.show, name='library-show'),
]