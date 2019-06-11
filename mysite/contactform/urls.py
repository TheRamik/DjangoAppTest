from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.get_contact, name='contact'),
    path('success/', views.successView, name='success'),
]