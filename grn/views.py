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


from grn.serializers import (
    GRNSerializer,
    GRNDetailSerializer,
    GRNMapSerializer,
    GRNReadSerializer,
    GRNUpdateStatusSerializer

)
from django.contrib.auth.models import User
from grn.models import GRNMap,GRNDetail,GRN

from django_filters.rest_framework import DjangoFilterBackend



class GRNReadViewList(ListAPIView):
    queryset = GRN.objects.all()
    serializer_class = GRNReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination




class GRNReadViewDropdown(ListAPIView):
    queryset = GRN.objects.filter(status=True, is_approve=1, is_finalised=0)
    serializer_class = GRNReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]




class GRNReadViewDetail(RetrieveAPIView):
    queryset = GRN.objects.all()
    serializer_class = GRNReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]



class GRNCreate(ListCreateAPIView):
    queryset = GRN.objects.all()
    serializer_class = GRNSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination


class GRNUpdate(RetrieveUpdateDestroyAPIView):
    queryset = GRN.objects.all()
    serializer_class = GRNSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

class GRNByPurchaseOrder(ListAPIView):
    serializer_class = GRNReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        po_order=self.kwargs['po_order']
        return GRN.objects.filter(po_order_id=po_order,status=True)
    # def get_queryset(self):
    #     requisition=self.kwargs['requisition']
    #     return PurchaseOrder.objects.filter(requisition_id=requisition)



class GRNUpdateStatus(RetrieveUpdateAPIView):
    queryset = GRN.objects.all()
    serializer_class = GRNUpdateStatusSerializer
