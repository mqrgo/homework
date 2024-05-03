from django.urls import path
from test_app import views

app_name = 'test_app'

urlpatterns = [
    # path('date_time/', views.date_time_response, name='date_time_response'),
    # path('upload/', views.test_upload, name='test_upload'),
    path('', views.index, name='index'),
]

