# 🔐 Login App com Flask

Este é um projeto de autenticação simples desenvolvido com **Python (Flask)**, **HTML**, **CSS** e **SQLite**.
Ele permite que usuários se cadastrem e façam login, com mensagens de feedback e segurança básica implementada.
---

## 🚀 Funcionalidades

- Cadastro de usuários com validação
- Login com verificação de credenciais
- Mensagens de sucesso, erro e alerta via `flash`
- Banco de dados SQLite com criação automática
- Estrutura organizada com pastas `templates`, `static` e `database`
- Senhas criptografadas com `werkzeug.security`
- Chave secreta protegida via `.env`
---

## 🧰 Tecnologias utilizadas

- Python 3
- Flask
- SQLite
- HTML5
- CSS3
- dotenv
---

# 🎨 Interface Web — Login e Cadastro

Este é o front-end do projeto **Login App**, desenvolvido com **HTML5**, **CSS3** e um toque de **JavaScript** para validação de senha.
A interface é moderna, responsiva e pensada para oferecer uma experiência clara e intuitiva ao usuário.
---

## 🖼️ Visual

- Layout centralizado com fundo temático de supermercado
- Formulários de login e cadastro com campos bem definidos
- Feedback visual para senha fraca ou forte
- Mensagens de alerta estilizadas por categoria (sucesso, erro, aviso)
- Logo da empresa centralizada no topo
---

## 🧪 Funcionalidades interativas

- Validação de senha em tempo real (mínimo de 12 caracteres)
- Ícones dinâmicos ✅❌ para indicar força da senha
- Mensagens de feedback via `flash` integradas ao Flask
- Link para recuperação de senha (a ser implementado)
---

## 🧰 Tecnologias utilizadas

- HTML5
- CSS3
- JavaScript (vanilla)
- Flask (para renderização dinâmica)
---
## 📁 Estrutura de pastas

login_app/ 
├── static/ 
│ └── style.css 
├── templates/ 
│ └── index.html 
├── database/ 
│ └── usuarios.db 
├── .env 
├── .gitignore 
└── app.py
