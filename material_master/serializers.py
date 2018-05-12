from material_master.models import MaterialType,Material,Material_UOM,MaterialPurchaseOrg,MaterialPurchaseGroup,Material_Tax
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

class MaterialTypeSerializer(ModelSerializer):
    material_type = serializers.CharField(validators=[UniqueValidator(queryset=MaterialType.objects.all())])
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)

    class Meta:
        model = MaterialType
        fields = ['id','material_type','status','created_at','created_by']


class MaterialUOMSerializer(ModelSerializer):

    class Meta:
        model = Material_UOM
        fields = ['material_for','base_uom','unit_per_uom','unit_uom']



class MaterialTaxSerializer(ModelSerializer):

    class Meta:
        model = Material_Tax
        fields = ['tax_for','igst','cgst','sgst','hsn']


class MaterialPurchaseOrgSerializer(ModelSerializer):

    class Meta:
        model = MaterialPurchaseOrg
        fields = ['pur_org']

class MaterialPurchaseGrpSerializer(ModelSerializer):

    class Meta:
        model = MaterialPurchaseGroup
        fields = ['pur_group']



class MaterialSerializer(ModelSerializer):

    #created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    material_uom=MaterialUOMSerializer(many=True)
    material_tax=MaterialTaxSerializer(many=True)
    material_pur_org=MaterialPurchaseOrgSerializer()
    material_pur_grp=MaterialPurchaseGrpSerializer()

    class Meta:
        model = Material
        fields = ['id','material_fullname','material_type','material_code','description','is_taxable','is_sales','status','created_at',
                  'material_uom','material_tax','material_pur_org','material_pur_grp']

    def create(self, validated_data):
        material_uoms=validated_data.pop('material_uom')
        material_taxs=validated_data.pop('material_tax')
        material_pur_orgs=validated_data.pop('material_pur_org')
        material_pur_grps=validated_data.pop('material_pur_grp')

        material=Material.objects.create(**validated_data)

        for material_uom in material_uoms:
            Material_UOM.objects.create(material=material,**material_uom)
        for material_tax in material_taxs:
            Material_Tax.objects.create(material=material,**material_tax)
        for material_pur_org in material_pur_orgs:
            MaterialPurchaseOrg.objects.create(material=material,**material_pur_org)
        for material_pur_grp in material_pur_grps:
            MaterialPurchaseGroup.objects.create(material=material,**material_pur_grp)

        return material

    def update(self, instance, validated_data):
        material_uoms = validated_data.pop('material_uom')
        material_taxs = validated_data.pop('material_tax')
        material_pur_orgs = validated_data.pop('material_pur_org')
        material_pur_grps = validated_data.pop('material_pur_grp')

        material = Material.objects.save(instance,**validated_data)

        for material_uom in material_uoms:
            Material_UOM.objects.create(material=instance,**material_uom)
        for material_tax in material_taxs:
            Material_Tax.objects.create(material=instance,**material_tax)
        for material_pur_org in material_pur_orgs:
            MaterialPurchaseOrg.objects.create(material=instance,**material_pur_org)
        for material_pur_grp in material_pur_grps:
            MaterialPurchaseGroup.objects.create(material=instance,**material_pur_grp)

        return material




class MaterialWithoutTaxSalesSerializer(ModelSerializer):

    #created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    material_uom=MaterialUOMSerializer()
    material_pur_org=MaterialPurchaseOrgSerializer()
    material_pur_grp=MaterialPurchaseGrpSerializer()

    class Meta:
        model = Material
        fields = ['id','material_fullname','material_type','material_code','description','is_taxable','is_sales','status','created_at',
                  'material_uom','material_pur_org','material_pur_grp']

    def create(self, validated_data):
        material_uoms=validated_data.pop('material_uom')
        material_pur_orgs=validated_data.pop('material_pur_org')
        material_pur_grps=validated_data.pop('material_pur_grp')

        material=Material.objects.create(**validated_data)

        for material_uom in material_uoms:
            Material_UOM.objects.create(material=material,**material_uom)
        for material_pur_org in material_pur_orgs:
            MaterialPurchaseOrg.objects.create(material=material,**material_pur_org)
        for material_pur_grp in material_pur_grps:
            MaterialPurchaseGroup.objects.create(material=material,**material_pur_grp)

        return material




class MaterialReadSerializer(ModelSerializer):


    class Meta:
        model = Material
        fields = ['id','material_fullname','material_type','material_code','description','is_taxable','is_sales','status','created_at'
                  ]




