import telebot
bot=telebot.TeleBot("6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")
import random

history = []
min_players = 1
roles = [
    ["one", None, None, 1],
    ["two", None, None, 1]
]
history_user = []

def assign_role(history, min_players, roles):
    # Список ролей, которые еще не набраны минимальное количество раз.
    roles_with_min_requirement = [role for role in roles if role[1] is not None and history.count(role[0]) < role[1]]

    if len(roles_with_min_requirement) > 0:
        # Если есть доступные роли, которые нужно набрать минимальное количество раз, 
        # выбираем случайную роль из этого списка и возвращаем ее имя.
        return random.choice(roles_with_min_requirement)[0]

    # Если ни одна из ролей не требует дополнительных игроков, то пробуем назначить роли по умолчанию.
    remaining_slots = max(min_players - len(history), 0) # Оставшееся количество игроков, которые нужно распределить.

    # Список ролей, которые еще не набраны максимальное количество раз.
    remaining_roles = [role for role in roles if role[2] is None or history.count(role[0]) < role[2]]

    # Список ролей, из которых будут выбираться роли для назначения.
    role_chances = []

    # Если осталось меньше ролей, чем игроков, то мы назначаем все доступные роли и возвращаем их.
    if remaining_slots <= len(remaining_roles):
        for role in remaining_roles[:remaining_slots]:
            history.append(role[0])
        return history

    # Если осталось больше ролей, чем игроков, то мы выбираем роли с вероятностями,
    # пропорциональными их "весам" (третий параметр в списке roles).
    for role in remaining_roles:
        role_count = remaining_slots * role[3] // sum(r[3] for r in remaining_roles)
        role_chances += [role[0]] * role_count

    # Выбираем случайную роль из списка возможных ролей и возвращаем ее имя.
    return random.choice(role_chances)





@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет. Я создан для раздачи ролей в ролевой "The Adventurers Guild".')
    bot.send_message(message.chat.id,"https://t.me/GenRolACHV")
    bot.send_message(message.chat.id,"Если ты сейчас напишешь /new, бот отправит тебе твою роль.\nЕсли что-то не работает, сообщи мне: @A_CH_V\nпожалуйста, не ломайте ничего, он и так сделан на коленке)")
@bot.message_handler(commands=['new'])
def new(message):
    rol=assign_role(history, min_players, roles)
    history.append(rol)
    bot.send_message(message.chat.id,f"твоя роль-{rol}")
bot.polling(none_stop=True)
