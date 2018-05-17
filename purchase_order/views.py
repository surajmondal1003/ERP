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


from purchase_order.serializers import (
    PurchaseOrderSerializer,
    PurchaseDetailSerializer,
    PurchaseFreightSerializer,



)
from django.contrib.auth.models import User
from purchase_order.models import PurchaseOrderTerms,PurchaseOrderMap,PurchaseOrderFreight,PurchaseOrderDetail,PurchaseOrder

from django_filters.rest_framework import DjangoFilterBackend



class PurchaseOrderReadView(ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination



class PurchaseOrderReadDropdown(ListAPIView):
    queryset = PurchaseOrder.objects.filter(status=True)
    serializer_class = PurchaseOrderSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]



class PurchaseOrderMatser(ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]



class PurchaseOrderUpdate(RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]
