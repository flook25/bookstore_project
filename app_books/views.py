from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def books(request):
    return render(request, 'app_books/books.html')


