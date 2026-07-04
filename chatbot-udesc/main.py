import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from handlers.language import escolher_idioma
from handlers.menu import menu_principal, tratar_menu_principal
from data.centros import CENTROS
from data.sistemas import SISTEMAS

usuarios = {
    8966013007: {
        "language": None,
        "state": "escolhendo_idioma"
    }
}

load_dotenv()

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("não foi encontrado o token")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    

    usuarios[user_id] = {
        "language" : None,
        "state" : "escolhendo_idioma"
    }

    await update.message.reply_text(
        escolher_idioma()
    )


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    mensagem = update.message.text.strip()

    usuario = usuarios.get(user_id)
    estado = usuario["state"]

    if estado == "escolhendo_idioma":
        if mensagem == "1":

            usuario["language"] = "pt"
            usuario["state"] = "menu_principal"

            await update.message.reply_text(
                "Idioma definido como Português"
            )
            await update.message.reply_text(
                menu_principal("pt")
            )

        elif mensagem == "2":

            usuario["language"] = "en"
            usuario["state"] = "menu_principal"

            await update.message.reply_text(
                "Language set to English 🇺🇸"
            )
            await update.message.reply_text(
                menu_principal("en")
            )

        elif mensagem == "3":

            usuario["language"] = "es"
            usuario["state"] = "menu_principal"

            await update.message.reply_text(
                "Idioma cambiado a Español 🇪🇸"
            )
            await update.message.reply_text(
                menu_principal("es")
            )            

    elif estado == "menu_principal":

        resposta = tratar_menu_principal(
            mensagem,
            usuario["language"]
        )

        usuario["state"] = resposta["estado"]

        await update.message.reply_text(
            resposta["mensagem"]
        )

    elif estado == "menu_centros":

        if mensagem in CENTROS:

            centro = CENTROS[mensagem]

            resposta = (
                f"{centro['nome']}\n\n"
                f"Cidade: {centro['cidade']}\n"
                f"Site: {centro['site']}"
            )

            await update.message.reply_text(resposta)

            usuario["state"] = "menu_principal"

            await update.message.reply_text(
                menu_principal(usuario["language"])
            )

        else:
            await update.message.reply_text(
                "Centro inválido. Escolha um número da lista."
            )

    elif estado == "menu_sistemas":

        if mensagem in SISTEMAS:

            sistema = SISTEMAS[mensagem]

            resposta = (
                f"{sistema['nome']}\n\n"
                f"Descrição:\n{sistema['descricao']}\n\n"
                "Requisitos:\n"
            )

            for requisito in sistema["requisitos"]:
                resposta += f"- {requisito}\n"

            resposta += f"\nAcesso:\n{sistema['link']}"

            await update.message.reply_text(resposta)

            usuario["state"] = "menu_principal"

            await update.message.reply_text(
                menu_principal(usuario["language"])
            )

        else:

            await update.message.reply_text(
                "Sistema inválido. Escolha uma opção da lista."
            )

    else:

        await update.message.reply_text(
            "Escolha 1, 2 ou 3."
        )



app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot iniciado!")

app.run_polling()