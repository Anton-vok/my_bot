import telegram

bot = telegram.Bot(token="6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")

group_link = "https://t.me/+rZ1pyV99Ad8wOTAy"
group_id = bot.get_chat_id(group_link)

def start_command(update, context):
    update.message.reply_text('Привет. Я создан для раздачи ролей в ролевой игре "The Adventurers Guild".')
    update.message.reply_text("https://t.me/GenRolACHV")
    update.message.reply_text("Если ты сейчас напишешь /new, бот отправит тебе твою роль.")
    update.message.reply_text("Если что-то не работает, сообщи мне: @A_CH_V")
    update.message.reply_text("(пожалуйста, не ломайте ничего, он и так сделан на коленке)")

def repeat_command(update, context):
  update.message.reply_text(update.message.text)

def new_command(update, context):
  if update.effective_chat.id == group_id:
    update.message.reply_text("Hello!")
  else:
    update.message.reply_text("Bye!")

bot.add_command("start", start_command)
bot.add_command("repeat", repeat_command)
bot.add_command("new", new_command)

bot.start()
