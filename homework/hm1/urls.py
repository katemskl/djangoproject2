from django.urls import path
from . import views

urlpatterns = [
    path('strings/<str:lang>/', views.string, name='strings'),
    path('cars/<str:name>/', views.cars, name='cars'),
    path('week/<str:day>/', views.week, name='week')
]
