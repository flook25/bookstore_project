# Django Bookstore

A web-based bookstore built with Django where users can browse books, register, login, and place orders.

## Features

- User authentication (register/login/logout)
- Browse books by category
- Add to cart & checkout
- Admin panel for managing books and orders

## Tech Stack

- Django (Python)
- HTML/CSS (Bootstrap or Tailwind)
- SQLite (default Django DB)

## Run Locally

```bash
git clone https://github.com/your-username/bookstore-django.git
cd bookstore-django
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
