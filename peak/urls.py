"""
URL configuration for peak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from messaging.views import *
from config.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'applications', ApplicationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('api/users/search/', user_search, name='user_search'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
