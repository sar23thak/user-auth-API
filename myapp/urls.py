from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, viewuser


router = routers.DefaultRouter()
router.register('user', UserViewSet)
# router.register('getdetails', viewuser)
urlpatterns = [
    path('', include(router.urls)),
    path('getdetails/', viewuser),
    ]