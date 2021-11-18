from django.urls import path
from django.contrib.auth import views as auth_views


from . import views


app_name = 'accounts'

urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('painel/', views.painel, name='painel'),
    path('cadastrar/', views.CadastrarView.as_view(), name='cadastro'),
    path('editar/', views.editar, name='editar'),
]





