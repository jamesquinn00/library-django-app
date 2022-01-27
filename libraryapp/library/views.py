from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from .forms import NewBookForm, RentBookForm
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

@login_required
def create(request):
    if request.method == 'POST':
        book = NewBookForm(request.POST)
        if book.is_valid():
            book_id = book.save().id
            return redirect("book-show", book_id=book_id)
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(request, 'books/new.html', data)

@login_required
def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = RentBookForm(request.POST)
        if form.is_valid():
            book.owner = request.user
            book.save()
            return redirect("book-show", book_id=book_id)
    else:
        form = RentBookForm(initial={'author': request.user})
    data = {
        'book': book,
        'form': form
    }
    return render(request, 'books/show.html', data)

def index(request):
    return render(request, 'home.html')