
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views
from . import api


router = routers.DefaultRouter()
router.register('users', views.UserViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    
]

    