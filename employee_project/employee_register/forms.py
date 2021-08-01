from django import forms
from django.db.models.base import Model
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta():
        model = Employee
        fields = ('fullName','empCode','MobileNo','position')
        labels = {

                'fullName':'Full Name',
                'empCode':'Emp Code',
                'MobileNo': 'Mobile No.',
                'position': 'Position'
        }
            
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"