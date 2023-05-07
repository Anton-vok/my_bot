import telebot
bot=telebot.TeleBot("6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")
@bot.message_handler(commands=['text'])
def echo(message):
  bot.send_message(message,chat.id,message.text)
bot.polling(none_stop=True)
