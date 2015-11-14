from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
	fields = ['title', 'pub_date', 'isbn']
	list_display = ('title', 'pub_date')

admin.site.register(Book, BookAdmin)