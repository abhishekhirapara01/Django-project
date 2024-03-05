from django.urls import path
from .views import fibonacci_view,home

urlpatterns = [
  path('fibonacci/<int:n>/', fibonacci_view, name = 'fibonacci_view'),
  path('home/', home, name='home'),
  ]