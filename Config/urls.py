"""Config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views

from API.router import router

urlpatterns = [
    path("", include("User.urls", namespace= "User")), # Default Auth URL
    path('',include('Quran.urls', namespace="Quran")),
    path('admin/', admin.site.urls),
    path('api/',include('API.urls', namespace="API")),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# Header
## Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
"""
    key: Authorization
    value: TOKEN <token>

    http://127.0.0.1:8000/api-token-auth/

    {
        "username": "f@f.com",
        "password": 12345
    }
"""