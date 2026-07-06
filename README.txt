==============================================
CHATBOT UDESC
==============================================

Chatbot para ajudar estudantes estrangeiros que vem fazer intercambio na UDESC.
Ele responde duvidas sobre os centros, sistemas da universidade, como obter o ID
UDESC e o CPF, tutoria, SOE e residencia estudantil.

O mesmo chatbot funciona em duas plataformas: Telegram e WhatsApp. A parte que
"pensa" (menus e respostas) e a mesma para as duas, entao qualquer mudanca nos
textos aparece nos dois lugares.

O bot atende em tres idiomas: Portugues, Ingles e Espanhol.


----------------------------------------------
O QUE VOCE PRECISA ANTES DE COMECAR
----------------------------------------------

- Python 3 instalado na maquina.
  Para conferir, abra o terminal e digite:
    python --version      (no Windows)
    python3 --version     (no Linux/Mac)
  Se aparecer um numero de versao, esta tudo certo.
  Se nao tiver, baixe em https://www.python.org/downloads/
  (no Windows, marque a opcao "Add Python to PATH" durante a instalacao).

- Conexao com a internet.

- Um token do Telegram (ja vem no arquivo .env do projeto).

- Para o WhatsApp: um celular com WhatsApp para ler o QR Code na primeira vez.


----------------------------------------------
ESTRUTURA DO PROJETO
----------------------------------------------

Os arquivos que importam ficam dentro da pasta chatbot-udesc/chatbot-udesc.
Todos os comandos abaixo devem ser executados DENTRO dessa pasta.

- bot_telegram.py inicia o bot no Telegram
- bot_whatsapp.py inicia o bot no WhatsApp
- chatbot.py      a logica dos menus e respostas (usada pelas duas plataformas)
- handlers/ e data/   textos dos menus e informacoes (centros, sistemas, etc.)
- requirements.txt    lista das bibliotecas que o projeto usa


----------------------------------------------
PASSO 1 - PREPARAR O PROJETO (so na primeira vez)
----------------------------------------------

Aqui a gente cria um "ambiente" separado para instalar as bibliotecas do projeto
sem baguncar o Python do computador. E uma pastinha so com o que este projeto
precisa.

>> No Windows (PowerShell):

    python -m venv venv
    venv\Scripts\pip install -r requirements.txt

>> No Linux ou Mac:

    python3 -m venv venv
    venv/bin/pip install -r requirements.txt

Voce so precisa fazer o Passo 1 uma vez por maquina. Depois disso, e so rodar.


----------------------------------------------
PASSO 2 - RODAR O BOT NO TELEGRAM
----------------------------------------------

>> No Windows:

    venv\Scripts\python bot_telegram.py

>> No Linux ou Mac:

    venv/bin/python bot_telegram.py

Quando aparecer a mensagem "Bot iniciado!", o bot esta no ar. Deixe essa janela
do terminal aberta (se fechar, o bot para).

Agora, no Telegram (pode ser no seu proprio celular), procure pelo bot e mande
/start. Ele vai responder pedindo para escolher o idioma e seguir os menus.

Para parar o bot, aperte Ctrl + C no terminal.


----------------------------------------------
PASSO 3 - RODAR O BOT NO WHATSAPP
----------------------------------------------

O WhatsApp funciona um pouco diferente do Telegram. O numero que voce conectar
VIRA o bot. Ou seja: para testar, voce manda mensagem para esse numero a partir
de OUTRO celular.

>> No Windows:

    venv\Scripts\python bot_whatsapp.py

>> No Linux ou Mac:

    venv/bin/python bot_whatsapp.py

Na primeira vez vai aparecer um QR Code no terminal. Para conectar:

  1. Abra o WhatsApp no celular que vai ser o bot.
  2. Va em Configuracoes > Dispositivos conectados > Conectar um dispositivo.
  3. Aponte a camera para o QR Code que apareceu no terminal.

Quando aparecer "WhatsApp conectado!", esta pronto. Espere alguns segundos (ele
sincroniza as conversas) e entao mande uma mensagem, de OUTRO celular, para o
numero que virou bot. Ele vai responder com o menu de idiomas.

IMPORTANTE: nao feche o terminal nem aperte Ctrl + C logo depois de conectar.
O bot precisa continuar rodando para responder. Se o processo for encerrado logo
apos a conexao, o WhatsApp entende como um logout e sera preciso ler o QR de novo.


----------------------------------------------
DUVIDAS COMUNS
----------------------------------------------

- Apareceu "nao foi encontrado o token" ao rodar o Telegram.
  Falta o arquivo .env na pasta. Ele guarda o token do bot. Crie um arquivo
  chamado .env (dentro de chatbot-udesc/chatbot-udesc) com uma linha assim:
    TOKEN=coloque_aqui_o_token_do_bot

- Copiei o projeto para outro computador e nao roda.
  Nao copie a pasta venv de um computador para o outro, ela nao funciona assim.
  Em cada maquina nova, refaca o Passo 1 (criar o venv e instalar de novo).

- No Windows da erro dizendo que "python3" nao foi encontrado.
  No Windows o comando e so "python", sem o 3.

- O WhatsApp pediu o QR Code de novo.
  E normal quando voce troca de computador ou fica muito tempo sem usar.
  E so ler o QR novamente seguindo o Passo 3.


----------------------------------------------
COMO USAR O CHATBOT (MENUS)
----------------------------------------------

  1. Ao iniciar, o bot pede para escolher o idioma
     (1 Portugues, 2 Ingles, 3 Espanhol).
  2. Depois aparece o menu principal com as opcoes:
       - Endereco dos Centros
       - Sistemas UDESC (SIGA, Moodle, Office 365, Biblioteca, SAS)
       - Como obter o ID UDESC
       - CPF
       - Tutoria
       - SOE (Servico de Orientacao ao Estudante)
       - Residencia Estudantil
  3. Basta digitar o numero da opcao desejada.
  4. A qualquer momento, digite 0 para voltar a escolher o idioma.
