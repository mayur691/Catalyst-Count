from rest_framework.serializers import ModelSerializer
from catalystapp.models import Employee
class EmpSerializer(ModelSerializer):
    class Meta:
        model= Employee
        fields = '__all__'