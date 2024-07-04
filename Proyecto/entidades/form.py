from django import forms
    
class ClienteForm(forms.Form):
    Nombre = forms.CharField(max_length=50, required=True)
    Correo = forms.EmailField(required=True)
    Consulta = forms.CharField(max_length=50, required=True)