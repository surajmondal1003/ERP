from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from company_branch.serializers import UOMSerializer
import datetime

from purchase_invoice.models import PurchaseInvoice,PurchaseInvoiceDetail,PurchaseInvoiceMap
from django.contrib.auth.models import User


class PurchaseInvoiceMapSerializer(ModelSerializer):

    class Meta:
        model = PurchaseInvoiceMap
        fields = ['id','purchase_inv_no']




class PurchaseInvoiceDetailSerializer(ModelSerializer):

    class Meta:
        model = PurchaseInvoiceDetail
        fields = ['id','material','rate','quantity','discount_per','discount_amount','igst',
                  'cgst', 'sgst', 'total_gst', 'material_value', 'material_amount_pay']




class PurchaseInvoiceSerializer(ModelSerializer):

    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    pur_invoice_detail = PurchaseInvoiceDetailSerializer(many=True)


    class Meta:
        model = PurchaseInvoice
        fields = ['id','grn','po_order','pur_org','pur_grp','total_gst','total_amount','vendor','vendor_address',
                  'company','is_approve','is_finalised','status','created_at','created_by',
                  'pur_invoice_detail']


    def create(self, validated_data):

        purchase_invoice_detail_data = validated_data.pop('pur_invoice_detail')

        po_invoice = PurchaseInvoice.objects.create(**validated_data)

        purchase_invoice_no = str(datetime.date.today()) + '/INV-00' + str(po_invoice.id)

        for purchase_invoice_detail in purchase_invoice_detail_data:
            PurchaseInvoiceDetail.objects.create(pur_invoice=po_invoice, **purchase_invoice_detail)


        PurchaseInvoiceMap.objects.create(pur_invoice=po_invoice, purchase_inv_no=purchase_invoice_no)


        return po_invoice



