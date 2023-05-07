from aiogram import Bot, Dispatcher, executor, types
API_TOKEN="6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем. 
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Эхо-бот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.") #Так как код работает асинхронно, то обязательно пишем await.
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
