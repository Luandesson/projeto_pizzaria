# 🍕 Projeto Pizzaria

**Projeto Final – Curso de Programação em Python para Web**  
**SENAC Campo Grande – RJ**

---

## 💡 Sobre o Projeto

O **Projeto Pizzaria** é uma aplicação web desenvolvida como trabalho final do curso **Programação em Python para Web** do **Senac Campo Grande (RJ)**.  
O objetivo é demonstrar os conhecimentos adquiridos no desenvolvimento de sistemas web utilizando **Python**, **Django** e boas práticas de programação.

A aplicação permite gerenciar pedidos de uma pizzaria, incluindo:
- Cadastro de clientes  
- Controle de pedidos e itens  
- Visualização de pedidos no painel administrativo  
- Estrutura escalável e organizada em apps Django  

---

## 🧠 Tecnologias Utilizadas

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,django,html,css,bootstrap,git,github,vscode" />
  </a>
</p>

```

## 🧩 Estrutura do Projeto

projeto_pizzaria/
│
├── itens_pedido/ # App responsável pelos itens do pedido
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ └── admin.py
│
├── pedido/ # App responsável pelo controle de pedidos
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ └── admin.py
│
├── manage.py
├── requirements.txt
└── ...
```

## ⚙️ Como Executar o Projeto

### 1️⃣ Clone o repositório:
```bash
git clone https://github.com/Luandesson/projeto_pizzaria.git
cd projeto_pizzaria
2️⃣ Crie e ative o ambiente virtual:
bash
Copiar código
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/macOS
source venv/bin/activate
3️⃣ Instale as dependências:
bash
Copiar código
pip install -r requirements.txt
4️⃣ Aplique as migrações:
bash
Copiar código
python manage.py makemigrations
python manage.py migrate
5️⃣ Crie um superusuário:
bash
Copiar código
python manage.py createsuperuser
6️⃣ Rode o servidor:
bash
Copiar código
python manage.py runserver
Depois, acesse:
👉 http://127.0.0.1:8000

🚀 Funcionalidades
✅ Cadastro de clientes e pedidos
✅ Listagem e controle de pedidos
✅ Adição de itens ao pedido
✅ Painel administrativo com Django Admin
✅ Estrutura modular (apps independentes)
✅ Código limpo e organizado

🖼️ Demonstração (prints sugeridos)
Adicione prints reais aqui para deixar o README mais atrativo.

Exemplo:

Tela de Pedidos	Painel Administrativo

👨‍💻 Autor
Luandesson Alves
📍 Campo Grande – Rio de Janeiro
📘 Projeto desenvolvido no SENAC Campo Grande RJ
🌐 GitHub
✉️ alves.luandesson@gmail.com

🧾 Licença
Este projeto está sob a licença MIT.
Sinta-se livre para estudar, modificar e utilizar para fins educacionais.

⭐ Agradecimentos
A todos os professores e colegas do curso Programação em Python para Web – SENAC Campo Grande RJ,
pelo apoio, incentivo e compartilhamento de conhecimento durante todo o aprendizado.
