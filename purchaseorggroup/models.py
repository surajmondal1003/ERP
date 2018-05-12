from django.db import models
from django.contrib.auth.models import User
from company_branch.models import CompanyBranch


# Create your models here.
class PurchaseOrg(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class PurchaseGroup(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class PurchaseOrgMapping(models.Model):
    pur_org=models.ForeignKey(PurchaseOrg,on_delete=models.CASCADE)
    branch=models.ForeignKey(CompanyBranch,on_delete=models.SET_NULL,blank=True,null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = (('pur_org', 'branch'))
        index_together = (('pur_org', 'branch'))

    def __str__(self):
        return str(self.pur_org.name)

