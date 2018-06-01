from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,ListCreateAPIView,RetrieveAPIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from authentication.pagination import ErpLimitOffestpagination, ErpPageNumberPagination
from django_filters.rest_framework import filters
from rest_framework import filters

from departments.serializers import (
    DepartmentsSerializer,
    DepartmentsReadSerializer

)

from django.contrib.auth.models import User
from departments.models import Departments

# Create your views here.


class DepartmentsReadView(ListAPIView):
    queryset = Departments.objects.filter(is_deleted=False)
    serializer_class = DepartmentsReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('department_name',)


class DepartmentsReadDetailView(RetrieveAPIView):
    queryset = Departments.objects.filter(is_deleted=False)
    serializer_class = DepartmentsSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]


class DepartmentsMatser(ListCreateAPIView):
    queryset = Departments.objects.filter(is_deleted=False)
    serializer_class = DepartmentsSerializer
    authentication_classes = [TokenAuthentication]


class DepartmentsUpdate(RetrieveUpdateAPIView):
    queryset = Departments.objects.filter(is_deleted=False)
    serializer_class = DepartmentsSerializer
    authentication_classes = [TokenAuthentication]

class SpecificCompanyDepartments(ListAPIView):

    serializer_class = DepartmentsReadSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        company=self.kwargs['company']
        return Departments.objects.filter(company_id=company,status=True,is_deleted=False)
