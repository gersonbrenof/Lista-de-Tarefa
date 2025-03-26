# Tarefas API - Django Rest Framework

## Descrição

Este é um projeto desenvolvido com **Django Rest Framework** que permite o gerenciamento de tarefas. O sistema inclui autenticação, e cada tarefa está associada a um usuário. O projeto oferece funcionalidades **CRUD** (Criar, Ler, Atualizar e Excluir) para as tarefas, além de gerenciamento de autenticação com **JWT** (JSON Web Token).

## Funcionalidades

- **Autenticação**: Usamos JWT (JSON Web Token) para autenticação e autorização dos usuários.
- **CRUD de Tarefas**:
  - **Criar**: O usuário pode criar novas tarefas.
  - **Ler**: O usuário pode visualizar suas tarefas.
  - **Atualizar**: O usuário pode editar suas tarefas.
  - **Excluir**: O usuário pode excluir suas tarefas.
- **Associação com o Usuário**: Cada tarefa é associada ao usuário que a criou. O sistema garante que apenas o usuário autenticado tenha acesso às suas tarefas.

## Pré-requisitos

Antes de rodar o projeto, é necessário ter instalado:

- **Python** (versão 3.8 ou superior)
- **Django** (versão 3.x ou superior)
- **Django Rest Framework**
- **PostgreSQL** (ou qualquer outro banco de dados configurado)

## Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/usuario/tarefas-api.git
cd tarefas-api
python -m venv venv
source venv/bin/activate   # Para sistemas Linux/Mac
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
