
from django.urls import path, include
from .views import todo

urlpatterns = [
    path('a/', todo),
]
