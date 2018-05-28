from stock.models import Stock,StockIssue
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from company.serializers import CompanyListSerializer
from authentication.serializers import UserLoginSerializer,UserReadSerializer
from material_master.serializers import MaterialNameSerializer,MaterialReadSerializer,MaterialSerializer
from company_branch.serializers import UOMSerializer,CompanyStorageSerializer,CompanyStorageBinSerializer,CompanyBranchSerializer

class StockSerializer(ModelSerializer):

    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    queryset = Stock.objects.all()
    class Meta:
        model = Stock
        fields = ['id','grn','company','branch','storage_location','storage_bin','material','rate','quantity','created_at','created_by','status']

    def create(self, validated_data):

        stock = Stock.objects.create(**validated_data)

        return stock

    def update(self, instance, validated_data):
        #id = validated_data.get('id', instance.id)
        instance.quantity = validated_data.get("quantity",instance.quantity)
        instance.save()

        return instance



class StockReadSerializer(ModelSerializer):

    #created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    company = CompanyListSerializer()
    branch = CompanyBranchSerializer(read_only=True)
    storage_location = CompanyStorageSerializer(read_only=True)
    storage_bin = CompanyStorageBinSerializer(read_only=True)
    material = MaterialNameSerializer(read_only=True)
    status = serializers.BooleanField(default=True)



    class Meta:
        model = Stock
        fields = ['id','grn_id','company','branch','storage_location','storage_bin','material','rate','quantity','created_at','created_by_id','status']


class StockIssueSerializer(ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)

    class Meta:
        model = StockIssue
        fields = ['id','stock','quantity','note','status','created_at','created_by']



class StockIssueReadSerializer(ModelSerializer):

    #created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)

    class Meta:
        model = StockIssue
        fields = ['id','stock_id','quantity', 'note','created_at','created_by_id','status']


