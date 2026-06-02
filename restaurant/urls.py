from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('signature-dishes/', views.signature_dishes, name='signature_dishes'),
    path('branches/', views.branches, name='branches'),
    path('contact/', views.contact, name='contact'),
]