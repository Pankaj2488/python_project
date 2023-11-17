from django.urls import path
from .views import word_counter

urlpatterns = [
    path('', word_counter, name='word_counter'),
]
