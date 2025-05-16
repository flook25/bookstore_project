from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def books(request):
    return render(request, 'app_books/books.html')

def book(request, book_id):
    return render(request, 'app_books/book.html', {'book_id': book_id})
