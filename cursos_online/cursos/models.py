from django.db import models
from django.urls import reverse
from django.utils import timezone



class CursosManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains = query) | \
            models.Q(description__icontains = query)
        )
# o models.Q() é uma espécie de filtro ( | sgnifica ou e & significa e)


class Cursos(models.Model):

    nome = models.CharField('Nome', max_length = 100)
    slug = models.SlugField('Atalho')
    descricao = models.TextField('Descrição Simples', blank = True)
    sbore = models.TextField('Sobre o Curso', blank = True)
    start_date = models.DateField(
        'Data de início', null = True, blank = True, 
        )
    imagem = models.ImageField(
        upload_to = 'cursos/imagens', verbose_name = 'Imagem',
        null = True, blank = True
        )
    created_at = models.DateTimeField('Criado em', auto_now_add = True)
    updated_at = models.DateTimeField('Atualizado em ', auto_now_add = True)
    
    objects = CursosManager()

    def __str__(self):
        return self.nome

    # def get_absolute_url(self):
    #     return reverse('cursos:details', args = [self.slug])

    # def release_lessons(self):
    #     today = timezone.now().date()
    #     return self.lessons.filter(release_date__gte = today)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome'] # ['-name'] ordem decrescente
    

