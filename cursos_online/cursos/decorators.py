from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Cursos, Enrollment

def inscrição_required(view_func):
    def _wrapper(request, *args, **kwargs):
        slug = kwargs['slug']
        curso = get_object_or_404(Cursos, slug=slug)
        has_permission = request.user.is_staff
        if not has_permission:
            try:
                enrollment = Enrollment.objects.get(
                    user=request.user, curso=curso
                )
            except Enrollment.DoesNotExist:
                message = 'Desculpe, você ainda não está inscrito para este curso.'
            else:
                if enrollment.aprovado():
                    has_permission = True
                else:
                    message = 'A sua inscrição no curso ainda está pendente'
        if not has_permission:
            messages.error(request, message)
            return redirect('accounts:dashboard')
        request.curso = curso
        return view_func(request, *args, **kwargs)
    return _wrapper