from purchaseorggroup import views
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register(r'all_purchase_organization', views.PurchaseOrgViewSet)
router.register(r'all_purchase_group', views.PurchaseGroupViewSet)
router.register(r'purchase_org_mapping', views.PurchaseOrgMappingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('company_branch_tree/', views.CompanyBranchTreeView.as_view()),
    path('specific_purorg_mapping/<organisation>/', views.SpecificPurchaseOrgMappingView.as_view()),
    path('del_purorg_mapping/<pur_org>/', views.DeletePurchaseOrgMappingView.as_view()),
    path('purchase_org_active_list/', views.PurchaseOrgCheckList.as_view()),
    path('purchase_grp_active_list/', views.PurchaseGroupCheckList.as_view()),

]