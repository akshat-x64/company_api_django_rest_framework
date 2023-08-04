from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def home_page(request):
    print('Home page requested')
    list_1 = ["Akshat", "Dwivdi", "Capgemini"]
    return JsonResponse(list_1, safe=False)
