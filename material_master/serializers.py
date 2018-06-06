from material_master.models import MaterialType,Material,Material_UOM,MaterialPurchaseOrg,MaterialPurchaseGroup,Material_Tax
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from company_branch.serializers import UOMSerializer

class MaterialTypeSerializer(ModelSerializer):
    material_type = serializers.CharField(validators=[UniqueValidator(queryset=MaterialType.objects.all())])
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    description=serializers.CharField(required=False,allow_null=True,allow_blank=True)

    class Meta:
        model = MaterialType
        fields = ['id','material_type','description','status','created_at','created_by']


class MaterialUOMSerializer(ModelSerializer):
    #base_uom = UOMSerializer()
    #unit_uom = UOMSerializer()
    id = serializers.ModelField(model_field=Material_UOM()._meta.get_field('id'), required=False,
                                allow_null=True)

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
    id = serializers.ModelField(model_field=Material_Tax()._meta.get_field('id'), required=False,
                                allow_null=True)

    class Meta:
        model = Material_Tax
        fields = ['id','tax_for','igst','cgst','sgst','hsn','is_deleted']


class MaterialPurchaseOrgSerializer(ModelSerializer):
    id = serializers.ModelField(model_field=MaterialPurchaseOrg()._meta.get_field('id'), required=False,
                                allow_null=True)

    class Meta:
        model = MaterialPurchaseOrg
        fields = ['id','pur_org','is_deleted']

class MaterialPurchaseGrpSerializer(ModelSerializer):
    id = serializers.ModelField(model_field=MaterialPurchaseGroup()._meta.get_field('id'), required=False, allow_null=True)

    class Meta:
        model = MaterialPurchaseGroup
        fields = ['id','pur_group','is_deleted']




# class MaterialReadSerializer(ModelSerializer):
#     material_type = MaterialTypeSerializer()
#     material_uom = MaterialUOMSerializerforRead(many=True)
#     material_tax = MaterialTaxSerializer(many=True)
#     material_purchase_org = MaterialPurchaseOrgSerializer(many=True)
#     material_purchase_grp = MaterialPurchaseGrpSerializer(many=True)
#
#     class Meta:
#         model = Material
#         fields = ['id','material_fullname','material_type','material_code','description','is_taxable','is_sales','status','created_at',
#                   'is_deleted','material_uom', 'material_tax','material_purchase_org','material_purchase_grp']


