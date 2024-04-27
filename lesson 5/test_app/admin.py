from django.contrib import admin
from test_app.models import Author, Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'short_biography',
        'birth_date',
        'where_from',
        'slug',
    ]
    
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'genre',
        'published',
        'aurhor',
        'slug',
    ]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

