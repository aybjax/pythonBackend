from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
#
##
#
from .models import Book
#
##
#
from django.template import loader # removed
from django.shortcuts import render
#
##
#
from django.http import Http404


def index(request):
    books = Book.objects.all()
    context = {
        "books" : books
    }
    return render(request, 'books/index.html', context)

def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404('This book does not exist')
    return render(request, 'books/detail.html', {'book': book})