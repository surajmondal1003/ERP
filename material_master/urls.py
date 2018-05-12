from material_master import views
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register(r'all_material_type', views.MaterialTypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('create_material_master/',views.MaterialMasterCreate.as_view()),
    path('all_material_master/',views.MaterialReadView.as_view()),
    path('update_material_master/<material>/', views.MaterialMasterUpdate.as_view()),
    #path('delete_material_master/',views.MaterialDeleteView.as_view()),


]
