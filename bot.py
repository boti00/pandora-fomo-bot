
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask

# Configuración
TOKEN = os.getenv('BOT_TOKEN')
PORT = int(os.environ.get('PORT', 5000))

app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🤖 **PandoraFOMO Bot Activado**\n\n'
        '✅ _Sistema de señales 24/7 operativo_\n'
        '📰 _Noticias de alto impacto_\n'
        '🚨 _Alertas en tiempo real_\n\n'
        '⌛ _Configuración completada_'
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('✅ **Bot Operativo** - Sistema de monitorización activo 24/7')

@app.route('/')
def home():
    return "🤖 PandoraFOMO Bot - ONLINE"

def main():
    # Crear aplicación
    application = Application.builder().token(TOKEN).build()
    
    # Comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    
    # Iniciar bot en Render (con webhook)
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://pandora-fomo-bot.onrender.com/{TOKEN}"
    )

if __name__ == '__main__':
    main()
