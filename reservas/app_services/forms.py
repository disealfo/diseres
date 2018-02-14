from django  import forms

from models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    fields = [
        'name',
        'duration',
        'price',
        'description',

    ]

    labels = {
        'name': 'Nombre',
        'duration': 'Duracion',
        'price': 'Precio',
        'description': 'Descripcion',
    }

    widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'duration': forms.IntegerField(),
        'price': forms.TextInput(attrs={'class':'form-control'}),
        'description': forms.Textarea(attrs={'class':'form-control'}),
    }