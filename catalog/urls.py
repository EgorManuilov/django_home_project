from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('contacts/', views.contacts)
]