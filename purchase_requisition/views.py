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


from purchase_requisition.serializers import (
    RequisitionDetailSerializer,
    RequisitionSerializer,
    RequisitionReadSerializer,
    RequisitionDetailReadSerializer,
    RequisitionUpdateStatusSerializer


)
from django.contrib.auth.models import User
from purchase_requisition.models import Requisition,RequisitionDetail

from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.


class RequisitionReadView(ListAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination




class RequisitionReadDropdown(ListAPIView):
    queryset = Requisition.objects.filter(status=True, is_approve=1, is_finalised=0)
    serializer_class = RequisitionReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

class RequisitionReadDetailView(RetrieveAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]



class RequisitionMatser(ListCreateAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer
    authentication_classes = [TokenAuthentication]



class RequisitionUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer

class RequisitionUpdateStatus(RetrieveUpdateAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionUpdateStatusSerializer








