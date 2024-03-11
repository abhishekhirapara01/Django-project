from django.urls import path
from accounts import views
from app import views as appviews

urlpatterns = [
  path('',appviews.home,name='home'),
  path('signupaccount/',views.signupaccount,name='signupaccount'),
  path('login/',views.loginaccount,name='loginaccount'),
  path('logout/',views.logoutaccount,name='logoutaccount'),
]