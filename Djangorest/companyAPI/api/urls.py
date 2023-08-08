
from django.urls import path
from django.urls import include
from rest_framework import routers
from api.views import companyViewSet
from api.views import employeeViewset

router = routers.DefaultRouter()
router.register(r"company", companyViewSet)
router.register(r"employee", employeeViewset)
urlpatterns = [

    path("", include(router.urls))
]
