from django.contrib import admin
from cats.models import Cat
from django.utils.safestring import mark_safe
# Register your models here.



class CatAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_photo', 'slug']
    
    @admin.display
    def display_photo(self, cat: Cat):
        if cat.photo:
            return mark_safe(f"<img src='{cat.photo.url}' width=50")
        return None
    
    
admin.site.register(Cat, CatAdmin)
