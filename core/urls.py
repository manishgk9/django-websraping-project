from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index),
    path('', views.home, name='homepage'),
    path('mobile/<str:pk>', views.Product, name='productpage'),
    path('electronics/<str:pk>', views.ElectronicPage, name='electronicpage'),
    path('smarttv/<str:pk>', views.Smart_tv, name='tvpage'),
    path('about/', views.About, name='aboutpage'),
]
