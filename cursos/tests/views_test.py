# from django.conf import settings
# from django.core import mail
# from django.test import TestCase
# from django.test.client import Client
# from django.urls import reverse

# from cursos.models import Cursos


# class ContactCursoTestCase(TestCase):
    
#     def setUp(self):
#         self.curso = Cursos.objects.create(nome='Name_test', slug="Slug_test")

#     def tearDown(self):
#         self.curso.delete()
    
#     # @classmethod
#     # def setUpClass(cls):
#     #     pass
    
#     # @classmethod
#     # def tearDownClass(cls):
#     #     pass
    
#     def test_contact_form_error(self):
#         data = {'nome': 'Nome_Contato_test', 'email':'', 'mensagem':''}
#         client = Client()
#         path = reverse('cursos:detalhes_curso', args=[self.curso.slug])
#         response = client.post(path, data)
#         self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.') 
#         self.assertFormError(response, 'form', 'mensagem', 'Este campo é obrigatório.')
        
#     def test_contact_form_success(self):
#         data = {'nome': 'Nome_Contato_test', 'email':'test@test.com', 'mensagem':'Testing success'}
#         client = Client()
#         path = reverse('cursos:detalhes_curso', args=[self.curso.slug])
#         response = client.post(path, data)
#         self.assertEqual(len(mail.outbox), 1)
#         self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])
#         # .to verifica para quem o email foi enviado, mas também pode ser para .subject, .body, etc
        

