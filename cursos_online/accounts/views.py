from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.shortcuts import redirect, render

from django.urls import reverse_lazy
from django.views import generic
from .forms import CadastrarUsuarioForm, EditarUsuarioForm



class CadastrarUsuarioView(generic.CreateView):
    form_class = CadastrarUsuarioForm
    template_name = 'accounts/cadastrar_usuario.html'
    success_url = reverse_lazy('accounts:login') 

    
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


