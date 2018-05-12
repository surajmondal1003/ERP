from purchaseorggroup.models import PurchaseOrg,PurchaseGroup,PurchaseOrgMapping
from company.models import Company
from states.models import State
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator,UniqueTogetherValidator
from company_branch.serializers import CompanyBranchSerializer


class PurchaseOrgSerializer(ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=PurchaseOrg.objects.all())]
    )
    status = serializers.BooleanField(default=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PurchaseOrg
        fields = ['id','name','description','status','created_at','created_by']


class PurchaseGroupSerializer(ModelSerializer):
    name=serializers.CharField(
        validators=[UniqueValidator(queryset=PurchaseGroup.objects.all())]
    )
    status = serializers.BooleanField(default=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PurchaseGroup
        fields = ['id', 'name', 'description','status','created_at','created_by']

class PurchaseOrgMappingSerializer(ModelSerializer):

    status = serializers.BooleanField(default=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PurchaseOrgMapping
        fields = ['id', 'pur_org', 'branch','status','created_at','created_by']
        validators = [
            UniqueTogetherValidator(queryset=PurchaseOrgMapping.objects.all(),fields=('pur_org', 'branch'))
        ]



class ChildrenSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CompanyBranchTreeSerializer(ModelSerializer):
    company_branch = CompanyBranchSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id','parent','company_name','status','company_branch']


