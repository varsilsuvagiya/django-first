from rest_framework import serializers
from api.models import Company,Employee


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields='__all__'
        
        #fields = ['company_id', 'name', 'location', 'about', 'type', 'added_date', 'active']  selected field

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
