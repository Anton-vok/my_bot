#Импортирование модулей и начальная настройка
import telebot
bot=telebot.TeleBot("6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")
import random
from collections import Counter

#Базовый набор ролей(заглушка)
history = []
min_players = 2
roles = [
    ["one", 1, None, 20],
    ["two", 1, 3, 80]
]
history_user = []
user_rol={}
rol_user={}

#Функция выбора ролей
#min_calls-гарантирование минемальное количество участников
#role_history рошлые выпавшие рольи
#role_rules правила ролей в формате название_роли,мин_количество_выпадений,макс_количество_выпадений(None-бесконечность),вераятность_выпадения_в_процентах(в итоге все роли 100%)
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
    user_name="@"+message.from_user.username
    if (user_name in history_user):
        bot.send_message(message.chat.id,f"Ты уже получил роль. Твоя роль {user_rol[user_name]}")
    else:
        history_user.append(user_name)
        rol = generate_random_role(min_players, history, roles)
        history.append(rol)
        user_rol.update({user_name:rol})
        rol_user.update({rol:user_name})
        bot.send_message(message.chat.id, f"твоя роль {rol}")

@bot.message_handler(commands=["rolAll"])
def rolAll(message):
    text=""
    for obj in history:
        text=text+obj+", "
    bot.send_message(message.chat.id,text)
@bot.message_handler(commands=["userAll"])
def userAll(message):
    text=""
    for obj in history_user:
        text=text+obj+", "
    bot.send_message(message.chat.id,text)
@bot.message_handler(commands=["rol"])
def rol(message):
    try:
        user = message.text
        user = user.replace('/rol', '')
        user = user.replace(" ","")
        text = user_rol[user]
        bot.send_message(message.chat.id, text)
    except KeyError:
        bot.send_message(message.chat.id, "Такой роли нету")

@bot.message_handler(commands=["user"])
def user(message):
    try:
        rol = message.text
        rol = rol.replace('/user', '')
        rol = rol.replace(" ","")
        text = rol_user[rol]
        bot.send_message(message.chat.id, text)
    except KeyError:
        bot.send_message(message.chat.id, "Такого пользователя нету")
bot.polling(none_stop=True)
