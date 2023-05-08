import telebot
bot=telebot.TeleBot("6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")
import random
from collections import Counter

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,message.chat.id)
bot.polling(none_stop=True)    
