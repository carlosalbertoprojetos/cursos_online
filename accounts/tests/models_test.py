from django.test import TestCase
# from ..models import User


# class CreateNewUser(TestCase):
#     # executa sempre antes de iniciar o teste
#     def setUp(self):
#         User.objects.create(
#             username='Username',
#             email = 'usuario@us.com',
#             name = 'Name',
#         )
    
#     def test_filtra_username_e_printa_o_que_foi_cadastrado(self):
#         teste_cadastro = User.objects.get(username='Username')
#         self.assertEquals(teste_cadastro.__str__(), 'Name')
#         print('Teste que cria novo usuário:\n'
#             'Name:', teste_cadastro.name,'\n'
#             'Username:', teste_cadastro.username,'\n'
#             'Email:', teste_cadastro.email,
#         )


# class UpdateNewUser(TestCase):
#     # executa sempre antes de iniciar o teste
#     def setUp(self):
#         User.objects.create(
#             username='Username',
#             email = 'usuario@us.com',
#             name = 'Name',
#         )
    
#     def test_filtra_username_altera_dados_e_printa_o_que_foi_alterado(self):
#         teste_cadastro = User.objects.get(username='Username')
#         self.assertEquals(teste_cadastro.__str__(), 'Name')
#         teste_cadastro2 = {'username': 'UsernameTeste', 'email': 'usuarioteste@us.com', 'name': 'NameTeste'}
#         print('Teste que altera dados do novo usuário:\n'
#             'Name:', teste_cadastro2.name,'\n'
#             'Username:', teste_cadastro2.username,'\n'
#             'Email:', teste_cadastro2.email,
#         )

from ..models import User

class CreateNewUser(TestCase):
    # executa sempre antes de iniciar o teste
    def setUp(self):
        User.objects.create(
            username='Username',
            email = 'usuario@us.com',
            name = 'Name',
        )

    def test():
        User.objects.create(
            username='Username',
            email = 'usuario@us.com',
            name = 'Name',
        )
    teste_cadastro = User.objects.get(username='Username')
    print('Teste que altera dados do novo usuário:\n'
        'Name:', teste_cadastro.name,'\n'
        'Username:', teste_cadastro.username,'\n'
        'Email:', teste_cadastro.email,
        )