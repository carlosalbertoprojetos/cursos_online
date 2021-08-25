from django.shortcuts import render, get_object_or_404


from .models import Cursos
from cursos_online.forms import FormContato



def lista_CursosView(request):
    lista_cursos = Cursos.objects.all()
    context = {
        'lista_cursos': lista_cursos,
        }
    template_name = 'cursos/lista_cursos.html'
    return render(request, template_name, context)


# forma simples
# def detalhes_CursoView(request, slug):
#     curso = get_object_or_404(Cursos, slug=slug)
#     context = {
#         'curso': curso,
#         }
#     template_name = 'cursos/detalhes_curso.html'
#     return render(request, template_name, context)


def detalhes_CursoView(request, slug):
    curso = get_object_or_404(Cursos, slug=slug)
    context = {}
    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form = FormContato()
    else:
        form = FormContato()
    context['curso'] = curso
    context['form']= form
    template_name = 'cursos/detalhes_curso.html'
    return render(request, template_name, context)




    