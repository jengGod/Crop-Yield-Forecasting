from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('model',views.model),
    path('provinces/', views.Province),  
]