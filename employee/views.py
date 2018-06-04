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


from employee.serializers import (
    EmployeeSerializer,
    EmployeeReadSerializer

)
from django.contrib.auth.models import User
from employee.models import Employee

from django_filters.rest_framework import DjangoFilterBackend




class EmployeeMatser(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication]



class EmployeeMatserUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication]


class EmployeeReadView(ListAPIView):
    queryset = Employee.objects.filter(is_deleted=False)
    serializer_class = EmployeeReadSerializer
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

    def get_queryset(self):
        try:
            order_by = self.request.query_params.get('order_by', None)
            field_name = self.request.query_params.get('field_name', None)

            if order_by and order_by.lower() == 'desc' and field_name:
                queryset = Employee.objects.filter(is_deleted=False).order_by('-' + field_name)
            elif order_by and order_by.lower() == 'asc' and field_name:
                queryset = Employee.objects.filter(is_deleted=False).order_by(field_name)
            else:
                queryset = Employee.objects.filter(is_deleted=False).order_by('-id')
            return queryset

        except Exception as e:
            raise



class EmployeeReadDetailView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeReadSerializer
    authentication_classes = [TokenAuthentication]
