from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CriarUsuariocomEmailForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Campo obrigatório! Insira um email válido!')

    class Meta:
        model = User
        fields = ['email', 'username']

    # validação - verificar se o email informado para cadastrado já existe
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está cadastrado, por favor insira outro.')
        return email

    
class EditarUserForm(forms.ModelForm)    :
    
    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(
            email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Este email já está cadastrado, por favor insira outro.')
        return email
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
        
        