from django.conf import settings
from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from model_mommy import mommy


from cursos.models import Cursos


class CourseManagerTestCase(TestCase):

    def setUp(self):
        # nome da app.nome do model
        self.cursos_django = mommy.make(
            'cursos.Cursos', nome='Python na web com Django', _quantity=10)
        self.cursos_java = mommy.make(
            'cursos.Cursos', nome='JavaScript python', _quantity=10)
        self.client = Client()

    def tearDown(self):
        # for curso in self.cursos:
        #     curso.delete()
        Cursos.objects.all().delete()

    def test_curso_search(self):
        search = Cursos.objects.search('django')
        self.assertEqual(len(search), 10)
        search = Cursos.objects.search('JavaScript')
        self.assertEqual(len(search), 10)
        search = Cursos.objects.search('python')
        self.assertEqual(len(search), 20)