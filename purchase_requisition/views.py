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
from django.utils.dateparse import parse_datetime



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
from pytz import timezone, utc
from datetime import datetime,timedelta,time,date
from django.utils import timezone





# Create your views here.


class RequisitionReadView(ListAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('requisition_map__requisition_no', 'company__company_name', 'purchase_org__name', 'purchase_grp__name' )



    def get_queryset(self):
        try:
            order_by = self.request.query_params.get('order_by', None)
            field_name = self.request.query_params.get('field_name', None)

            if order_by and order_by.lower() == 'desc' and field_name:
                queryset = Requisition.objects.all().order_by('-' + field_name)
            elif order_by and order_by.lower() == 'asc' and field_name:
                queryset = Requisition.objects.all().order_by(field_name)
            else:
                queryset = Requisition.objects.all().order_by('-id')
            return queryset

        except Exception as e:
            raise




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



class RequisitioSearchView(ListAPIView):

    serializer_class = RequisitionReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

    def get_queryset(self):
        queryset = Requisition.objects.all()
        username = self.request.query_params.get('username', None)
        company = self.request.query_params.get('company', None)
        status = self.request.query_params.get('status', None)
        approve=self.request.query_params.get('approve', None)
        from_date=self.request.query_params.get('from_date', None)
        to_date=self.request.query_params.get('to_date', None)
        created_at=self.request.query_params.get('created_at', None)


        if username is not None:
            queryset = queryset.filter(created_by__first_name=username)

        if company is not None:
            queryset = queryset.filter(company_id=company)

        if status is not None:
            queryset = queryset.filter(status=status)

        if approve is not None:
            queryset = queryset.filter(is_approve=approve)

        if created_at is not None:

            created_from_date = datetime.strptime(created_at, "%Y-%m-%d").date()
            created_from_date = datetime.combine(created_from_date, time.min)
            created_from_date = datetime.isoformat(created_from_date)

            created_to_date = datetime.strptime(created_at, "%Y-%m-%d").date()
            created_to_date = datetime.combine(created_to_date, time.max)
            created_to_date = datetime.isoformat(created_to_date)

            queryset = queryset.filter(created_at__gte=created_from_date,created_at__lte=created_to_date)


        if from_date and to_date is not None:

            created_from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
            created_from_date = datetime.combine(created_from_date, time.min)
            created_from_date = datetime.isoformat(created_from_date)

            created_to_date = datetime.strptime(to_date, "%Y-%m-%d").date()
            created_to_date = datetime.combine(created_to_date, time.max)
            created_to_date = datetime.isoformat(created_to_date)

            queryset = queryset.filter(created_at__gte=created_from_date,created_at__lte=created_to_date)

        return queryset







