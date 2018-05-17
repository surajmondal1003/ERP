from grn import views
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path



urlpatterns = [
    path('all_grn/',views.GRNReadViewList.as_view()),
    path('all_grn/<pk>/',views.GRNReadViewDetail.as_view()),
    path('grn/', views.GRNCreate.as_view()),
    path('grn/<pk>/', views.GRNUpdate.as_view()),


]
