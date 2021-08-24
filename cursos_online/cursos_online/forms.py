from django import forms


class FormContato(forms.Form):
    nome = forms.CharField(label="Nome", widget=forms.TextInput())
    email = forms.EmailField(label="E-mail", widget=forms.TextInput())
    mensagem = forms.CharField(label="Assunto", widget=forms.Textarea())