from django.contrib import admin

from .models import Cursos, Enrollment, Anuncios, Comentarios


class CursosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'data_inicial', 'criado_em']
    search_fields = ['nome', 'slug']
    prepopulated_fields = {'slug':('nome',)}
    
    
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'curso', 'status', 'criado_em']
    search_fields = ['usuario', 'curso']


admin.site.register(Cursos, CursosAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)    
    
admin.site.register([Anuncios, Comentarios])
