from rest_framework import serializers
from api.models import company
from api.models import employee
# create serializers here


class companyserializers(serializers.HyperlinkedModelSerializer):
    company_i = serializers.ReadOnlyField()

    class Meta:
        model = company
        fields = "__all__"


class employeeserializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = employee
        fields = '__all__'
