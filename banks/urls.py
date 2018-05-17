from banks import views
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register(r'banks', views.BankViewSet)


urlpatterns = [
    path('', include(router.urls)),


]
