from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='list'),
    path('habit_update/<str:pk>/', views.updateHabit, name='habit_update'),
    path('delete/<str:pk>/', views.deleteHabit, name='delete'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
]