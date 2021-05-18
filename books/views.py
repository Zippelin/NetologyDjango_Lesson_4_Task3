from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def book_details(request, p_date):
    books = Book.objects.all().order_by('pub_date')

    dates_list = list(books.distinct().values_list('pub_date', flat=True))

    dates_list = [
        d.strftime('%Y-%d-%m')
        for d in dates_list
    ]
    page = dates_list.index(p_date.strftime('%Y-%d-%m'))

    next_url = None
    prev_url = None

    if len(dates_list) - 1 > page:
        next_url = datetime.strptime(dates_list[page + 1], '%Y-%d-%m')

    if page > 0:
        prev_url = datetime.strptime(dates_list[page - 1], '%Y-%d-%m')

    template = 'books/book_details.html'
    context = {
        'p_date': p_date,
        'books': books.filter(pub_date=p_date),
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, template, context)