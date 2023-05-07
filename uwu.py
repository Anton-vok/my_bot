import telegram

bot = telegram.Bot(token="6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")

def start_command(update, context):
    update.message.reply_text('Привет. Я создан для раздачи ролей в ролевой игре "The Adventurers Guild".')
    update.message.reply_text("https://t.me/GenRolACHV")
    update.message.reply_text("Если ты сейчас напишешь /new, бот отправит тебе твою роль.")
    update.message.reply_text("Если что-то не работает, сообщи мне: @A_CH_V")
    update.message.reply_text("(пожалуйста, не ломайте ничего, он и так сделан на коленке)")

bot.add_command("start", start_command)

bot.start()
