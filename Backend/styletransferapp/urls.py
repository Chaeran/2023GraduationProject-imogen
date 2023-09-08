from django.urls import path
from . import views

# app_name = 'styletransferapp'

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('stylegen/', views.stylegen, name='stylegen'),
]