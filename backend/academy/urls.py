from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),  
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),


]
