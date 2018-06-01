from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from purchase_requisition.models import RequisitionDetail,Requisition,RequisitionMap
from django.contrib.auth.models import User
import datetime
from employee.models import Employee
from authentication.serializers import UserLoginSerializer,UserReadSerializer
from company.serializers import CompanyListSerializer
from departments.serializers import DepartmentsListSerializer
from designation.serializers import DesignationReadSerializer

class EmployeeSerializer(ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.BooleanField(default=True)
    blood_group=serializers.CharField(required=False)

    class Meta:
        model = Employee
        fields = ['id','company','departments','designation','first_name','last_name','email','contact','dob','alt_contact',
                  'pan','blood_group','adhaar_no','emp_present_address','emp_present_state','emp_present_city','emp_present_pin',
                  'emp_permanent_address','emp_permanent_state','emp_permanent_city','emp_permanent_pin','created_at','created_by','status'
                  ,'is_deleted']




class EmployeeReadSerializer(ModelSerializer):
    created_by = UserReadSerializer()
    status = serializers.BooleanField(default=True)
    company = CompanyListSerializer()
    departments = DepartmentsListSerializer()
    designation = DesignationReadSerializer()

    class Meta:
        model = Employee
        fields = ['id','company','departments','designation','first_name','last_name','email','contact','dob','alt_contact',
                  'pan','blood_group','adhaar_no','emp_present_address','emp_present_state','emp_present_city','emp_present_pin',
                  'emp_permanent_address','emp_permanent_state','emp_permanent_city','emp_permanent_pin','created_at','created_by','status',
                  'is_deleted']
