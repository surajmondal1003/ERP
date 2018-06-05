from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,GenericAPIView,RetrieveAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from authentication.pagination import ErpLimitOffestpagination, ErpPageNumberPagination

from salesorg_group.serializers import (
   SalesOrgSerializer,
   SalesGroupSerializer

)
from django.contrib.auth.models import User
from salesorg_group.models import SalesOrg,SalesGroup
from company.models import Company
from rest_framework import filters


# Create your views here.


class SalesOrgViewSet(viewsets.ModelViewSet):
    queryset = SalesOrg.objects.all()
    serializer_class =SalesOrgSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','description')

    def get_queryset(self):
        try:
            order_by = self.request.query_params.get('order_by', None)
            field_name = self.request.query_params.get('field_name', None)

            if order_by and order_by.lower() == 'desc' and field_name:
                queryset = SalesOrg.objects.all().order_by('-' + field_name)
            elif order_by and order_by.lower() == 'asc' and field_name:
                queryset = SalesOrg.objects.all().order_by(field_name)
            else:
                queryset = SalesOrg.objects.all().order_by('-id')
            return queryset

        except Exception as e:
            raise


class SalesGroupViewSet(viewsets.ModelViewSet):
    queryset = SalesGroup.objects.all()
    serializer_class =SalesGroupSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description')

    def get_queryset(self):
        try:
            order_by = self.request.query_params.get('order_by', None)
            field_name = self.request.query_params.get('field_name', None)

            if order_by and order_by.lower() == 'desc' and field_name:
                queryset = SalesGroup.objects.all().order_by('-' + field_name)
            elif order_by and order_by.lower() == 'asc' and field_name:
                queryset = SalesGroup.objects.all().order_by(field_name)
            else:
                queryset = SalesGroup.objects.all().order_by('-id')
            return queryset

        except Exception as e:
            raise

