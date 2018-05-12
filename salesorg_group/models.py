from django.db import models
from django.contrib.auth.models import User
from company_branch.models import CompanyBranch


# Create your models here.

class SalesOrg(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class SalesGroup(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.name)

