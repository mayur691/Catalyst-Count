from rest_framework import viewsets
from catalystapp.models import Employee
from catalystapp.api.serializers import EmpSerializer
class EmployeeCRUDCBV(viewsets.ModelViewSet):
    serializer_class=EmpSerializer
    queryset=Employee.objects.all()