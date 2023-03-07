from django.urls import path
from rest_framework.authtoken import views

from .views import UserDetailAPI,RegisterUserAPIView



app_name = "API"


urlpatterns = [
  path("get-my_details",UserDetailAPI.as_view(), name= "GetUserDetails"),
  path('register',RegisterUserAPIView.as_view(), name= "Registeration"),
]


## Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b