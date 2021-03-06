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

from stock.serializers import (
    StockSerializer,
    StockReadSerializer,
    StockIssueReadSerializer,
    StockIssueSerializer
)

from django.contrib.auth.models import User
from stock.models import Stock,StockIssue

# Create your views here.

class StockReadView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('company__company_name', 'branch__branch_name', 'storage_location__storage_address', 'storage_bin__bin_no','quantity')

    def get_queryset(self):

        try:
            order_by = self.request.query_params.get('order_by', None)
            field_name = self.request.query_params.get('field_name', None)

            if order_by and order_by.lower() == 'desc' and field_name:
                queryset = Stock.objects.all().order_by('-' + field_name)
            elif order_by and order_by.lower() == 'asc' and field_name:
                queryset = Stock.objects.all().order_by(field_name)
            else:
                queryset = Stock.objects.all().order_by('-id')
            return queryset

        except Exception as e:
            raise


class StocktReadDetailView(RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

class StockIssueCreate(ListCreateAPIView):
    queryset = StockIssue.objects.all()
    serializer_class = StockIssueSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

class SpecificStockIssueView(ListAPIView):

    serializer_class = StockIssueSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

    def get_queryset(self):
        stock=self.kwargs['stock']
        return StockIssue.objects.filter(stock_id=stock)

class StockIssueReadView(ListAPIView):
    queryset = StockIssue.objects.all()
    serializer_class = StockIssueReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination


class StockMatser(ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    authentication_classes = [TokenAuthentication]


class StockUpdate(RetrieveUpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    authentication_classes = [TokenAuthentication]