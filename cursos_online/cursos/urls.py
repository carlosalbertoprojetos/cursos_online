from django.urls import path


from . import views


app_name = 'cursos'


urlpatterns = [
    path('', views.lista_CursosView, name='lista_cursos'),
    path('contato/', views.contatoCursoView, name='contato'),
    path('<slug:slug>/', views.detalhes_CursoView, name='detalhes_curso'),
    path('<slug:slug>/inscricao/', views.enrollment, name='enrollment'),
    path('<slug:slug>/cancelar-inscricao/', views.cancelar_enrollment, name='cancelar_enrollment'),
    path('<slug:slug>/anuncios/', views.anuncios, name='anuncios'),
]


