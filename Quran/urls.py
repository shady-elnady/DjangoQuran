from django.urls import path

from .views import home, about, brand , contact, special


app_name = "Quran"


urlpatterns = [
  path('',home, name= "Home"),
  path('about',about, name= "About"),
  path('brand',brand, name= "Brand"),
  path('contact',contact, name= "Contact"),
  path('special',special, name= "Special"),
]
