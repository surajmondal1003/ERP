from purchase_order import views
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path



urlpatterns = [
    path('all_purchase_order/',views.PurchaseOrderReadView.as_view()),
    path('purchase_order/', views.PurchaseOrderMatser.as_view()),
    path('purchase_order/<pk>/', views.PurchaseOrderUpdate.as_view()),
    path('purchase_order_dropdown/', views.PurchaseOrderReadDropdown.as_view()),


]
