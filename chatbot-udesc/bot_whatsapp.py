from neonize.client import NewClient
from neonize.events import ConnectedEv, MessageEv, PairStatusEv
import chatbot
from utils.usuarios import usuarios

cliente = NewClient("sessao_whatsapp.sqlite3")


@cliente.event(ConnectedEv)
def ao_conectar(cliente: NewClient, evento: ConnectedEv):
    print("WhatsApp conectado!")


@cliente.event(PairStatusEv)
def ao_parear(cliente: NewClient, evento: PairStatusEv):
    print("Conectado como", evento.ID.User)


@cliente.event(MessageEv)
def ao_receber_mensagem(cliente: NewClient, evento: MessageEv):
    if evento.Info.MessageSource.IsFromMe:
        return

    mensagem = evento.Message.conversation or evento.Message.extendedTextMessage.text
    if not mensagem:
        return

    chat = evento.Info.MessageSource.Chat
    user_id = str(evento.Info.MessageSource.Sender)

    if user_id not in usuarios:
        respostas = chatbot.iniciar(user_id)
    else:
        respostas = chatbot.responder(user_id, mensagem)

    for resposta in respostas:
        cliente.send_message(chat, resposta)


print("Iniciando o WhatsApp... leia o QR Code abaixo com o celular.")

cliente.connect()
