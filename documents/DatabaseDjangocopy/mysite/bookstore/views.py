from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the bookstore index.")
# Create your views here.

def all_books(request):
	return HttpResponse("Hello, world. You're viewing all books")

def book(request, book_id):
	HttpResponse("Hello, world. You're viewing %s" % book_id)