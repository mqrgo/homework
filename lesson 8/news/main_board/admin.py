from django.contrib import admin
from main_board.models import NewsPost, Category
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'display_cover',
        'created',
        'author',
        'category',
        'slug',
    ]
    
    @admin.display
    def display_cover(self, news: NewsPost):
        if news.cover:
            return mark_safe(f"<img src='{news.cover.url}' width=50")
        return None
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']