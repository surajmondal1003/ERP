from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView
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
    PurchaseOrderReadSerializer,
    PurchaseOrderUpdateStatusSerializer



)
from django.contrib.auth.models import User
from purchase_order.models import PurchaseOrderTerms,PurchaseOrderMap,PurchaseOrderFreight,PurchaseOrderDetail,PurchaseOrder

from django_filters.rest_framework import DjangoFilterBackend



class PurchaseOrderReadView(ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination


class PurchaseOrderReadDetailView(RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]





class PurchaseOrderReadDropdown(ListAPIView):
    queryset = PurchaseOrder.objects.filter(status=True, is_approve=1, is_finalised=0)
    serializer_class = PurchaseOrderReadSerializer
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

class PurchaseOrderByRequisition(ListAPIView):
    serializer_class = PurchaseOrderReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        requisition=self.kwargs['requisition']
        return PurchaseOrder.objects.filter(requisition_id=requisition,status=True)
    # def get_queryset(self):
    #     requisition=self.kwargs['requisition']
    #     return PurchaseOrder.objects.filter(requisition_id=requisition)



class PurchaseOrderUpdateStatus(RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderUpdateStatusSerializer
