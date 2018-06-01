from material_master.models import MaterialType,Material,Material_UOM,MaterialPurchaseOrg,MaterialPurchaseGroup,Material_Tax
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from company_branch.serializers import UOMSerializer

class MaterialTypeSerializer(ModelSerializer):
    material_type = serializers.CharField(validators=[UniqueValidator(queryset=MaterialType.objects.all())])
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)

    class Meta:
        model = MaterialType
        fields = ['id','material_type','status','created_at','created_by']


class MaterialUOMSerializer(ModelSerializer):
    #base_uom = UOMSerializer()
    #unit_uom = UOMSerializer()

    class Meta:
        model = Material_UOM
        fields = ['id','material_for','base_uom','unit_per_uom','unit_uom','is_deleted']

class MaterialUOMSerializerforRead(ModelSerializer):
    base_uom = UOMSerializer()
    unit_uom = UOMSerializer()

    class Meta:
        model = Material_UOM
        fields = ['id','material_for','base_uom','unit_per_uom','unit_uom','is_deleted']



class MaterialTaxSerializer(ModelSerializer):

    class Meta:
        model = Material_Tax
        fields = ['id','tax_for','igst','cgst','sgst','hsn','is_deleted']


class MaterialPurchaseOrgSerializer(ModelSerializer):

    class Meta:
        model = MaterialPurchaseOrg
        fields = ['id','pur_org','is_deleted']

class MaterialPurchaseGrpSerializer(ModelSerializer):

    class Meta:
        model = MaterialPurchaseGroup
        fields = ['id','pur_group','is_deleted']




# class MaterialWithoutTaxSalesSerializer(ModelSerializer):
#
#     #created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     status = serializers.BooleanField(default=True)
#     material_uom=MaterialUOMSerializer()
#     material_pur_org=MaterialPurchaseOrgSerializer()
#     material_pur_grp=MaterialPurchaseGrpSerializer()
#
#     class Meta:
#         model = Material
#         fields = ['id','material_fullname','material_type','material_code','description','is_taxable','is_sales','status','created_at',
#                   'material_uom','material_pur_org','material_pur_grp']
#
#     def create(self, validated_data):
#         material_uoms=validated_data.pop('material_uom')
#         material_pur_orgs=validated_data.pop('material_pur_org')
#         material_pur_grps=validated_data.pop('material_pur_grp')
#
#         material=Material.objects.create(**validated_data)
#
#         for material_uom in material_uoms:
#             Material_UOM.objects.create(material=material,**material_uom)
#         for material_pur_org in material_pur_orgs:
#             MaterialPurchaseOrg.objects.create(material=material,**material_pur_org)
#         for material_pur_grp in material_pur_grps:
#             MaterialPurchaseGroup.objects.create(material=material,**material_pur_grp)
#
#         return material




class MaterialReadSerializer(ModelSerializer):
    material_type = MaterialTypeSerializer()
    material_uom = MaterialUOMSerializerforRead(many=True)
    material_tax = MaterialTaxSerializer(many=True)
    material_purchase_org = MaterialPurchaseOrgSerializer(many=True)
    material_purchase_grp = MaterialPurchaseGrpSerializer(many=True)

    class Meta:
        model = Material
        fields = ['id','material_fullname','material_type','material_code','description','is_taxable','is_sales','status','created_at',
                  'is_deleted','material_uom', 'material_tax','material_purchase_org','material_purchase_grp']







class MaterialSerializer(ModelSerializer):

    #created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    material_uom = MaterialUOMSerializer(many=True)
    material_tax = MaterialTaxSerializer(many=True)
    material_purchase_org = MaterialPurchaseOrgSerializer(many=True)
    material_purchase_grp = MaterialPurchaseGrpSerializer(many=True)

    class Meta:
        model = Material
        fields = ['id','material_fullname','material_type','material_code','description','is_taxable','is_sales','status','created_at',
                  'is_deleted','material_uom','material_tax','material_purchase_org','material_purchase_grp']

    def create(self, validated_data):
        is_taxable = validated_data.get('is_taxable')
        print(is_taxable)

        if is_taxable == True:

            material_uoms = validated_data.pop('material_uom')
            material_taxs = validated_data.pop('material_tax')
            material_pur_orgs = validated_data.pop('material_purchase_org')
            material_pur_grps = validated_data.pop('material_purchase_grp')

            material = Material.objects.create(**validated_data)

            for material_uom in material_uoms:
                Material_UOM.objects.create(material=material, **material_uom)
            for material_tax in material_taxs:
                Material_Tax.objects.create(material=material, **material_tax)
            for material_pur_org in material_pur_orgs:
                MaterialPurchaseOrg.objects.create(material=material, **material_pur_org)
            for material_pur_grp in material_pur_grps:
                MaterialPurchaseGroup.objects.create(material=material, **material_pur_grp)

            return material

        else:
            material_uoms = validated_data.pop('material_uom')
            material_taxs = validated_data.pop('material_tax')
            material_pur_orgs = validated_data.pop('material_purchase_org')
            material_pur_grps = validated_data.pop('material_purchase_grp')

            material = Material.objects.create(**validated_data)

            for material_uom in material_uoms:
                Material_UOM.objects.create(material=material, **material_uom)
            for material_pur_org in material_pur_orgs:
                MaterialPurchaseOrg.objects.create(material=material, **material_pur_org)
            for material_pur_grp in material_pur_grps:
                MaterialPurchaseGroup.objects.create(material=material, **material_pur_grp)

            return material

    def update(self, instance, validated_data):
        is_taxable = validated_data.get('is_taxable')
        print(is_taxable)

        if is_taxable == True:
            material_uoms_data = validated_data.pop('material_uom')
            material_taxs_data = validated_data.pop('material_tax')
            material_pur_orgs_data = validated_data.pop('material_purchase_org')
            material_pur_grps_data = validated_data.pop('material_purchase_grp')

            material_uoms = (instance.material_uom).all()
            material_uoms = list(material_uoms)
            material_taxs = (instance.material_tax).all()
            material_taxs = list(material_taxs)
            material_pur_orgs = (instance.material_purchase_org).all()
            material_pur_orgs = list(material_pur_orgs)
            material_pur_grps = (instance.material_purchase_grp).all()
            material_pur_grps = list(material_pur_grps)

            instance.material_fullname = validated_data.get('material_fullname', instance.material_fullname)
            instance.material_type = validated_data.get('material_type', instance.material_type)
            instance.material_code = validated_data.get('material_code', instance.material_code)
            instance.description = validated_data.get('description', instance.description)
            instance.is_taxable = validated_data.get('is_taxable', instance.is_taxable)
            instance.is_sales = validated_data.get('is_sales', instance.is_sales)
            instance.status = validated_data.get('status', instance.status)
            instance.created_at = validated_data.get('created_at', instance.created_at)
            instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
            instance.save()

            print(instance)

            for material_uom in material_uoms:
                if material_uom:
                    print(material_uom)
                    material_uom.delete()
            for material_tax in material_taxs:
                if material_tax:
                    print(material_tax)
                    material_tax.delete()
            for material_pur_org in material_pur_orgs:
                if material_pur_org:
                    material_pur_org.delete()
            for material_pur_grp in material_pur_grps:
                if material_pur_grp:
                    material_pur_grp.delete()

            for material_uom in material_uoms_data:
                Material_UOM.objects.create(material=instance, **material_uom)
            for material_tax in material_taxs_data:
                Material_Tax.objects.create(material=instance, **material_tax)
            for material_pur_org in material_pur_orgs_data:
                MaterialPurchaseOrg.objects.create(material=instance, **material_pur_org)
            for material_pur_grp in material_pur_grps_data:
                MaterialPurchaseGroup.objects.create(material=instance, **material_pur_grp)

            return instance

        else:
            material_uoms_data = validated_data.pop('material_uom')
            material_taxs_data = validated_data.pop('material_tax')
            material_pur_orgs_data = validated_data.pop('material_purchase_org')
            material_pur_grps_data = validated_data.pop('material_purchase_grp')

            material_uoms = (instance.material_uom).all()
            material_uoms = list(material_uoms)
            material_taxs = (instance.material_tax).all()
            material_taxs = list(material_taxs)
            material_pur_orgs = (instance.material_purchase_org).all()
            material_pur_orgs = list(material_pur_orgs)
            material_pur_grps = (instance.material_purchase_grp).all()
            material_pur_grps = list(material_pur_grps)

            instance.material_fullname = validated_data.get('material_fullname', instance.material_fullname)
            instance.material_type = validated_data.get('material_type', instance.material_type)
            instance.material_code = validated_data.get('material_code', instance.material_code)
            instance.description = validated_data.get('description', instance.description)
            instance.is_taxable = validated_data.get('is_taxable', instance.is_taxable)
            instance.is_sales = validated_data.get('is_sales', instance.is_sales)
            instance.status = validated_data.get('status', instance.status)
            instance.created_at = validated_data.get('created_at', instance.created_at)
            instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
            instance.save()

            print(instance)

            for material_uom in material_uoms:
                if material_uom:
                    print(material_uom)
                    material_uom.delete()
            for material_tax in material_taxs:
                if material_tax:
                    print(material_tax)
                    material_tax.delete()
            for material_pur_org in material_pur_orgs:
                if material_pur_org:
                    material_pur_org.delete()
            for material_pur_grp in material_pur_grps:
                if material_pur_grp:
                    material_pur_grp.delete()

            for material_uom in material_uoms_data:
                Material_UOM.objects.create(material=instance, **material_uom)
            for material_pur_org in material_pur_orgs_data:
                MaterialPurchaseOrg.objects.create(material=instance, **material_pur_org)
            for material_pur_grp in material_pur_grps_data:
                MaterialPurchaseGroup.objects.create(material=instance, **material_pur_grp)

            return instance



class MaterialNameSerializer(ModelSerializer):
    material_tax = MaterialTaxSerializer(many=True)

    class Meta:
        model = Material
        fields = ['id','material_fullname','material_code','material_tax']