from django import forms
from django.forms.extras.widgets import SelectDateWidget
from models import Person
from django.contrib.auth.models import User
from app_establishment.models import Phone, Address


class PersonForm(forms.ModelForm):
        class Meta:
            model = Person

            fields=[
                'fullName',
                'lastName',
                'gender',
                'birthdate',
                'email',
            ]
            labels = {

                'fullName': 'Nombre completo',
                'lastName': 'Apellidos',
                'gender': 'Genero',
                'birthdate': 'Fecha de nacimiento',
                'email': 'Correo',
            }
            widgets={

                'fullName': forms.TextInput(attrs={'class':'form-control'}),
                'lastName': forms.TextInput(attrs={'class':'form-control'}),
                'gender' : forms.Select(attrs={'class':'form-control'}),
                'birthdate': forms.DateInput(attrs={'class':'form-control'}),
                'email': forms.EmailInput(attrs={'class':'form-control'}),
            }


class UserForm (forms.ModelForm):
        class Meta:
            model = User

            fields=[
                'username',
                'password',
            ]
            labels = {
                'username':'Nombre usuario',
                'password':'Contrasenia',


            }
            widgets={
                'username': forms.TextInput(attrs={'class':'form-control'}),
                'password': forms.PasswordInput(attrs={'class':'form-control'}),

            }


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone

        fields = [
            'number',
            'description',
        ]
        labels = {
            'number': 'Numero Telefono',
            'description': 'Descripcion',

        }
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddresForm(forms.ModelForm):
    class Meta:
        model = Address

        fields = [
            'address',
            'description',
        ]
        labels = {
            'address': 'Direccion',
            'description': 'Descripcion',

        }
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }