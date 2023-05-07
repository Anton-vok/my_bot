import telebot
bot=telebot.TeleBot("6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo")
history=[]
min_players=1
roles=[
    ["one",None,None,1],
    ["two",None,None,1]
]
history_user=[]
def assign_role(history, min_players, roles):
    roles_with_min_requirement = [role for role in roles if history.count(role[0]) < role[1]]

    if len(roles_with_min_requirement) > 0:
        return random.choice(roles_with_min_requirement)[0]

    remaining_slots = min_players - len(history)
    remaining_roles = []

    for role in roles:
        if role[2] is None or history.count(role[0]) < role[2]:
            remaining_roles.append(role)
        else:
            remaining_slots += role[1]

    role_chances = []

    for role in remaining_roles:
        role_count = remaining_slots * role[3] // sum(r[3] for r in remaining_roles)
        role_chances += [role[0]] * role_count

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
    bot.send_message(message.chat.id,"твоя роль ${rol}")
bot.polling(none_stop=True)
