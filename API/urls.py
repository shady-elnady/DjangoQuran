from django.urls import path
from rest_framework.authtoken import views

from .views import UserDetailAPI,RegisterUserAPIView



app_name = "API"



urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
]


## Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b