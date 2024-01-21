from django import forms
from .models import Employee

# form of add a employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'designation', 'department', 'date_of_joining']
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    # Optional: You can set common attributes for all fields here, if needed
    # For example, you can set 'class': 'form-control' for all fields

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Name', 'required': True}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation', 'required': True}))
    department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department', 'required': True}))
    date_of_joining = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Joining', 'required': True}))


