from django.urls import path
from .import views
urlpatterns = [
    path('meals', views.meals,name='menu'),
    path('about', views.about,name='about'),
]
