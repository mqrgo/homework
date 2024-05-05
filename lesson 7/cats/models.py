from typing import Iterable
from django.db import models
from slugify import slugify

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100, verbose_name='Порода', unique=True)
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='cats_photoes', verbose_name='Фото', blank=True, null=True)
    slug = models.SlugField(verbose_name='Слаг', editable=False)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Котик'
        verbose_name_plural = 'Котики'
        
    def save(self, *ar, **kw):
        self.slug = slugify(self.name)
        super().save(*ar, **kw)
        
    def __str__(self):
        return self.name
    
    