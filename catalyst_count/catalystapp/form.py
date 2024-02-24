from django import forms
from .models import Upload,Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields = "__all__"



class CSVImportForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'
