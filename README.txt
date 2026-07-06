CHATBOT UDESC

---
Requisitos para execução:

- Conexão com a internet.
- Python 3 instalado na máquina.
    Para conferir, abra o terminal e digite:
      - python --version (no Windows)
      - python3 --version (no Linux/Mac)
    Se aparecer um numero de versão, está tudo certo.
    Se não, baixe em https://www.python.org/downloads/
    (no Windows, marque a opcao "Add Python to PATH" durante a instalacao).
- Um token do Telegram (ja vem no arquivo .env do projeto).
- Para o WhatsApp: um celular com WhatsApp para ler o QR Code na primeira vez.

---
Estrutura do projeto:

Os arquivos importantes ficam dentro da pasta chatbot-udesc/chatbot-udesc.
- bot_telegram.py: inicia o bot no Telegram
- bot_whatsapp.py: inicia o bot no WhatsApp
- chatbot.py: a lógica dos menus e respostas (usada pelas duas plataformas)
- handlers/ e data/: textos dos menus e informacões (centros, sistemas, etc.)
- requirements.txt: lista das bibliotecas que o projeto usa

---
Passo 1 - Preparar o projeto (no primeiro acesso)

  No Windows (PowerShell):
    python -m venv venv
    venv\Scripts\pip install -r requirements.txt

  No Linux ou Mac:
    python3 -m venv venv
    venv/bin/pip install -r requirements.txt

---
Passo 2 - Rodar o Chatbot no Telegram

  No Windows:
    venv\Scripts\python bot_telegram.py

  No Linux ou Mac:
    venv/bin/python bot_telegram.py

Se aparecer a mensagem "Bot iniciado!", o bot está em execução. Deixe essa janela
do terminal aberta (se fechar, o bot para).

Agora, no Telegram, basta procurar pelo bot e clicar no botão "Iniciar Bot" (ou mandar a mensagem
/start). Ele vai responder pedindo para escolher o idioma e seguir os menus.

Para parar o bot, basta apertar Ctrl + C no terminal.

---
Passo 3 - Rodar o Chatbot no Whatsapp

O WhatsApp funciona um pouco diferente do Telegram. O número que for conectado
vira o bot. Ou seja: para testar, você manda mensagem para esse número a partir
de outro celular.

  No Windows:
    venv\Scripts\python bot_whatsapp.py

  No Linux ou Mac:
    venv/bin/python bot_whatsapp.py

Aparecerá um QR Code no terminal. Para conectar:
  1. Abra o WhatsApp no celular que vai ser o bot.
  2. Vá nos três pontinhos > Dispositivos conectados > Conectar dispositivo.
  3. Aponte a câmera para o QR Code que apareceu no terminal.

Quando aparecer "WhatsApp conectado!", está pronto. Espere alguns segundos (ele
sincroniza as conversas) e então mande uma mensagem, de outro celular, para o
número que virou bot. Ele vai responder com o menu de idiomas.

Para parar o bot, basta apertar Ctrl + C no terminal.
