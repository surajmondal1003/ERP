from django.db import models
from states.models import State
from company.models import Company
from django.contrib.auth.models import User

# Create your models here.

class CompanyBranch(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='company_branch')
    branch_name=models.CharField(max_length=100)
    branch_address=models.CharField(max_length=100)
    branch_state=models.ForeignKey(State,on_delete=models.SET_NULL,blank=True,null=True)
    branch_city=models.CharField(max_length=100)
    branch_pincode=models.CharField(max_length=50)
    branch_contact_no=models.BigIntegerField()
    branch_email = models.EmailField(max_length=50)
    branch_gstin=models.CharField(max_length=50)
    branch_pan=models.CharField(max_length=50)
    branch_cin=models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.branch_name)



class StorageLocation(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    branch = models.ForeignKey(CompanyBranch, on_delete=models.CASCADE)
    storage_address=models.CharField(max_length=100)
    storage_state=models.ForeignKey(State,on_delete=models.SET_NULL,blank=True,null=True)
    storage_city=models.CharField(max_length=50)
    storage_pincode=models.CharField(max_length=50)
    storage_contact_no=models.BigIntegerField()
    storage_email = models.EmailField(max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.branch.branch_name)


class UOM(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return str(self.name)


class StorageBin(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    branch = models.ForeignKey(CompanyBranch, on_delete=models.CASCADE)
    storage = models.ForeignKey(StorageLocation, on_delete=models.CASCADE)
    uom=models.ForeignKey(UOM, on_delete=models.SET_NULL,blank=True,null=True)
    bin_no=models.CharField(max_length=100)
    bin_volume=models.DecimalField(max_digits=10,decimal_places=2)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.branch.branch_name)

