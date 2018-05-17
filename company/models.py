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



class TermsandConditon(models.Model):
    TERM_CHOICES = (
        ('1', 'Payment'),
        ('2', 'Delivery'),
        ('3', 'Others'),
    )

    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    term_type = models.CharField(max_length=1, choices=TERM_CHOICES, default=None,blank=True,null=True)
    term_text=models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.company.company_name)


