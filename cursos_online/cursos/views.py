from django.shortcuts import render



from .models import Cursos


def lista_CursosView(request):
    lista_cursos = Cursos.objects.all()
    context = {
        'lista_cursos': lista_cursos,
        }
    template_name = 'cursos/lista_cursos.html'
    return render(request, template_name, context)



