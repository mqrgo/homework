from django.db import models
from slugify import slugify #встроенный slugify не работал, поэтому воспользовался сторонней библиотекой



class Author(models.Model):
    
    WHERE_FROM = [
        ('RU', 'Россия'),
        ('USA', 'Америка'),
        ('ENG', 'Англия'),
        ('GER', 'Гурмания'),
        ('FRA', 'Франция'),
    ]  
    
    first_name = models.CharField(max_length=50,verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    short_biography = models.TextField(verbose_name='Краткая биография')
    birth_date = models.DateField(verbose_name='Дата рождения')
    where_from = models.CharField(max_length=4, choices=WHERE_FROM)
    slug = models.SlugField(blank=True, editable=False)
    
    class Meta:
        ordering = ['first_name', 'last_name']
        unique_together = [['first_name', 'last_name']]
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    
    def save(self, *ar, **kw):
        fullname = f'{self.first_name}-{self.last_name}'
        self.slug = slugify(fullname)
        super().save(*ar, **kw)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Book(models.Model):
    
    GENRE = [
        ('Nov', 'Новелла'),
        ('Dra', 'Драма'),
        ('Poe', 'Поэма'),
        ('Rom', 'Роман'),
        ('Epo', 'Эпос'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Название книги')
    genre = models.CharField(max_length=3, choices=GENRE, verbose_name='Жанр')
    published = models.DateField(verbose_name='Дата публикации')
    aurhor = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    slug = models.SlugField(blank=True, editable=False)
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        
    def __str__(self):
        return self.name
        
    def save(self, *ar, **kw):
        self.slug = slugify(self.name)
        super().save(*ar, **kw)