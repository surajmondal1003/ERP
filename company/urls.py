from company import views
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from company.views import CompanyListView


router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('company_dropdownlist/', CompanyListView.as_view(),name='company_list'),

]
