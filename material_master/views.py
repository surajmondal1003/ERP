from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from authentication.pagination import ErpLimitOffestpagination, ErpPageNumberPagination
from django_filters.rest_framework import filters
from rest_framework import filters


from material_master.serializers import (
    MaterialTypeSerializer,
    MaterialSerializer,
    MaterialWithoutTaxSalesSerializer,
    MaterialReadSerializer

)
from django.contrib.auth.models import User
from material_master.models import MaterialType,Material,Material_Tax,Material_UOM

from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.
class MaterialTypeViewSet(viewsets.ModelViewSet):
    queryset = MaterialType.objects.all()
    serializer_class =MaterialTypeSerializer
    #permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination


class MaterialMasterCreate(APIView):
    """
    Creates the user.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request, format='json'):
        is_taxable = request.data.get('is_taxable')
        is_sales = request.data.get('is_sales')


        if is_taxable=='true' and is_sales=='true':

            material_serializer = MaterialSerializer(data=request.data)

        else:
            material_serializer = MaterialWithoutTaxSalesSerializer(data=request.data)
            if material_serializer.is_valid():
                material=material_serializer.save()

                if material:
                    return Response({'message':'Success','status':status.HTTP_201_CREATED})

            return Response(material_serializer.errors, status=status.HTTP_400_BAD_REQUEST)






    # def get(self, request, format=None):
    #
    #     materials=Material.objects.all()
    #     for material in materials:
    #         print(material.material_fullname)
    #
    #     material_serializer=MaterialReadSerializer(materials,context={"request": request})
    #
    #     return Response('Sucess',material_serializer.data,status=status.HTTP_200_OK)




class MaterialMasterUpdate(RetrieveUpdateDestroyAPIView):

    #queryset = Material_Tax.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = ('material')

    def get_queryset(self):
        material = self.kwargs['material']
        return Material_Tax.objects.filter(material=material)
    def get(self, request, *args, **kwargs):
        material_details = self.get_queryset()
        for material_detail in material_details:
            print(material_detail.material.material_fullname)

        return Response({'message':'Sucess', 'status': status.HTTP_200_OK})

    def put(self, request, *args, **kwargs):
        material = self.kwargs['material']

        is_taxable = request.data.get('is_taxable')
        is_sales = request.data.get('is_sales')

        if is_taxable =='false':
            material_tax_details = Material_Tax.objects.filter(material=material)
            material_tax_details.delete()
        if is_sales=='false':
            material_uom_details = Material_UOM.objects.filter(material=material,material_for=2)
            material_uom_details.delete()
            material_tax_details = Material_Tax.objects.filter(material=material,tax_for=2)
            material_tax_details.delete()

        if is_taxable == 'true' and is_sales == 'true':
            material_master = Material.objects.get(id=material)
            material_serializer = MaterialSerializer(instance=material_master,data=request.data)

        else:
            material_master=Material.objects.get(id=material)
            material_serializer = MaterialWithoutTaxSalesSerializer(instance=material_master,data=request.data)
            if material_serializer.is_valid():
                material = material_serializer.update(instance=material_master,validated_data=request.data)

                if material:
                    return Response({'message': 'Success', 'status': status.HTTP_201_CREATED})

            return Response(material_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Sucess', 'status': status.HTTP_200_OK})




class MaterialReadView(ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialReadSerializer
    # permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [TokenAuthentication]
    pagination_class = ErpPageNumberPagination








