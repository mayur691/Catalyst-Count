from django.urls import path,include
from rest_framework import routers
from catalystapp.api.views import EmployeeCRUDCBV
router=routers.DefaultRouter()
router.register('employeeinfo',EmployeeCRUDCBV)
urlpatterns = [
    path(r'', include(router.urls)),
]