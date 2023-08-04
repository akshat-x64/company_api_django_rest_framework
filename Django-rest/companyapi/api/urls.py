from django.contrib import admin
from django.urls import path, include
from api.views import companyviewset, employeeviewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"company", companyviewset)
router.register(r"employee", employeeviewset)
urlpatterns = [
    path("", include(router.urls))
]
