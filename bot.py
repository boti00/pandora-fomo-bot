import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuración
TOKEN = os.getenv('BOT_TOKEN')

# Configurar logging
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🤖 **PandoraFOMO Bot Activado**\n\n'
        '✅ _Sistema de señales 24/7 operativo_\n'
        '📰 _Noticias de alto impacto_\n'
        '🚨 _Alertas en tiempo real_\n\n'
        '⌛ _Preparando primer reporte..._'
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('✅ **Bot Operativo** - Sistema de monitorización activo 24/7')

def main():
    # Crear aplicación
    application = Application.builder().token(TOKEN).build()
    
    # Comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    
    # Iniciar bot
    application.run_polling()
    print("🤖 Bot iniciado correctamente")

if __name__ == '__main__':
    main()
