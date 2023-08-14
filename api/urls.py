from django.urls import path
from . import views

urlpatterns = [
    path('get_random_array/', views.get_random_array, name='get_random_array'),
]
