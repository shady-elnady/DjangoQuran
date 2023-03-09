from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import LoginPageView, Signup


app_name = "User"


urlpatterns = [
  path('login', LoginPageView.as_view(), name='LogIn' ),
  path('signup',Signup.as_view(), name= "SignUp"),
  path('logout/', LogoutView.as_view(), name='LogOut'),
]