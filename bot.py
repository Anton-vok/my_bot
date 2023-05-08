import telebot
bot=telebot.TeleBot("6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")
import random

history = []
min_players = 2
roles = [
    ["one", 1, None, 20],
    ["two", 1, 3, 80]
]
history_user = []

def generate_random_role(min_calls, role_history, role_rules):
    total_prob = sum([rule[3] for rule in role_rules])
    if total_prob != 100:
        raise ValueError("Сумма вероятностей всех ролей должна равняться 100%")

    if len(role_history) < min_calls:
        needed_roles = [rule for rule in role_rules if role_history.count(rule[0]) < rule[1]]
        if needed_roles:
            return random.choice(needed_roles)[0]

    while True:
        chosen_role = random.choices(role_rules, weights=[rule[3] for rule in role_rules])[0]
        if chosen_role[2] is None or role_history.count(chosen_role[0]) < chosen_role[2]:
            return chosen_role[0]





@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет. Я создан для раздачи ролей в ролевой "The Adventurers Guild".')
    bot.send_message(message.chat.id,"https://t.me/GenRolACHV")
    bot.send_message(message.chat.id,"Если ты сейчас напишешь /new, бот отправит тебе твою роль.\nЕсли что-то не работает, сообщи мне: @A_CH_V\nпожалуйста, не ломайте ничего, он и так сделан на коленке)")
@bot.message_handler(commands=['new'])
def new(message):
    rol = generate_random_role(history, min_players, roles)  # Изменена переменная 'rol'
    text = f"твоя роль - {rol}"
    bot.send_message(message.chat.id, text)
bot.polling(none_stop=True)
