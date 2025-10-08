# Projeto Pizzaria

**Projeto final do curso de Programação em Python para Web – SENAC Campo Grande RJ**

---

## 🏷️ Descrição

Este projeto consiste em uma aplicação web para gerenciar pizzaria: cadastro de clientes, cardápio, controle de pedidos, itens de pedido, etc. Permite que usuários façam pedidos e que administradores visualizem e gerenciem esses pedidos.

O objetivo é demonstrar conceitos aprendidos no curso, como Django (ou framework usado), modelos, migrações, rotas, views, templates, etc.

---

## 📂 Estrutura do Projeto / Organização

Aqui está um esboço das principais pastas e arquivos do projeto:

projeto_pizzaria/
│
├── itens_pedido/ # app para itens dos pedidos
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ └── …
│
├── pedido/ # app para pedidos
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ └── …
│
├── manage.py
├── requirements.txt
├── …

yaml
Copiar código

Você pode detalhar cada app (o que contém, quais models) se quiser para o avaliador.

---

## 🛠️ Tecnologias e Dependências

Algumas tecnologias usadas:

- **Python 3.x**  
- **Django** (ou framework web que você usou)  
- Banco de dados (SQLite ou outro usado)  
- Outras dependências (listar no `requirements.txt`)

Certifique-se que o arquivo `requirements.txt` contém todas as bibliotecas necessárias.

---

## 🔧 Como instalar / rodar localmente

Passo a passo para configurar o projeto em sua máquina:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Luandesson/projeto_pizzaria.git
   cd projeto_pizzaria
(Opcional) criar ambiente virtual:

bash
Copiar código
python -m venv venv
# no Windows
venv\Scripts\activate
# no Linux/macOS
source venv/bin/activate
Instalar dependências:

bash
Copiar código
pip install -r requirements.txt
Executar migrações:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
Criar superusuário (para acessar painel admin, se aplicável):

bash
Copiar código
python manage.py createsuperuser
Rodar o servidor de desenvolvimento:

bash
Copiar código
python manage.py runserver
Acesse no navegador:

cpp
Copiar código
http://127.0.0.1:8000/
