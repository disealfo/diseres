from django  import forms


class serviceForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)