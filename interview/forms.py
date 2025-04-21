from django import forms

class CargarExcelForm(forms.Form):
    archivo = forms.FileField()
