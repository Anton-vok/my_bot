import telebot
bot=telebot.TeleBot("6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")
@bot.message_handler(commands=['start'])
def echo(message):
  bot.send_message(message.chat.id,"Привет")
@bot.message_hendler(commands=["new"])
def new(message):
  bot.send_message(message.chat.id,"ты ввел /new")
bot.polling(none_stop=True)
