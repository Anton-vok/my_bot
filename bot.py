import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Не забудь вставить свой токен API в следующей строке
API_TOKEN = '6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo'

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет!')


# Обработчик команды /new
def new(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Новый!')

# Функция main, в которой запускается бот
def main() -> None:
    updater = Updater(API_TOKEN)

    dispatcher = updater.dispatcher

    # Регистрация обработчиков команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("new", new))

    # Запуск бота
    updater.start_polling()

    # Запуск бота до принудительной остановки
    updater.idle()

if __name__ == '__main__':
    main()
