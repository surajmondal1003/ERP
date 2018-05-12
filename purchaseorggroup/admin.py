from django.contrib import admin
from purchaseorggroup.models import PurchaseOrg,PurchaseGroup,PurchaseOrgMapping

# Register your models here.

admin.site.register(PurchaseOrg)
admin.site.register(PurchaseGroup)
admin.site.register(PurchaseOrgMapping)
