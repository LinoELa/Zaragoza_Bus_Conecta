
# 8 D - FORMULARIO DE REGISTRO 
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# 13 C historial 
from .models import historial



# 8 E - Informacion a recopilar 
class FormRegistro(UserCreationForm):
    nombre =  forms.CharField(required=True, label='', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre *'}))
    correo =  forms.EmailField(required=True, label='',max_length=50 , widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email' } ))


    # 8 F - Informacion a enseñar en el front de registro
    class Meta:
        model = User
        fields = ('nombre', 'correo' , 'username' ,'password1', 'password2')


    # 8 G - Llamar al contructor de la parte de (formulario registro)
    def __init__(self, *args, **kwargs):
        super(FormRegistro, self).__init__(*args, **kwargs)

        # 8 H - Personalizacion de los campos del fomulario
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'nombre usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small> Sólo letras, dígitos y @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña*'
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['id'] = 'password1'  # Añadir un id único
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña no puede corta ni cumun.</li><li>Su contraseña debe contener al menos 8 caracteres.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña*'
        self.fields['password2'].widget.attrs['id'] = 'password2'  # Añadir un id único
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Introduzca la misma contraseña que antes, para la verificación</small></span>'


# 13 D
class FormAgregar (forms.ModelForm):
    inicio = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Inicio", "class":"form-control"}), label="")

    final = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Final", "class":"form-control"}), label="")

# ------------------ Para hacer que no sea obligatario y que pueda pasar  el argumento vacio como un None

    poste_1 = forms.CharField(required=True, widget=forms.NumberInput(attrs={"placeholder":"Numero Poste ", "class":"form-control"}), label="")

    poste_2 = forms.CharField(required=False, widget=forms.NumberInput(attrs={"placeholder":"Numero Poste ", "class":"form-control"}), label="")

    poste_3 = forms.CharField(required=False, widget=forms.NumberInput(attrs={"placeholder":"Numero Poste ", "class":"form-control"}), label="")

    notas = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"Notas", "class":"form-control"}), label="")


    class Meta:
        model = historial
        # la (,) al final es importante
        exclude = ('user',)
