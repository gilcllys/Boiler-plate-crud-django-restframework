from rest_framework import routers
from core import viewsets
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'user', viewsets.UserViewSet)


urlpatterns = router.urls
