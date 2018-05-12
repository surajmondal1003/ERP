from salesorg_group.models import SalesOrg,SalesGroup
from company.models import Company
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

class SalesOrgSerializer(ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=SalesOrg.objects.all())]
    )
    status = serializers.BooleanField(default=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SalesOrg
        fields = ['id','name','description','status','created_at','created_by']


class SalesGroupSerializer(ModelSerializer):
    name=serializers.CharField(
        validators=[UniqueValidator(queryset=SalesGroup.objects.all())]
    )
    status = serializers.BooleanField(default=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = SalesGroup
        fields = ['id', 'name', 'description','status','created_at','created_by']