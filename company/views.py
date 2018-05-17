from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView,ListAPIView
from rest_framework import viewsets, status
from company.models import Company,TermsandConditon
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from authentication.pagination import ErpLimitOffestpagination, ErpPageNumberPagination

from company.serializers import (
    CompanySerializer,
    CompanyListSerializer,
    TermsAndConditionSerializer

)


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class =CompanySerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination

    def list(self, request, *args, **kwargs):
        queryset = Company.objects.filter(parent=None)
        serializer = CompanySerializer(queryset,many=True)
        return Response(serializer.data)


class CompanyListView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    #permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [TokenAuthentication]


class TermsAndConditionsViewSet(viewsets.ModelViewSet):
    queryset = TermsandConditon.objects.all()
    serializer_class =TermsAndConditionSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination


class TermsAndConditionsDropdown(ListAPIView):
    queryset = TermsandConditon.objects.all()
    serializer_class =TermsAndConditionSerializer
    #permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]





class PurchaseOrganisationSpecificCompanyList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    #authentication_classes = [TokenAuthentication]
    lookup_field = ('org_id')

    def get_queryset(self):
        org_id = self.kwargs['org_id']
        return Company.objects.filter(company_branch__purchaseorgmapping__pur_org_id=org_id)




