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

from company_branch.serializers import (
    CompanyBranchSerializer,
    CompanyStorageSerializer,
    UOMSerializer,
    CompanyStorageBinSerializer

)
from django.contrib.auth.models import User
from company.models import Company
from company_branch.models import CompanyBranch,StorageLocation,UOM,StorageBin
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import filters
from rest_framework import filters


# Create your views here.
class CompanyBranchViewSet(viewsets.ModelViewSet):
    queryset = CompanyBranch.objects.all()
    serializer_class =CompanyBranchSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('branch_name',)




class SpecificCompanyBranchView(ListAPIView):

    serializer_class = CompanyBranchSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

    def get_queryset(self):
        company=self.kwargs['company']
        return CompanyBranch.objects.filter(company_id=company)



class CompanyStorageViewSet(viewsets.ModelViewSet):
    queryset = StorageLocation.objects.all()
    serializer_class =CompanyStorageSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination



class SpecificCompanyStorageView(ListAPIView):

    serializer_class = CompanyStorageSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

    def get_queryset(self):
        company=self.kwargs['company']
        return StorageLocation.objects.filter(company_id=company)



class UOMViewSet(viewsets.ModelViewSet):
    queryset = UOM.objects.all()
    serializer_class =UOMSerializer
    #permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

class CompanyStorageBinViewSet(viewsets.ModelViewSet):
    queryset = StorageBin.objects.all()
    serializer_class =CompanyStorageBinSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

class SpecificCompanyStorageBinView(ListAPIView):

    serializer_class = CompanyStorageBinSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

    def get_queryset(self):
        company=self.kwargs['company']
        return StorageBin.objects.filter(company_id=company)




class SpecificCompanyBranchDropdown(ListAPIView):

    serializer_class = CompanyBranchSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]


    def get_queryset(self):
        company=self.kwargs['company']
        return CompanyBranch.objects.filter(company_id=company,status=True)



class SpecificCompanyStorageDropdown(ListAPIView):

    serializer_class = CompanyStorageSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]


    def get_queryset(self):
        company=self.kwargs['company']
        return StorageLocation.objects.filter(company_id=company,status=True)


class SpecificCompanyStorageBinDropdown(ListAPIView):

    serializer_class = CompanyStorageBinSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]


    def get_queryset(self):
        company=self.kwargs['company']
        return StorageBin.objects.filter(company_id=company,status=True)

