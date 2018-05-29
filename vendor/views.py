from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from authentication.pagination import ErpLimitOffestpagination, ErpPageNumberPagination
from django_filters.rest_framework import filters
from rest_framework import filters


from vendor.serializers import (
    VendorTypeSerializer,
    VendorAccountSerializer,
    VendorAddressSerializer,
    VendorSerializer,
    VendorUpdateStatusSerializer



)
from django.contrib.auth.models import User
from vendor.models import VendorType,VendorAccount,VendorAddress,Vendor

from django_filters.rest_framework import DjangoFilterBackend



class VendorTypeViewSet(viewsets.ModelViewSet):
    queryset = VendorType.objects.all()
    serializer_class =VendorTypeSerializer
    #permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('vendor_type',)


class VendorReadView(ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('vendor_fullname',)


class VendorReadDropdown(ListAPIView):
    queryset = Vendor.objects.filter(status=True)
    serializer_class = VendorSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]



class VendorMatserCreate(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination



class VendorMatserUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

class VendorMatserStatusUpdate(RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorUpdateStatusSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

