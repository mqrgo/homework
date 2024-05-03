from django.contrib import admin
from test_app.models import Author, Book
from django.utils.safestring import mark_safe
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'display_photo',
        'short_biography',
        'birth_date',
        'where_from',
        'slug',
    ]
    
    @admin.display
    def display_photo(self, author: Author):
        if author.photo:
            return mark_safe(f"<img src='{author.photo.url}' width=50")
        return 'None'
    
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'display_cover',
        'genre',
        'published',
        'author',
        'price',
        'slug',
    ]
    
    @admin.display
    def display_cover(self, book: Book):
        if book.cover:
            return mark_safe(f"<img src='{book.cover.url}' width=50")
        return None

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

