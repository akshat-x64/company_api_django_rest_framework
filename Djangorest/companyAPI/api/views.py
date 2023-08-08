from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serializers import companySerializers
from api.models import Employee
from api.serializers import employeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class companyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = companySerializers
    # /company/{company.id}/employee

    @action(detail=True, methods=['get'])
    def employee(self, request, pk=None):
        print("method gets executed", pk, 'company')
        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(company=company)
            emp_serializers = employeeSerializers(
                emp, many=True, context={'request': request})
            return Response(emp_serializers.data)
        except Exception as e:
            print(e)
            return ResourceWarning({'message': 'company might not exist'})


class employeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializers
