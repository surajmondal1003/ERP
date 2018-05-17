from purchase_invoice import views
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path



urlpatterns = [
    path('all_purchase_invoice/',views.PurchaseInvoiceReadView.as_view()),
    path('purchase_invoice/', views.PurchaseInvoiceMatser.as_view()),
    path('purchase_invoice/<pk>/', views.PurchaseInvoiceUpdate.as_view()),


]
