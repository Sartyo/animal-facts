from django.urls import path
from . import views

app_name = 'facts'

urlpatterns = [
    path('dog-facts', views.dog_facts, name='dog_facts'),
    path('cat-facts', views.cat_facts, name='cat_facts'),
]