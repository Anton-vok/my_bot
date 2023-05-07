import telebot;
bot = telebot.TeleBot('%ваш токен%');
bot = telebot.TeleBot(token="6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.chat.id,"Привет. Я создан для раздачи ролей в ролевой игре 'The Adventurers Guild'.")
    bot.send_message(message.chat.id,"https://t.me/GenRolACHV")
    bot.send_message(message.chat.id,"Если ты сейчас напишешь /new, бот отправит тебе твою роль.")
    bot.send_message(message.chat.id,"Если что-то не работает, сообщи мне: @A_CH_V")
    bot.send_message(message.chat.id,"(пожалуйста, не ломайте ничего, он и так сделан на коленке)")
