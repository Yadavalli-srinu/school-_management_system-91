from django import forms
from app1.models import staff_model,student_model,fee_model
class staff_update_form(forms.ModelForm):
    class Meta:
        model=staff_model
        fields='__all__'

class student_update_form(forms.ModelForm):
    class Meta:
        model = student_model
        fields = '__all__'

class fee_update_form(forms.ModelForm):
    class Meta:
        model = fee_model
        fields = '__all__'