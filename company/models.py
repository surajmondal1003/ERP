from django.db import models
from states.models import State
from django.contrib.auth.models import User


# Create your models here.

class Company(models.Model):
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='children', null=True, blank=True)
    company_name=models.CharField(max_length=100)
    company_url=models.URLField()
    company_gst=models.CharField(max_length=50)
    company_pan=models.CharField(max_length=50)
    company_cin=models.CharField(max_length=50)
    company_email=models.EmailField(max_length=50)
    company_address=models.CharField(max_length=100)
    company_contact=models.BigIntegerField()
    company_state=models.ForeignKey(State,on_delete=models.SET_NULL,blank=True,null=True)
    company_city=models.CharField(max_length=100)
    company_pin=models.CharField(max_length=50)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return str(self.company_name)

