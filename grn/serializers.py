from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
import datetime

from grn.models import GRN,GRNDetail,GRNMap
from django.contrib.auth.models import User
from vendor.serializers import VendorAddressSerializer
from purchase_order.serializers import PurchaseMapSerializer

from rest_framework.relations import StringRelatedField


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




class GRNReadSerializer(ModelSerializer):

    purchase_order_no=PurchaseMapSerializer(read_only=True,many=True)
    company=StringRelatedField()
    pur_org=StringRelatedField()
    pur_grp=StringRelatedField()
    vendor=StringRelatedField()
    vendor_address=VendorAddressSerializer()
    grn_map=GRNMapSerializer(read_only=True,many=True)

    class Meta:
        model = GRN
        fields = ['id','purchase_order_no','po_order','pur_org','pur_grp','company','vendor','vendor_address','waybill_no','vehicle_no',
                  'check_post','challan_no','challan_date','is_approve','is_finalised','status','created_at',
                  'created_by','grn_detail','grn_map']

