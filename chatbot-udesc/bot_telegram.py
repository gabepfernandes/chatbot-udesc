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
import chatbot

load_dotenv()

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("não foi encontrado o token")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    respostas = chatbot.iniciar(user_id)
    for resposta in respostas:
        await update.message.reply_text(resposta)


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    mensagem = update.message.text

    respostas = chatbot.responder(user_id, mensagem)
    for resposta in respostas:
        await update.message.reply_text(resposta)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot iniciado!")

app.run_polling()
