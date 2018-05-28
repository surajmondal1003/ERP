from employee import views
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path



urlpatterns = [
    path('employee/',views.EmployeeMatser.as_view()),
    path('all_employee/',views.EmployeeReadView.as_view()),
    path('all_employee/<pk>/',views.EmployeeReadDetailView.as_view()),

]
