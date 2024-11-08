# Plataforma de Cursos Online

Este projeto desenvolve uma plataforma de cursos online onde alunos podem se inscrever em cursos disponíveis, acessar materiais, e interagir através de comentários. Oferece também um painel com dados pessoais e cursos ativos ou concluídos.

## Funcionalidades

- **Inscrição em Cursos:** Alunos podem explorar e se inscrever em cursos.
- **Dashboard Pessoal:** Exibe dados do aluno, cursos inscritos e completados.
- **Comentários:** Espaço para feedback e interações.
- **Materiais do Curso:** Suporte para arquivos e vídeos disponibilizados pelos instrutores.

## Estrutura do Projeto

### Models

1. **User**: Gerencia dados de login e perfil do aluno, incluindo cursos inscritos e progresso.
2. **Curso**: Armazena informações de cada curso, como título, descrição e instrutores.
3. **Material**: Vincula recursos (arquivos, vídeos) ao curso, disponibilizando-os aos alunos.
4. **Comentário**: Permite que alunos deixem feedback, criando um histórico de interação.
5. **Inscrição**: Controla a participação e o status de cada aluno nos cursos.

### Aplicações

- **Educação a Distância**: Ideal para escolas e instrutores independentes que desejam disponibilizar cursos online.
- **Gerenciamento de Conteúdo**: Permite organizar, gerenciar e compartilhar materiais de forma centralizada.
  
## Tecnologias

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Banco de Dados**: SQLite

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/carlosalbertoprojetos/cursos_online.git
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

Acesse em `http://127.0.0.1:8000`.

## Contribuições

Contribuições são bem-vindas! Abra uma issue ou envie um pull request para sugestões e melhorias.