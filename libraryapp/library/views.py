from django.shortcuts import render, get_object_or_404
from .models import Book
# Create your views here.

books = [
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Life', 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
    ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def get_books(request):
    data = { "books" : books }
    return render(request, 'books.html', data)

def show(request, id):
    # book = list(filter(lambda book:book["id"] == id, books))
    # data = { "book": book[0]}
    dog = get_object_or_404(Book, pk=id)
    return render(request, 'show.html', dog)

def not_found_404(request, exception):
    data = { "err" : exception }
    return render(request, "library/404.html", data)

def not_found_500(request):
    return render(request, "library/500.html")