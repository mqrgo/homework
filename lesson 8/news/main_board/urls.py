from django.urls import path
from main_board import views

app_name = 'news'

urlpatterns = [
    path('<slug:category_slug>', views.index, name='index_with_category'),
    path('', views.index, name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', views.detail, name='detail'),
]
