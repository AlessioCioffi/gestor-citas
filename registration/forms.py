from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserCreationFormsEmail(UserCreationForm):
    # Creo un nuevo form porque el default de django no pide mail
    email = forms.EmailField(required=True,help_text="Requerido, máximo 254 caracteres")
    # Añado la mail a modelo user
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2']

    def clean_email(self):
        # recupero el valor del campo email del formulario
        email = self.cleaned_data.get('email')
        # compruebo si ya existe en el query
        if User.objects.filter(email=email).exists():
            # Generamos una excepción con raise
            raise forms.ValidationError("el email ya está registrado")
        return email
