from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'description']

    def clean_dept_name(self):
        dept_name = self.cleaned_data.get('dept_name')
        if Department.objects.filter(dept_name__iexact=dept_name).exists():
            raise forms.ValidationError("Department with this name already exists.")
        return dept_name