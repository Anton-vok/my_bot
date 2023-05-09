import telebot
import random
import json
from collections import Counter

# Импортирование модулей и начальная настройка
bot = telebot.TeleBot("6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")

# Заглушка для данных
default_data = {
    'history': [],
    'min_players': 2,
    'roles': [
        ["one", 1, None, 20],
        ["two", 1, 3, 80]
    ],
    'history_user': [],
    'user_rol': {},
    'rol_user': {},
}

history = []
min_players = 2
roles = []
history_user = []
user_rol = {}
rol_user = {}

# Функция для сохранения данных в файл
def save_data_to_file():
    data = {
        'history': history,
        'min_players': min_players,
        'roles': roles,
        'history_user': history_user,
        'user_rol': user_rol,
        'rol_user': rol_user,
    }

    with open('bot_data.json', 'w') as file:
        json.dump(data, file)

# Функция для загрузки данных из файла
def load_data_from_file():
    global history, min_players, roles, history_user, user_rol, rol_user

    try:
        with open('bot_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = default_data  # Если файла нет, используем заглушку

    history = data['history']
    min_players = data['min_players']
    roles = data['roles']
    history_user = data['history_user']
    user_rol = data['user_rol']
    rol_user = data['rol_user']

load_data_from_file()


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
#гига парсер котрый будет легаси сто лет, пока проект не закроют нах##

def process_input_data(input_data):
    try:
        input_lines = input_data.split('\n')
        min_players = int(input_lines[1])
        roles = []
        
        for line in input_lines[2:]:
            if line.strip() != "":
                role_data = line.split(',')
                role = [role_data[0].strip()]
                for num in role_data[1:]:
                    try:
                        value = int(num) if 'Inf' not in num else float(num)
                    except ValueError:
                        value = float('Inf')
                    role.append(value)
                roles.append(role)

        return True, min_players, roles

    except Exception as e:
        print("Ошибка обработки данных:", e)
        return False, None, None


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

        save_data_to_file()

@bot.message_handler(commands=["rolAll"])
def rolAll(message):
    if message.chat.id==-975731544:
        text=""
        for obj in history:
            text=text+obj+", "
        bot.send_message(message.chat.id,text)
    else:
        bot.send_message(message.chat.id,"У мужлан нет прав")
@bot.message_handler(commands=["userAll"])
def userAll(message):
    if message.chat.id==-975731544:
        text=""
        for obj in history_user:
            text=text+obj+", "
        bot.send_message(message.chat.id,text)
    else:
        bot.send_message(message.chat.id,"У мужлан нет прав")
@bot.message_handler(commands=["rol"])
def rol(message):
    if message.chat.id==-975731544:
        try:
            user = message.text
            user = user.replace('/rol', '')
            user = user.replace(" ","")
            text = user_rol[user]
            bot.send_message(message.chat.id, text)
        except KeyError:
            bot.send_message(message.chat.id, "Такой роли нету")
    else:
        bot.send_message(message.chat.id,"У мужлан нет прав")
@bot.message_handler(commands=["user"])
def user(message):
    if message.chat.id==-975731544:
        try:
            rol = message.text
            rol = rol.replace('/user', '')
            rol = rol.replace(" ","")
            text = rol_user[rol]
            bot.send_message(message.chat.id, text)
        except KeyError:
            bot.send_message(message.chat.id, "Такого пользователя нету")
    else:
        bot.send_message(message.chat.id,"У мужлан нет прав")
@bot.message_handler(commands=["new_rol"])
def new_rol(message):
    global min_players, roles, history, history_user, rol_user, user_rol  # добавьте эту строку
    
    if message.chat.id == -975731544:
        success, x, y= process_input_data(input_data)

        if succes:
            min_players, roles = x, y
            history = []
            history_user = []
            rol_user = {}
            user_rol = {}
            bot.send_message(message.chat.id, "OK 400")
        else:
            bot.send_message(message.chat.id, "Нет")
    else:
        bot.send_message(message.chat.id, "У мужлан нет прав")


bot.polling(none_stop=True)
