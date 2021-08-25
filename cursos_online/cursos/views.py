from django.shortcuts import render, get_object_or_404


from .models import Cursos



def lista_CursosView(request):
    lista_cursos = Cursos.objects.all()
    context = {
        'lista_cursos': lista_cursos,
        }
    template_name = 'cursos/lista_cursos.html'
    return render(request, template_name, context)



def detalhes_CursoView(request, slug):
    curso = get_object_or_404(Cursos, slug=slug)
    context = {
        'curso': curso,
        }
    template_name = 'cursos/detalhes_curso.html'
    return render(request, template_name, context)


