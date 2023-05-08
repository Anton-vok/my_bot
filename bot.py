import telebot
bot=telebot.TeleBot("6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")
import random
from collections import Counter

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
    
    role_counts = Counter(role_history)
    
    if len(role_history) < min_calls:
        needed_roles = [rule for rule in role_rules if role_counts[rule[0]] < rule[1]]
        
        if needed_roles:
            remaining_calls = min_calls - len(role_history)
            needed_roles.sort(key=lambda x: x[1] - role_counts[x[0]], reverse=True)
            if remaining_calls >= sum([x[1] - role_counts[x[0]] for x in needed_roles]):
                return random.choice(needed_roles)[0]
            
    while True:
        chosen_role = random.choices(role_rules, weights=[rule[3] for rule in role_rules])[0]
        if chosen_role[2] is None or role_counts[chosen_role[0]] < chosen_role[2]:
            return chosen_role[0]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет. Я создан для раздачи ролей в ролевой "The Adventurers Guild".')
    bot.send_message(message.chat.id,"https://t.me/GenRolACHV")
    bot.send_message(message.chat.id,"Если ты сейчас напишешь /new, бот отправит тебе твою роль.\nЕсли что-то не работает, сообщи мне: @A_CH_V\nпожалуйста, не ломайте ничего, он и так сделан на коленке)")
@bot.message_handler(commands=['new'])
def new(message):
    user_name = message.from_user.username
    history_user.append(user_name)
    rol = generate_random_role(min_players, history, roles)  # Используйте функцию 'generate_random_role'
    history.append(rol)
    bot.send_message(message.chat.id, f"твоя роль {rol}")  # Используйте f-строку для форматирования текста

bot.polling(none_stop=True)
