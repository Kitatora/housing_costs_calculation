from django.urls import path
from app import views

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('about/', views.AbtView.as_view(), name='about')
]