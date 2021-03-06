from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
import datetime

from grn.models import GRN,GRNDetail,GRNMap
from django.contrib.auth.models import User
from vendor.serializers import VendorAddressSerializer
from purchase_order.serializers import (
    PurchaseMapSerializer,
    PurchaseOrderSerializer,
    PurchaseDetailSerializer,
    PurchaseOrderReadSerializer,
    PurchaseOrderReadForGRNSerializer
)


from rest_framework.relations import StringRelatedField
from material_master.serializers import MaterialNameSerializer
from vendor.serializers import VendorNameSerializer
from purchaseorggroup.serializers import PurchaseOrgSerializer,PurchaseGroupSerializer
from company.serializers import CompanyListSerializer
from company_branch.serializers import CompanyBranchSerializer,CompanyStorageBinSerializer,CompanyStorageSerializer,UOMSerializer
from authentication.serializers import UserReadSerializer


class GRNMapSerializer(ModelSerializer):

    class Meta:
        model = GRNMap
        fields = ['id','grn_no']



class GRNDetailSerializer(ModelSerializer):

    class Meta:
        model = GRNDetail
        fields = ['id','material','uom','order_quantity','receive_quantity','company_branch','storage_location',
                  'storage_bin']



class GRNSerializer(ModelSerializer):

    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    grn_detail = GRNDetailSerializer(many=True)


    class Meta:
        model = GRN
        fields = ['id','po_order','pur_org','pur_grp','company','vendor','vendor_address','waybill_no','vehicle_no',
                  'check_post','challan_no','challan_date','is_approve','is_finalised','status','created_at',
                  'created_by','grn_detail']


    def create(self, validated_data):

        grn_detail_data = validated_data.pop('grn_detail')

        grn = GRN.objects.create(**validated_data)

        grn_no = str(datetime.date.today()) + '/GRN-00' + str(grn.id)

        for grn_detail in grn_detail_data:
            GRNDetail.objects.create(grn=grn, **grn_detail)


        GRNMap.objects.create(grn=grn,grn_no=grn_no)


        return grn

    def update(self, instance, validated_data):

            instance.is_approve = validated_data.get('is_approve', instance.is_approve)
            instance.is_finalised = validated_data.get('is_finalised', instance.is_finalised)
            instance.status = validated_data.get('status', instance.status)

            instance.save()

            return instance




class GRNDetailReadSerializer(ModelSerializer):
    material = MaterialNameSerializer(read_only=True)
    company_branch = CompanyBranchSerializer(read_only=True)
    storage_location = CompanyStorageSerializer(read_only=True)
    storage_bin = CompanyStorageBinSerializer(read_only=True)
    uom = UOMSerializer(read_only=True)

    class Meta:
        model = GRNDetail
        fields = ['id','material','uom','order_quantity','receive_quantity','company_branch','storage_location',
                  'storage_bin']




class GRNReadSerializer(ModelSerializer):

    purchase_order_no=PurchaseMapSerializer(read_only=True,many=True)
    po_order=PurchaseOrderReadForGRNSerializer(read_only=True)
    company=CompanyListSerializer()
    pur_org=PurchaseOrgSerializer()
    pur_grp=PurchaseGroupSerializer()
    vendor=VendorNameSerializer(read_only=True)
    vendor_address=VendorAddressSerializer()
    grn_map=GRNMapSerializer(read_only=True,many=True)
    grn_detail = GRNDetailReadSerializer(many=True)
    created_by = UserReadSerializer()


    class Meta:
        model = GRN
        fields = ['id','purchase_order_no','po_order','pur_org','pur_grp','company','vendor','vendor_address','waybill_no','vehicle_no',
                  'check_post','challan_no','challan_date','is_approve','is_finalised','status','created_at',
                  'created_by','is_deleted','grn_detail','grn_map']




class GRNCreateBySerializer(ModelSerializer):
    created_by = UserReadSerializer()

    class Meta:
        model = GRN
        fields = ['id','created_at','created_by']




class GRNUpdateStatusSerializer(ModelSerializer):

    class Meta:
        model = GRN
        fields = ['id','status','is_approve','is_finalised','is_deleted']


    def update(self, instance, validated_data):
            instance.is_approve = validated_data.get('is_approve', instance.is_approve)
            instance.is_finalised = validated_data.get('is_finalised', instance.is_finalised)
            instance.status = validated_data.get('status', instance.status)
            instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
            instance.save()

            return instance