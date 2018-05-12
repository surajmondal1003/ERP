from salesorg_group import views
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register(r'all_sales_organization', views.SalesOrgViewSet)
router.register(r'all_sales_group', views.SalesGroupViewSet)


urlpatterns = [
    path('', include(router.urls)),


]