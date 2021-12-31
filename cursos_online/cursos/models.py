from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class CursosManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )
# o models.Q() é uma espécie de filtro ( | sgnifica 'OU' e & significa 'E')


class Cursos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    descricao = models.TextField('Descrição Simples', blank=True)
    sobre = models.TextField('Sobre o Curso', blank=True)
    data_inicial = models.DateField(
        'Data de início', null=True, blank=True,
    )
    imagem = models.ImageField(
        upload_to='cursos/imagens', verbose_name='Imagem',
        null=True, blank=True
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em ', auto_now_add=True)

    objects = CursosManager()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('cursos:detalhes_curso', args=[self.slug])

    # def release_lessons(self):
    #     today = timezone.now().date()
    #     return self.lessons.filter(release_date__gte = today)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']  # ['-name'] ordem decrescente


class Enrollment(models.Model):

    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
        (3, 'Recusado'),
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        related_name='enrollments',
        on_delete=models.DO_NOTHING
    )
    curso = models.ForeignKey(
        Cursos, verbose_name='Curso',
        related_name='enrollments',
        on_delete=models.DO_NOTHING
    )
    status = models.ImageField(
        'Situação',
        choices=STATUS_CHOICES,
        default=0,
        blank=True
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em ', auto_now_add=True)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        """ 
        unique_together/unicidade - combina a unicidade entre cursos e usuário,
        ou seja, cada usuário se increve apenas uma vez para cada curso.
        """
        unique_together = (('usuario', 'curso'),)

    def ativo(self):
        self.status = 1
        self.save()

    def aprovado(self):
        return self.status == 1

    def __str__(self):
        return self.usuario


class Anuncios(models.Model):
    curso = models.ForeignKey(
        Cursos,
        verbose_name='Curso',
        related_name='anuncios',
        on_delete=models.DO_NOTHING
    )
    titulo = models.CharField('Título', max_length=100)
    conteudo = models.TextField('Conteúdo', blank=True)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'
        ordering = ['-criado_em']


class Comentarios(models.Model):
    anuncio = models.ForeignKey(
        Anuncios, verbose_name='Anúncio', related_name='comentarios',
        on_delete=models.DO_NOTHING
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        on_delete=models.DO_NOTHING
    )
    comentario = models.TextField('Comentário', blank=True)

    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['-criado_em']

    def __str__(self):
        return str(self.anuncio.curso)
