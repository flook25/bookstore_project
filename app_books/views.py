from django.shortcuts import render

BOOKS = [
    {
        "id": 1,
        "title": "Python Programming 101",
        "author": "John Doe",
        "price": 350,
        "img": "https://cdn-icons-png.flaticon.com/128/29/29302.png"
    },
    {
        "id": 2,
        "title": "Django for Beginners",
        "author": "Jane Smith",
        "price": 420,
        "img": "https://cdn-icons-png.flaticon.com/128/29/29302.png"
    },
    {
        "id": 3,
        "title": "R Programming for Data Science",
        "author": "Jane Miller",
        "price": 390,
        "img": "https://cdn-icons-png.flaticon.com/128/29/29302.png"
    }
]

def books(request):
    return render(request, 'app_books/books.html', {'books': BOOKS})

def book(request, book_id):
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    return render(request, 'app_books/book.html', {'book': book})