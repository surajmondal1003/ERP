from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from company_branch.serializers import UOMSerializer
import datetime

from payment.models import Payment,PaymentMap
from django.contrib.auth.models import User
from grn.serializers import GRNMapSerializer,GRNDetailReadSerializer,GRNReadSerializer,GRNCreateBySerializer
from purchase_order.serializers import PurchaseMapSerializer
from company.serializers import CompanyListSerializer
from vendor.serializers import VendorAddressSerializer,VendorNameSerializer
from authentication.serializers import UserReadSerializer
from banks.serializers import BankSerializer




class PaymentMapSerializer(ModelSerializer):

    class Meta:
        model = PaymentMap
        fields = ['id','payment_no']



class PaymentSerializer(ModelSerializer):

    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)



    class Meta:
        model = Payment
        fields = ['id','company','pur_inv','vendor','vendor_address','purchase_inv_no','purchase_inv_date','po_order','po_order_no','bank','payment_mode',
                  'payment_refrence','total_amount','special_note','is_approve','status','created_at',
                  'created_by']



    def create(self, validated_data):



        payment = Payment.objects.create(**validated_data)

        payment_no = str(datetime.date.today()) + '/PAY-00' + str(payment.id)

        PaymentMap.objects.create(payment=payment,payment_no=payment_no)


        return payment




class PaymentReadSerializer(ModelSerializer):



    company = CompanyListSerializer()
    vendor = VendorNameSerializer(read_only=True)
    vendor_address = VendorAddressSerializer(read_only=True)
    created_by = UserReadSerializer()
    bank=BankSerializer()
    payment_map=PaymentMapSerializer(read_only=True,many=True)

    class Meta:
        model = Payment
        fields = ['id','company','pur_inv','vendor','vendor_address','purchase_inv_no','purchase_inv_date','po_order','po_order_no','bank','payment_mode',
                  'payment_refrence','total_amount','special_note','is_approve','status','created_at',
                  'created_by','payment_map']
