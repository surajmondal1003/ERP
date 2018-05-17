from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from vendor.models import VendorType,Vendor,VendorAccount,VendorAddress

class VendorTypeSerializer(ModelSerializer):
    vendor_type = serializers.CharField(validators=[UniqueValidator(queryset=VendorType.objects.all())])
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)

    class Meta:
        model = VendorType
        fields = ['id','vendor_type','status','created_at','created_by']


class VendorAddressSerializer(ModelSerializer):


    class Meta:
        model = VendorAddress
        fields = ['id','address','state','city','pincode','mobile','email','designation','contact_person']


class VendorAccountSerializer(ModelSerializer):
    class Meta:
        model = VendorAccount
        fields = ['id', 'bank_name', 'branch_name', 'account_no', 'ifsc_code']




class VendorSerializer(ModelSerializer):

    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    vendor_address = VendorAddressSerializer(many=True)
    vendor_account = VendorAccountSerializer(many=True)


    class Meta:
        model = Vendor
        fields = ['id','vendor_fullname','vendor_type','company','pan_no','gst_no','cin_no','status','created_at','created_by',
                  'vendor_address','vendor_account']

    def create(self, validated_data):

            vendor_address_data = validated_data.pop('vendor_address')
            vendor_account_data = validated_data.pop('vendor_account')


            vendor = Vendor.objects.create(**validated_data)

            for vendor_address in vendor_address_data:
                VendorAddress.objects.create(vendor=vendor, **vendor_address)
            for vendor_account in vendor_account_data:
                VendorAccount.objects.create(vendor=vendor, **vendor_account)


            return vendor

    def update(self, instance, validated_data):

            vendor_address_data = validated_data.pop('vendor_address')
            vendor_account_data = validated_data.pop('vendor_account')

            vendor_addresses = (instance.vendor_address).all()
            vendor_addresses = list(vendor_addresses)
            vendor_accounts = (instance.vendor_account).all()
            vendor_accounts = list(vendor_accounts)


            instance.vendor_fullname = validated_data.get('vendor_fullname', instance.vendor_fullname)
            instance.vendor_type = validated_data.get('vendor_type', instance.vendor_type)
            instance.company = validated_data.get('company', instance.company)
            instance.pan_no = validated_data.get('pan_no', instance.pan_no)
            instance.gst_no = validated_data.get('gst_no', instance.gst_no)
            instance.cin_no = validated_data.get('cin_no', instance.cin_no)
            instance.status = validated_data.get('status', instance.status)
            instance.created_at = validated_data.get('created_at', instance.created_at)
            instance.created_by = validated_data.get('created_by', instance.created_by)
            instance.save()

            print(instance)

            for vendor_address in vendor_addresses:
                if vendor_address:
                    vendor_address.delete()
            for vendor_account in vendor_accounts:
                if vendor_account:
                    vendor_account.delete()


            for vendor_address in vendor_address_data:
                VendorAddress.objects.create(vendor=instance, **vendor_address)
            for vendor_account in vendor_account_data:
                VendorAccount.objects.create(vendor=instance, **vendor_account)


            return instance




