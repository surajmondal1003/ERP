from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from purchase_requisition.models import RequisitionDetail,Requisition,RequisitionMap
from django.contrib.auth.models import User
import datetime
from company.serializers import CompanyListSerializer
from purchaseorggroup.serializers import PurchaseGroupSerializer,PurchaseOrgSerializer
from authentication.serializers import UserLoginSerializer,UserReadSerializer
from material_master.serializers import MaterialNameSerializer,MaterialReadSerializer,MaterialSerializer
from company_branch.serializers import UOMSerializer,CompanyStorageSerializer,CompanyStorageBinSerializer,CompanyBranchSerializer
from rest_framework.relations import StringRelatedField,PrimaryKeyRelatedField





class RequisitionDetailSerializer(ModelSerializer):

    #created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)

    class Meta:
        model = RequisitionDetail
        fields = ['id','material','quantity','uom','branch','storage_location','storage_bin','status']


class RequisitionMapSerializer(ModelSerializer):


    class Meta:
        model = RequisitionMap
        fields = ['id','requisition_no']




class RequisitionSerializer(ModelSerializer):
    requisition_detail=RequisitionDetailSerializer(many=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    # is_approve = serializers.BooleanField(default=False)
    # is_finalised = serializers.BooleanField(default=False)

    class Meta:
        model = Requisition
        fields = ['id','company','purchase_org','purchase_grp','special_note','is_approve','is_finalised','status','created_at','created_by',
                  'requisition_detail']

    def create(self, validated_data):

            requisitions_data = validated_data.pop('requisition_detail')


            requisition = Requisition.objects.create(**validated_data)


            requisition_no=str(datetime.date.today())+'/I-00'+str(requisition.id)
            print(requisition_no)

            for requisition_data in requisitions_data:
                RequisitionDetail.objects.create(requisition=requisition,**requisition_data)

            RequisitionMap.objects.create(requisition=requisition,requisition_no=requisition_no)


            return requisition

    def update(self, instance, validated_data):
            requisitions_data = validated_data.pop('requisition_detail')

            instance.is_approve = validated_data.get('is_approve', instance.is_approve)
            instance.is_finalised = validated_data.get('is_finalised', instance.is_finalised)
            instance.status = validated_data.get('status', instance.status)

            instance.save()

            return instance




class RequisitionDetailReadSerializer(ModelSerializer):

    #created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    material=MaterialNameSerializer(read_only=True)
    uom=UOMSerializer(read_only=True)
    branch=CompanyBranchSerializer(read_only=True)
    storage_location=CompanyStorageSerializer(read_only=True)
    storage_bin=CompanyStorageBinSerializer(read_only=True)

    class Meta:
        model = RequisitionDetail
        fields = ['id','material','quantity','uom','branch','storage_location','storage_bin','status']


class RequisitionReadSerializer(ModelSerializer):

    requisition_detail=RequisitionDetailReadSerializer(many=True)
    requisition_map=RequisitionMapSerializer(many=True)
    company=CompanyListSerializer()
    purchase_org=PurchaseOrgSerializer()
    purchase_grp=PurchaseGroupSerializer()
    created_by=UserReadSerializer()


    class Meta:
        model = Requisition
        fields = ['id','company','purchase_org','purchase_grp','special_note','is_approve','is_finalised','status','created_at','created_by',
                  'requisition_detail','requisition_map']




