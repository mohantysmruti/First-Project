from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cooking/', views.cooking, name='cooking'),
    path('electronics/', views.electronics, name='electronics'),
    path('essentials/', views.essentials, name='essentials'),
    path('furniture/',views.furniture, name='furniture'),
    path('vehicle/',views.vehicle, name='vehicle'),
    path('housing/', views.housing, name='housing')
]
