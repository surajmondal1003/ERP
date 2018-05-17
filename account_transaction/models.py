# from django.db import models
# from company.models import Company
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
#
# # Create your models here.
#
# class Account_Transaction(models.Model):
#     TRANSACTION_CHOICES = (
#         ('1', 'Bank Opening'),
#         ('2', 'Employee Opening'),
#         ('3', 'Vendor Opening'),
#         ('4', 'Transporter Opening'),
#         ('5', 'Purchase'),
#         ('6', 'Payment'),
#         ('7', 'Expenses'),
#         ('8', 'Sales'),
#     )
#     company=models.ForeignKey(Company,on_delete=models.SET_NULL,blank=True,null=True)
#     transaction_type=models.CharField(max_length=1,choices=TRANSACTION_CHOICES,default=None,blank=True,null=True)
#     debitor_name=models.CharField(max_length=255)
#     creditor_name=models.CharField(max_length=255)
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#
#     debitor_id=GenericForeignKey('content_type', 'object_id')
#     creditor_id=models.CharField(max_length=255)
#
#
