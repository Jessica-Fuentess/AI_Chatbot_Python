# 🤖 AI Chatbot com Python, OpenAI e Streamlit jh

Projeto de **Chatbot com Inteligência Artificial** desenvolvido em **Python**, utilizando a **API da OpenAI** e o framework **Streamlit** para construção de uma interface web interativa.  
O sistema permite que usuários enviem mensagens em tempo real e recebam respostas geradas por um modelo de linguagem, mantendo o histórico da conversa durante a sessão.

Este projeto demonstra, na prática, **integração com APIs**, **gerenciamento de estado**, **engenharia de prompts**, **estruturação de dados em listas e dicionários**, além da criação de aplicações web voltadas a **IA aplicada**.

---

## 🎯 Objetivo do Projeto

- Construir um **chatbot funcional com IA generativa**
- Integrar Python com a **API da OpenAI**
- Criar uma **interface web simples e interativa**
- Gerenciar histórico de conversas com **estado de sessão**
- Demonstrar aplicação prática de IA em produtos digitais

---

## 🧠 Visão Geral da Solução

O chatbot funciona da seguinte forma:

1. O usuário digita uma mensagem no chat
2. A mensagem é exibida na interface
3. O histórico completo da conversa é enviado à API da OpenAI
4. O modelo de IA gera uma resposta contextual
5. A resposta é exibida na tela
6. O histórico é mantido durante toda a sessão

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Streamlit** — Interface web interativa
- **OpenAI API** — Modelo de linguagem (GPT)
- **Estruturas de dados** (listas e dicionários)
- **Gerenciamento de estado** (`st.session_state`)

---

## 📂 Estrutura do Repositório
```
AI_Chatbot_Python/
│
├── main.py        # Aplicação principal do chatbot
├── auxiliar.py    # Exemplos e apoio conceitual (listas e dicionários)
└── README.md      # Documentação do projeto
```

---

## ▶️ Demonstração do Processo

1. O script `main.py` é iniciado via Streamlit  
2. Uma interface web é aberta automaticamente no navegador  
3. O usuário digita uma mensagem no chat  
4. A mensagem é armazenada no histórico da sessão  
5. A conversa é enviada para a API da OpenAI  
6. A IA gera uma resposta contextual  
7. A resposta é exibida no chat em tempo real  

---

## 🚀 Como Executar o Projeto

- Ter o **Python 3.9 ou superior** instalado
- Ter uma **chave de API da OpenAI**
- Criar um ambiente virtual (opcional, mas recomendado):
  - `python -m venv venv`
  - Ativar o ambiente:
    - Linux/macOS: `source venv/bin/activate`
    - Windows: `venv\Scripts\activate`
- Instalar as dependências do projeto:
  - `pip install streamlit openai`
- Configurar a variável de ambiente com a chave da OpenAI:
  - Linux/macOS: `export OPENAI_API_KEY="sua_api_key_aqui"`
  - Windows (PowerShell): `setx OPENAI_API_KEY "sua_api_key_aqui"`
- Executar a aplicação:
  - `streamlit run main.py`
- Após a execução, o Streamlit abrirá automaticamente a aplicação no navegador

---

## 🧩 Principais Conceitos Aplicados

- Integração com **APIs REST**
- **IA Generativa** aplicada
- Persistência de estado em aplicações web
- Estruturação de mensagens (`role` / `content`)
- Boas práticas de separação de responsabilidades
- Desenvolvimento de produtos com foco no usuário

---

## 📊 Aplicações Práticas

Este projeto é facilmente adaptável para:

- Chatbots corporativos
- Assistentes de atendimento
- Ferramentas internas de suporte
- Prototipação de produtos com IA
- Integração com pipelines de dados e analytics
- Camada conversacional para sistemas de BI e Data Products

---

## 📬 Contato
Fico à disposição para conversar sobre este projeto, oportunidades na área de **Dados, BI, Engenharia ou Ciência de Dados**, e novos desafios em tecnologia.

- 💼 LinkedIn: [Jéssica Fuentes](https://www.linkedin.com/in/j%C3%A9ssica-fuentes/)
