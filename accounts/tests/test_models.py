from django.test import TestCase
from ..models import User


class CreateNewUser(TestCase):
    # executa sempre antes de iniciar o teste
    def setUp(self):
        User.objects.create(
            username='Username',
            email = 'usuario@us.com',
            name = 'Name',
        )
    
    def test_filtra_username_e_printa_o_que_foi_cadastrado(self):
        teste_cadastro = User.objects.get(username='Username')
        self.assertEquals(teste_cadastro.__str__(), 'Name')
        print('Teste que cria novo usuário:\n'
            'Name:', teste_cadastro.name,'\n'
            'Username:', teste_cadastro.username,'\n'
            'Email:', teste_cadastro.email,
        )