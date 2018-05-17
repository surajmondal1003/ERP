from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from authentication.pagination import ErpLimitOffestpagination, ErpPageNumberPagination
from django_filters.rest_framework import filters
from rest_framework import filters


from purchase_invoice.serializers import (
    PurchaseInvoiceSerializer,

)
from django.contrib.auth.models import User
from purchase_invoice.models import PurchaseInvoice,PurchaseInvoiceDetail,PurchaseInvoiceMap

from django_filters.rest_framework import DjangoFilterBackend




class PurchaseInvoiceReadView(ListAPIView):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination


class PurchaseInvoiceMatser(ListCreateAPIView):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]



class PurchaseInvoiceUpdate(RetrieveUpdateDestroyAPIView):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
