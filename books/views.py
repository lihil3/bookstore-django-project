from django.shortcuts import render
from .models import Book
from .forms import BookForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

#10
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

#11
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'add_book.html', {
                'form': BookForm(),
                'message': 'Book added successfully!'
            })
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

#12
def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'view_book.html', {'book': book})

#13
def search_books(request):
    query = request.GET.get('q', '')

    books = Book.objects.filter(title__icontains=query)

    return render(request, 'search.html', {
        'books': books,
        'query': query
    })