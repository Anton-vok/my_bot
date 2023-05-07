from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from queue import Queue

import random

def parse_roles_text(text):
    lines = text.strip().split('\n')
    min_participants_line, *role_lines = lines

    min_participants = int(min_participants_line.split()[1])

    roles = []
    for role_line in role_lines:
        parts = role_line.split(', ')
        role_name = parts[0]
        min_role = int(parts[1].split()[1])
        max_role = None if parts[2].split()[1] == "null" else int(parts[2].split()[1])
        probability = int(parts[3].split()[2])

        roles.append([role_name, min_role, max_role, probability])

    return min_participants, roles

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

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет. Я создан для раздачи ролей в ролевой игре "The Adventurers Guild".')
    update.message.reply_text("https://t.me/GenRolACHV")
    update.message.reply_text("Если ты сейчас напишешь /new, бот отправит тебе твою роль.")
    update.message.reply_text("Если что-то не работает, сообщи мне: @A_CH_V")
    update.message.reply_text("(пожалуйста, не ломайте ничего, он и так сделан на коленке)")

def handle_message(update: Update, context: CallbackContext):
    global history, mini, rul
    chat_id = update.effective_chat.id
    if chat_id == -1001690902050:
        mini, rul = parse_roles_text(update.message.text)
        history = []

def get_registered_players(update: Update, context: CallbackContext):
    global history
    if update.effective_chat.id == -1001690902050:
        players = ', '.join(history)
        update.message.reply_text(f"Registered players: {players}")

def get_roles(update: Update, context: CallbackContext):
    global history
    if update.effective_chat.id == -1001690902050:
        unique_roles = list(set(history))
        roles_count = [history.count(role) for role in unique_roles]
        roles = ', '.join([f"{unique_roles[i]}: {roles_count[i]}" for i in range(len(unique_roles))])
        update.message.reply_text(f"Roles: {roles}")


def new(update: Update, context: CallbackContext):
    global history, mini, rul
    if update.effective_user.username in history:
        update.message.reply_text("Вы уже получили роль. Дождитесь обновления ролей.")
        return
    me = assign_role(history, mini, rul)
    history.append(update.effective_user.username)
    update.message.reply_text(me)

def main():
    updater = Updater("6024635066:AAFGjWIB62DdBx355aCCduZJdTKvBphnsBo", update_queue=Queue())

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.text & ~Filters.command, handle_message))
    dispatcher.add_handler(CommandHandler("new", new))
    dispatcher.add_handler(CommandHandler("get", get_registered_players))
    dispatcher.add_handler(CommandHandler("rol", get_roles))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    history = []
    mini = 0
    rul = []

    main()

