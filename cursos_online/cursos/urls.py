from django.urls import path


from . import views


app_name = 'cursos'


urlpatterns = [
    path('', views.lista_CursosView, name='lista_cursos'),
    path('contato/', views.contatoCursoView, name='contato'),
    path('<slug:slug>/', views.detalhes_CursoView, name = 'detalhes_curso'),
    
]
