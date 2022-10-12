from django.test import TestCase
from .models import User

class CreateNewUser(TestCase):
    # executa sempre antes de iniciar o teste
    def setUp(self):
        User.objects.create(
            username='Username',
            email = 'usuario@us.com',
            name = 'Name',
        )
    
    def test_cadastro_conta(self):
        teste_cadastro = User.objects.get(username='Username')
        self.assertEquals(teste_cadastro.__str__(), 'Name')
        print(
            'Name:', teste_cadastro.name,'\n'
            'Username:', teste_cadastro.username,'\n'
            'Email:', teste_cadastro.email,
        )