from django.shortcuts import render
from rest_framework import viewsets
from api.models import company
from api.models import employee
from api.serializers import companyserializers, employeeserializers
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import company, employee
# Create your views here.


class companyviewset(viewsets.ModelViewSet):
    queryset = company.objects.all()

    serializer_class = companyserializers

    @action(detail=True, methods=['get'])
    def employee(self, request, pk=None):
        print("get employees of ", pk, "company")
        company_instance = company.objects.get(pk=pk)
        emps = employee.objects.filter(company1=company_instance)
        emps_serializer = employeeserializers(
            emps, many=True, context={'request': request})
        return Response(emps_serializer.data)


class employeeviewset(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeserializers
