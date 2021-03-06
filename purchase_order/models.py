from django.db import models
from purchase_requisition.models import Requisition
from purchaseorggroup.models import PurchaseGroup,PurchaseOrg
from company.models import Company,TermsandConditon
from vendor.models import Vendor,VendorAddress
from django.contrib.auth.models import User
from company_branch.models import CompanyBranch,StorageLocation,StorageBin,UOM
from material_master.models import Material,Material_UOM
from gstrates.models import GSTrates
from purchase_requisition.models import RequisitionMap


# Create your models here.

class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ('2', 'False'),
        ('1', 'True'),
        ('0', 'None'),
    )

    requisition=models.ForeignKey(Requisition,on_delete=models.SET_NULL,blank=True,null=True)
    quotation_no=models.CharField(max_length=200)
    quotation_date=models.DateTimeField()
    pur_org=models.ForeignKey(PurchaseOrg,on_delete=models.SET_NULL,blank=True,null=True)
    pur_grp=models.ForeignKey(PurchaseGroup,on_delete=models.SET_NULL,blank=True,null=True)
    company=models.ForeignKey(Company,on_delete=models.SET_NULL,blank=True,null=True)
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,blank=True,null=True)
    vendor_address=models.ForeignKey(VendorAddress,on_delete=models.SET_NULL,blank=True,null=True)
    grand_total=models.DecimalField(max_digits=20,decimal_places=2)
    grand_total_words=models.CharField(max_length=255)
    is_approve = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    is_finalised = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.created_at)


    def requisition_no(self):
        return RequisitionMap.objects.filter(requisition=self.requisition)



class PurchaseOrderDetail(models.Model):
    po_order=models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE,related_name='purchase_order_detail')
    company_branch=models.ForeignKey(CompanyBranch,on_delete=models.SET_NULL,blank=True,null=True)
    storage_location=models.ForeignKey(StorageLocation,on_delete=models.SET_NULL,blank=True,null=True)
    storage_bin=models.ForeignKey(StorageBin,on_delete=models.SET_NULL,blank=True,null=True)
    material=models.ForeignKey(Material,on_delete=models.SET_NULL,blank=True,null=True)
    uom=models.ForeignKey(UOM,on_delete=models.SET_NULL,blank=True,null=True)
    requisition_quantity=models.DecimalField(max_digits=20,decimal_places=2)
    order_quantity=models.DecimalField(max_digits=20,decimal_places=2)
    rate=models.DecimalField(max_digits=15,decimal_places=2)
    material_value=models.DecimalField(max_digits=20,decimal_places=2)
    discount_percent=models.DecimalField(max_digits=8,decimal_places=2)
    discount_value=models.DecimalField(max_digits=20,decimal_places=2)
    igst=models.DecimalField(max_digits=10,decimal_places=2)
    cgst=models.DecimalField(max_digits=10,decimal_places=2)
    sgst=models.DecimalField(max_digits=10,decimal_places=2)
    gst_amount=models.DecimalField(max_digits=10,decimal_places=2)
    sub_total=models.DecimalField(max_digits=10,decimal_places=2)
    delivery_date=models.DateTimeField()

    def __str__(self):
        return str(self.po_order.created_at)


class PurchaseOrderFreight(models.Model):
    FREIGHT_CHOICES = (
        ('1', 'Vendor'),
        ('2', 'Own'),
    )

    po_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='purchase_order_freight')
    freight_option = models.CharField(max_length=1, choices=FREIGHT_CHOICES, default=None,blank=True,null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True)
    freight_rate=models.DecimalField(max_digits=10,decimal_places=2)
    freight_amount=models.DecimalField(max_digits=15,decimal_places=2)
    freight_gst_rate=models.ForeignKey(GSTrates, on_delete=models.SET_NULL, blank=True, null=True)
    freight_total=models.DecimalField(max_digits=20,decimal_places=2)


    def __str__(self):
        return str(self.po_order.created_at)


class PurchaseOrderTerms(models.Model):
    po_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='purchase_order_terms')
    po_terms=models.ForeignKey(TermsandConditon,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return str(self.po_order.created_at)


class PurchaseOrderMap(models.Model):
    po_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='purchase_order_map')
    purchase_order_no = models.CharField(max_length=255)

    def __str__(self):
        return str(self.purchase_order_no)








