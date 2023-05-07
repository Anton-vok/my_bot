import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет!")

def main():
    # Создаем объект Updater и передаем ему токен бота
    updater = Updater("<your_bot_token_here>", use_context=True)

    # Получаем объект диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при получении сигнала SIGINT (Ctrl+C в терминале)
    updater.idle()

if __name__ == '__main__':
    main()
