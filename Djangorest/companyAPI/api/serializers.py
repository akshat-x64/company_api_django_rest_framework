from rest_framework import serializers
from api.models import Company
from api.models import Employee


class companySerializers(serializers.HyperlinkedModelSerializer):
    # company_id = serializers.ReadOnlyField()
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = '__all__'


class employeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
