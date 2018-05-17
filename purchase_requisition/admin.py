from django.contrib import admin
from purchase_requisition.models import Requisition,RequisitionDetail,RequisitionMap
# Register your models here.

admin.site.register(Requisition)
admin.site.register(RequisitionDetail)
admin.site.register(RequisitionMap)
