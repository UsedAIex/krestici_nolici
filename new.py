import logging
import random

from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Updater, Filters

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = '5304987949:AAGA1UhT-0deO0xHF5bHTMNA0T_YRjSk8NM'

def start(update, context):
    update.message.reply_text(
        "Работает только ссылка \nhttps://ce41-79-165-120-167.eu.ngrok.io\n"
        "И то ее нужно каждый раз обновлять"
    )




def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
