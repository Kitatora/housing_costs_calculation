from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AbtView.as_view(), name='about'),
]