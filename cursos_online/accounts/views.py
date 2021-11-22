from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404

from django.urls import reverse_lazy
from django.views import generic

from .models import ResetarSenha
from .forms import CadastrarUsuarioForm, EditarUsuarioForm, ResetarSenhaForm
from .utils import generate_hash_key


User = get_user_model()


class CadastrarUsuarioView(generic.CreateView):
    form_class = CadastrarUsuarioForm
    template_name = 'accounts/cadastrar_usuario.html'
    success_url = reverse_lazy('accounts:login') 


def resetar_senha(request):
    template_name = 'accounts/resetar_senha.html'
    context = {}
    form = ResetarSenhaForm(request.POST or None)
    if form.is_valid():
       form.save()
       context['success'] = True
    context ['form'] =  form
    return render(request, template_name, context)


def confirmar_resetar_senha(request, key):
    template_name = 'accounts/resetar_senha_confirmar.html'
    context = {}
    reset = get_object_or_404(ResetarSenha, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


# def register(request):
#     template_name = 'accounts/cadastro.html'
#     form_class = CriarUsuariocomEmailForm
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = UserCreationForm()
#     context = {
#         'form':form
#     }
#     return render(request, template_name, context)


@login_required
def painel(request):
    # template_name = 'accounts/painel.html'
    template_name = 'accounts/dashboard.html'
    return render(request, template_name,)


@login_required
def editar_usuario(request):
    template_name = 'accounts/editar_usuario.html'
    context = {}
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditarUsuarioForm(instance=request.user)
            context['success'] = True
    else:
        form = EditarUsuarioForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def editar_senha(request):
    template_name = 'accounts/editar_senha.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


