# urls.py
from django.urls import path
from .views import install_file

urlpatterns = [
    path('install/', install_file, name='install-file'),
]
