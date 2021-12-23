from rest_framework import routers
from .views import personaViewSet

routers = routers.DefaultRouter()
routers.register('persona', personaViewSet)

from django.urls import path ,include

urlpatterns = [
    path('api/', include(routers.urls)),
]