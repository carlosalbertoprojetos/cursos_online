from django.template import Library

register = Library()

from cursos.models import Enrollment

@register.inclusion_tag('cursos/templatetags/meus_cursos.html')
def meus_cursos(user):
    enrollments = Enrollment.objects.filter(usuario=user)
    context = {
        'enrollments': enrollments
    }
    return context


@register.simple_tag
def load_meus_cursos(usuario):
    return Enrollment.objects.filter(usuario=usuario)
    


