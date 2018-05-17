from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView,RetrieveAPIView
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
    GRNReadSerializer

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