class MaterialReadSerializer(ModelSerializer):
    material_type = MaterialTypeSerializer()
    material_uom = serializers.SerializerMethodField()
    material_tax = serializers.SerializerMethodField()
    material_purchase_org = serializers.SerializerMethodField()
    material_purchase_grp = serializers.SerializerMethodField()


    def get_material_uom(self, obj):
        qs = Material_UOM.objects.filter(material=obj,is_deleted=False)
        serializer = MaterialUOMSerializerforRead(instance=qs,many=True)
        return serializer.data

    def get_material_tax(self, obj):
        qs = Material_Tax.objects.filter(material=obj,is_deleted=False)
        serializer = MaterialTaxSerializer(instance=qs,many=True)
        return serializer.data

    def get_material_purchase_org(self, obj):
        qs = MaterialPurchaseOrg.objects.filter(material=obj,is_deleted=False)
        serializer = MaterialPurchaseOrgSerializer(instance=qs,many=True)
        return serializer.data

    def get_material_purchase_grp(self, obj):
        qs = MaterialPurchaseGroup.objects.filter(material=obj,is_deleted=False)
        serializer = MaterialPurchaseGrpSerializer(instance=qs,many=True)
        return serializer.data



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

                    material_uoms_data_ids = list()
                    for material_uoms_data_id in material_uoms_data:
                        if material_uoms_data_id['id']:
                            material_uoms_data_ids.append(material_uoms_data_id['id'])

                    material_uoms_instance_ids = list()
                    for item in material_uoms:
                        material_uoms_instance_ids.append(item.id)

                    uom_updateable_ids = list(set(material_uoms_data_ids) & set(material_uoms_instance_ids))
                    uom_deleteable_ids = list(set(material_uoms_instance_ids) - set(material_uoms_data_ids))

                    for uom_data in material_uoms_data:
                        if uom_data['id'] in uom_updateable_ids:
                            uom = Material_UOM.objects.get(pk=uom_data['id'])

                            uom.material_for = uom_data.get('material_for', uom.material_for)
                            uom.base_uom = uom_data.get('base_uom', uom.base_uom)
                            uom.unit_per_uom = uom_data.get('unit_per_uom', uom.unit_per_uom)
                            uom.unit_uom = uom_data.get('unit_uom', uom.unit_uom)
                            uom.is_deleted = uom_data.get('is_deleted', uom.is_deleted)

                            uom.save()

                        elif uom_data['id'] is None:
                            Material_UOM.objects.create(material=instance, **uom_data)

                    for delete_id in uom_deleteable_ids:
                        uom = Material_UOM.objects.get(pk=delete_id)
                        uom.is_deleted = True
                        uom.save()




                #material tax

                    material_taxs_data_ids = list()
                    for material_taxs_data_id in material_taxs_data:
                        if material_taxs_data_id['id']:
                            material_taxs_data_ids.append(material_taxs_data_id['id'])

                    material_taxs_instance_ids = list()
                    for item in material_taxs:
                        material_taxs_instance_ids.append(item.id)

                    tax_updateable_ids = list(set(material_taxs_data_ids) & set(material_taxs_instance_ids))
                    tax_deleteable_ids = list(set(material_taxs_instance_ids) - set(material_taxs_data_ids))

                    for tax_data in material_taxs_data:
                        if tax_data['id'] in tax_updateable_ids:
                            tax = Material_Tax.objects.get(pk=tax_data['id'])

                            tax.tax_for = tax_data.get('tax_for', tax.tax_for)
                            tax.igst = tax_data.get('igst', tax.igst)
                            tax.cgst = tax_data.get('cgst', tax.cgst)
                            tax.sgst = tax_data.get('sgst', tax.sgst)
                            tax.hsn = tax_data.get('hsn', tax.hsn)
                            tax.is_deleted = tax_data.get('is_deleted', tax.is_deleted)

                            tax.save()

                        elif tax_data['id'] is None:
                            Material_Tax.objects.create(material=instance, **tax_data)

                    for delete_id in tax_deleteable_ids:
                        tax = Material_Tax.objects.get(pk=delete_id)
                        tax.is_deleted = True
                        tax.save()



                #material purchase organisation

                    material_pur_orgs_data_ids = list()
                    for material_pur_orgs_data_id in material_pur_orgs_data:
                        if material_pur_orgs_data_id['id']:
                            material_pur_orgs_data_ids.append(material_pur_orgs_data_id['id'])

                    material_pur_orgs_instance_ids = list()
                    for item in material_pur_orgs:
                        material_pur_orgs_instance_ids.append(item.id)

                    pur_org_updateable_ids = list(set(material_pur_orgs_data_ids) & set(material_pur_orgs_instance_ids))
                    pur_org_deleteable_ids = list(set(material_pur_orgs_instance_ids) - set(material_pur_orgs_data_ids))

                    for org_data in material_pur_orgs_data:
                        if org_data['id'] in pur_org_updateable_ids:
                            org = MaterialPurchaseOrg.objects.get(pk=org_data['id'])

                            org.pur_org = org_data.get('pur_org', org.pur_org)
                            org.is_deleted = org_data.get('is_deleted', org.is_deleted)
                            org.save()

                        elif org_data['id'] is None:
                            MaterialPurchaseOrg.objects.create(material=instance, **org_data)

                    for delete_id in pur_org_deleteable_ids:
                        org = MaterialPurchaseOrg.objects.get(pk=delete_id)
                        org.is_deleted = True
                        org.save()


                #material purchase group

                    material_pur_grps_data_ids = list()
                    for material_pur_grps_data_id in material_pur_grps_data:
                        if material_pur_grps_data_id['id']:
                            material_pur_grps_data_ids.append(material_pur_grps_data_id['id'])

                    material_pur_grps_instance_ids = list()
                    for item in material_pur_grps:
                        material_pur_grps_instance_ids.append(item.id)

                    pur_grp_updateable_ids = list(set(material_pur_grps_data_ids) & set(material_pur_grps_instance_ids))
                    pur_grp_deleteable_ids = list( set(material_pur_grps_instance_ids) - set(material_pur_grps_data_ids))

                    for grp_data in material_pur_grps_data:
                        if grp_data['id'] in pur_grp_updateable_ids:
                            grp = MaterialPurchaseGroup.objects.get(pk=grp_data['id'])

                            grp.pur_group = grp_data.get('pur_group', grp.pur_group)
                            grp.is_deleted = grp_data.get('is_deleted', grp.is_deleted)
                            grp.save()

                        elif grp_data['id'] is None:
                            MaterialPurchaseGroup.objects.create(material=instance, **grp_data)

                    for delete_id in pur_grp_deleteable_ids:
                        grp = MaterialPurchaseGroup.objects.get(pk=delete_id)
                        grp.is_deleted = True
                        grp.save()

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

                    material_uoms_data_ids = list()
                    for material_uoms_data_id in material_uoms_data:
                        if material_uoms_data_id['id']:
                            material_uoms_data_ids.append(material_uoms_data_id['id'])

                    material_uoms_instance_ids = list()
                    for item in material_uoms:
                        material_uoms_instance_ids.append(item.id)

                    uom_updateable_ids = list(set(material_uoms_data_ids) & set(material_uoms_instance_ids))
                    uom_deleteable_ids = list(set(material_uoms_instance_ids) - set(material_uoms_data_ids))

                    for uom_data in material_uoms_data:
                        if uom_data['id'] in uom_updateable_ids:
                            uom = Material_UOM.objects.get(pk=uom_data['id'])

                            uom.material_for = uom_data.get('material_for', uom.material_for)
                            uom.base_uom = uom_data.get('base_uom', uom.base_uom)
                            uom.unit_per_uom = uom_data.get('unit_per_uom', uom.unit_per_uom)
                            uom.unit_uom = uom_data.get('unit_uom', uom.unit_uom)
                            uom.is_deleted = uom_data.get('is_deleted', uom.is_deleted)

                            uom.save()

                        elif uom_data['id'] is None:
                            Material_UOM.objects.create(material=instance, **uom_data)

                    for delete_id in uom_deleteable_ids:
                        uom = Material_UOM.objects.get(pk=delete_id)
                        uom.is_deleted = True
                        uom.save()




                        # material tax

                    material_taxs_data_ids = list()
                    for material_taxs_data_id in material_taxs_data:
                        if material_taxs_data_id['id']:
                            material_taxs_data_ids.append(material_taxs_data_id['id'])

                    material_taxs_instance_ids = list()
                    for item in material_taxs:
                        material_taxs_instance_ids.append(item.id)

                    tax_updateable_ids = list(set(material_taxs_data_ids) & set(material_taxs_instance_ids))
                    tax_deleteable_ids = list(set(material_taxs_instance_ids) - set(material_taxs_data_ids))

                    for tax_data in material_taxs_data:
                        if tax_data['id'] in tax_updateable_ids:
                            tax = Material_Tax.objects.get(pk=tax_data['id'])

                            tax.tax_for = tax_data.get('tax_for', tax.tax_for)
                            tax.igst = tax_data.get('igst', tax.igst)
                            tax.cgst = tax_data.get('cgst', tax.cgst)
                            tax.sgst = tax_data.get('sgst', tax.sgst)
                            tax.hsn = tax_data.get('hsn', tax.hsn)
                            tax.is_deleted = True
                            tax.save()

                        elif tax_data['id'] is None:
                            Material_Tax.objects.create(material=instance, **tax_data)

                    for delete_id in tax_deleteable_ids:
                        tax = Material_Tax.objects.get(pk=delete_id)
                        tax.is_deleted = True
                        tax.save()



                        # material purchase organisation

                    material_pur_orgs_data_ids = list()
                    for material_pur_orgs_data_id in material_pur_orgs_data:
                        if material_pur_orgs_data_id['id']:
                            material_pur_orgs_data_ids.append(material_pur_orgs_data_id['id'])

                    material_pur_orgs_instance_ids = list()
                    for item in material_pur_orgs:
                        material_pur_orgs_instance_ids.append(item.id)

                    pur_org_updateable_ids = list(set(material_pur_orgs_data_ids) & set(material_pur_orgs_instance_ids))
                    pur_org_deleteable_ids = list(set(material_pur_orgs_instance_ids) - set(material_pur_orgs_data_ids))

                    for org_data in material_pur_orgs_data:
                        if org_data['id'] in pur_org_updateable_ids:
                            org = MaterialPurchaseOrg.objects.get(pk=org_data['id'])

                            org.pur_org = org_data.get('pur_org', org.pur_org)
                            org.is_deleted = org_data.get('is_deleted', org.is_deleted)
                            org.save()

                        elif org_data['id'] is None:
                            MaterialPurchaseOrg.objects.create(material=instance, **org_data)

                    for delete_id in pur_org_deleteable_ids:
                        org = MaterialPurchaseOrg.objects.get(pk=delete_id)
                        org.is_deleted = True
                        org.save()


                        # material purchase group

                    material_pur_grps_data_ids = list()
                    for material_pur_grps_data_id in material_pur_grps_data:
                        if material_pur_grps_data_id['id']:
                            material_pur_grps_data_ids.append(material_pur_grps_data_id['id'])

                    material_pur_grps_instance_ids = list()
                    for item in material_pur_grps:
                        material_pur_grps_instance_ids.append(item.id)

                    pur_grp_updateable_ids = list(set(material_pur_grps_data_ids) & set(material_pur_grps_instance_ids))
                    pur_grp_deleteable_ids = list(set(material_pur_grps_instance_ids) - set(material_pur_grps_data_ids))

                    for grp_data in material_pur_grps_data:
                        if grp_data['id'] in pur_grp_updateable_ids:
                            grp = MaterialPurchaseGroup.objects.get(pk=grp_data['id'])

                            grp.pur_group = grp_data.get('pur_group', grp.pur_group)
                            grp.is_deleted = grp_data.get('is_deleted', grp.is_deleted)
                            grp.save()

                        elif grp_data['id'] is None:
                            MaterialPurchaseGroup.objects.create(material=instance, **grp_data)

                    for delete_id in pur_grp_deleteable_ids:
                        grp = MaterialPurchaseGroup.objects.get(pk=delete_id)
                        grp.is_deleted = True
                        grp.save()

                    return instance

    # def update(self, instance, validated_data):
    #     is_taxable = validated_data.get('is_taxable')
    #     print(is_taxable)
    #
    #     if is_taxable == True:
    #         material_uoms_data = validated_data.pop('material_uom')
    #         material_taxs_data = validated_data.pop('material_tax')
    #         material_pur_orgs_data = validated_data.pop('material_purchase_org')
    #         material_pur_grps_data = validated_data.pop('material_purchase_grp')
    #
    #         material_uoms = (instance.material_uom).all()
    #         material_uoms = list(material_uoms)
    #         material_taxs = (instance.material_tax).all()
    #         material_taxs = list(material_taxs)
    #         material_pur_orgs = (instance.material_purchase_org).all()
    #         material_pur_orgs = list(material_pur_orgs)
    #         material_pur_grps = (instance.material_purchase_grp).all()
    #         material_pur_grps = list(material_pur_grps)
    #
    #         instance.material_fullname = validated_data.get('material_fullname', instance.material_fullname)
    #         instance.material_type = validated_data.get('material_type', instance.material_type)
    #         instance.material_code = validated_data.get('material_code', instance.material_code)
    #         instance.description = validated_data.get('description', instance.description)
    #         instance.is_taxable = validated_data.get('is_taxable', instance.is_taxable)
    #         instance.is_sales = validated_data.get('is_sales', instance.is_sales)
    #         instance.status = validated_data.get('status', instance.status)
    #         instance.created_at = validated_data.get('created_at', instance.created_at)
    #         instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
    #         instance.save()
    #
    #         print(instance)
    #
    #         for material_uom in material_uoms:
    #             if material_uom:
    #                 print(material_uom)
    #                 material_uom.delete()
    #         for material_tax in material_taxs:
    #             if material_tax:
    #                 print(material_tax)
    #                 material_tax.delete()
    #         for material_pur_org in material_pur_orgs:
    #             if material_pur_org:
    #                 material_pur_org.delete()
    #         for material_pur_grp in material_pur_grps:
    #             if material_pur_grp:
    #                 material_pur_grp.delete()
    #
    #         for material_uom in material_uoms_data:
    #             Material_UOM.objects.create(material=instance, **material_uom)
    #         for material_tax in material_taxs_data:
    #             Material_Tax.objects.create(material=instance, **material_tax)
    #         for material_pur_org in material_pur_orgs_data:
    #             MaterialPurchaseOrg.objects.create(material=instance, **material_pur_org)
    #         for material_pur_grp in material_pur_grps_data:
    #             MaterialPurchaseGroup.objects.create(material=instance, **material_pur_grp)
    #
    #         return instance
    #
    #     else:
    #         material_uoms_data = validated_data.pop('material_uom')
    #         material_taxs_data = validated_data.pop('material_tax')
    #         material_pur_orgs_data = validated_data.pop('material_purchase_org')
    #         material_pur_grps_data = validated_data.pop('material_purchase_grp')
    #
    #         material_uoms = (instance.material_uom).all()
    #         material_uoms = list(material_uoms)
    #         material_taxs = (instance.material_tax).all()
    #         material_taxs = list(material_taxs)
    #         material_pur_orgs = (instance.material_purchase_org).all()
    #         material_pur_orgs = list(material_pur_orgs)
    #         material_pur_grps = (instance.material_purchase_grp).all()
    #         material_pur_grps = list(material_pur_grps)
    #
    #         instance.material_fullname = validated_data.get('material_fullname', instance.material_fullname)
    #         instance.material_type = validated_data.get('material_type', instance.material_type)
    #         instance.material_code = validated_data.get('material_code', instance.material_code)
    #         instance.description = validated_data.get('description', instance.description)
    #         instance.is_taxable = validated_data.get('is_taxable', instance.is_taxable)
    #         instance.is_sales = validated_data.get('is_sales', instance.is_sales)
    #         instance.status = validated_data.get('status', instance.status)
    #         instance.created_at = validated_data.get('created_at', instance.created_at)
    #         instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
    #         instance.save()
    #
    #         print(instance)
    #
    #         for material_uom in material_uoms:
    #             if material_uom:
    #                 print(material_uom)
    #                 material_uom.delete()
    #         for material_tax in material_taxs:
    #             if material_tax:
    #                 print(material_tax)
    #                 material_tax.delete()
    #         for material_pur_org in material_pur_orgs:
    #             if material_pur_org:
    #                 material_pur_org.delete()
    #         for material_pur_grp in material_pur_grps:
    #             if material_pur_grp:
    #                 material_pur_grp.delete()
    #
    #         for material_uom in material_uoms_data:
    #             Material_UOM.objects.create(material=instance, **material_uom)
    #         for material_pur_org in material_pur_orgs_data:
    #             MaterialPurchaseOrg.objects.create(material=instance, **material_pur_org)
    #         for material_pur_grp in material_pur_grps_data:
    #             MaterialPurchaseGroup.objects.create(material=instance, **material_pur_grp)
    #
    #         return instance



class MaterialNameSerializer(ModelSerializer):
    material_tax = MaterialTaxSerializer(many=True)

    class Meta:
        model = Material
        fields = ['id','material_fullname','material_code','material_tax']