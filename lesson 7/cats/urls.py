from cats import views
from django.urls import path


app_name = 'cats'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/<int:cat_id>', views.about, name='about'),    
]