from django.db import models
from company.models import Company
from purchaseorggroup.models import PurchaseOrg,PurchaseGroup
from django.contrib.auth.models import User
from material_master.models import Material
from company_branch.models import UOM,CompanyBranch,StorageLocation,StorageBin

# Create your models here.

class Requisition(models.Model):
    STATUS_CHOICES = (
        ('2', 'False'),
        ('1', 'True'),
        ('0', 'None'),
    )


    company=models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True,related_name='requisition_company')
    purchase_org=models.ForeignKey(PurchaseOrg, on_delete=models.SET_NULL, blank=True, null=True,related_name='requisition_pur_org')
    purchase_grp=models.ForeignKey(PurchaseGroup, on_delete=models.SET_NULL, blank=True, null=True,related_name='requisition_pur_grp')
    special_note=models.TextField()
    is_approve = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    is_finalised = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,related_name='requisition_by')

    def __str__(self):
        return str(self.created_at)


class RequisitionDetail(models.Model):
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE,related_name='requisition_detail')
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, blank=True, null=True)
    quantity=models.DecimalField(max_digits=10,decimal_places=2)
    uom=models.ForeignKey(UOM,on_delete=models.SET_NULL,blank=True,null=True)

    branch = models.ForeignKey(CompanyBranch, on_delete=models.SET_NULL, blank=True, null=True)
    storage_location=models.ForeignKey(StorageLocation, on_delete=models.SET_NULL, blank=True, null=True)
    storage_bin=models.ForeignKey(StorageBin, on_delete=models.SET_NULL, blank=True, null=True)

    status = models.BooleanField(default=True)


    def __str__(self):
        return str(self.requisition.created_at)

class RequisitionMap(models.Model):
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE, related_name='requisition_map')
    requisition_no = models.CharField(max_length=255)

    def __str__(self):
        return str(self.requisition_no)








