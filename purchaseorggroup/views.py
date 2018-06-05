from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,GenericAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.mixins import ListModelMixin,DestroyModelMixin
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from authentication.pagination import ErpLimitOffestpagination, ErpPageNumberPagination

from purchaseorggroup.serializers import (
    PurchaseOrgSerializer,
    PurchaseGroupSerializer,
    PurchaseOrgMappingSerializer,
    CompanyBranchTreeSerializer

)
from django.contrib.auth.models import User
from purchaseorggroup.models import PurchaseGroup,PurchaseOrg,PurchaseOrgMapping
from company.models import Company
from rest_framework import filters


# Create your views here.
class PurchaseOrgViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrg.objects.all()
    serializer_class =PurchaseOrgSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','description')


class PurchaseGroupViewSet(viewsets.ModelViewSet):
    queryset = PurchaseGroup.objects.all()
    serializer_class =PurchaseGroupSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class PurchaseOrgMappingViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrgMapping.objects.all()
    serializer_class = PurchaseOrgMappingSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination


class SpecificPurchaseOrgMappingView(ListAPIView):
    serializer_class = PurchaseOrgMappingSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

    def get_queryset(self):
        organisation = self.kwargs['organisation']
        return PurchaseOrgMapping.objects.filter(pur_org=organisation)


class DeletePurchaseOrgMappingView(DestroyAPIView):
    queryset = PurchaseOrgMapping.objects.all()
    serializer_class = PurchaseOrgMappingSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination
    lookup_field = ('pur_org')

    def get_queryset(self):
        pur_org = self.kwargs['pur_org']
        return PurchaseOrgMapping.objects.filter(pur_org=pur_org)


    def destroy(self, request, *args, **kwargs):
        pur_org = self.get_queryset()
        for record in pur_org:
             self.perform_destroy(record)

        return Response({'msg':'Sucess','status':status.HTTP_200_OK})




class CompanyBranchTreeView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyBranchTreeSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination



class PurchaseOrgCheckList(ListAPIView):
    queryset = PurchaseOrg.objects.filter(status=True)
    serializer_class = PurchaseOrgSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]

class PurchaseGroupCheckList(ListAPIView):
    queryset = PurchaseGroup.objects.filter(status=True)
    serializer_class = PurchaseGroupSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]







# class CompanyBranchTreeView(ListAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanyBranchTreeSerializer
#     #permission_classes = [IsAuthenticated,IsAdminUser]
#     authentication_classes = [TokenAuthentication]
#     pagination_class = ErpPageNumberPagination
#
#     def get_queryset(self):
#         organization=self.kwargs['organization']
#         return Company.objects.filter(company_branch__purchaseorgmapping__pur_org=organization)
#









