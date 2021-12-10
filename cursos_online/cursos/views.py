from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage


from .models import Cursos, Enrollment
from .forms import FormContatoCurso



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
        form = FormContatoCurso(request.POST)
        if form.is_valid():
            context['is_valid'] = True # aciona a mensagem
            form.send_email(curso)
            form = FormContatoCurso()
    else:
        form = FormContatoCurso()
    context['curso'] = curso
    context['form']= form
    template_name = 'cursos/detalhes_curso.html'
    return render(request, template_name, context)


    
def contatoCursoView(request):
    send = False
    form = FormContatoCurso(request.POST or None)
    if form.is_valid():
        #enviar e-mail
        nome = request.POST.get('nome','')
        email = request.POST.get('email','')
        mensagem = request.POST.get('mensagem','')
        email = EmailMessage(
            "Mensagem de Cursos Online",
            "De {} <{}> Escreveu: \n\n{}".format(nome,email,mensagem),
            "nao-responder@inbox.mailtrap.io",
            ["cursos_online@cursos_online.com"],
            reply_to=[email]     
        )

        try:
            email.send()
            send = True
        except:
            send = False       
        
        form = FormContatoCurso()
        
    context = {
        'form':form,
        'success':send
    }
    return render(request,'cursos/contato_curso.html',context)   



@login_required
def enrollment(request, slug):
    curso = get_object_or_404(Cursos, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        usuario=request.user, 
        curso=curso,
    )
    if created:
        enrollment.ativo()
        messages.success(request, 'Inscrição realizada com sucesso!!!')
    else:
        messages.info(request, 'Usuário já inscrito neste curso.')
    return redirect('accounts:painel')



@login_required
def anuncios(request, slug):
    curso = get_object_or_404(Cursos, slug=slug)
    if not request.user.is_staff:
        enrollment = get_object_or_404(
            Enrollment,
            usuario = request.user,
            curso = curso
        )
        if not enrollment.aprovado():
            messages.error(request, 'A sua inscrição está pendente')
            return redirect('accounts:painel')
    template_name = 'cursos/anuncios.html'
    context = {
        'curso': curso,
    }
    return render(request, template_name, context)


