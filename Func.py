from telebot import types
import telebot
from CusKey import *

# ===============================================================================================

# some variable like telegram channel id and TeleBot as bot
types = types
ChannelId = '-1002160415180'
bot = telebot.TeleBot('7366730929:AAE071bwbTaEXsSOcKBi35bkETlhxzpjKQY')


# ================================================================================================

# check the status of user on telegram channel
def user_status(message):
    user_id = message.chat.id


# ================================================================================================

# check if user is joined on channel
def is_join(message, bot):
    member = bot.get_chat_member(ChannelId, message.chat.id)
    if member.status in ['member', 'administrator', 'creator']:
        return True


# ================================================================================================

# return the user id
def chat_id(message):
    return message.chat.id


# ================================================================================================

# commands functions

def start(message):
    if is_join(message, bot):
        bot.send_message(message.chat.id, f"سلام {message.chat.first_name} \n به ربات visa ping خوش اومدی \n\n اینجا میتونی فقط با چند تا کلیک ی فیلترشکن سریع داشته باشی ! \n.")
    else:
        in_not_join(message, types, bot)




# ================================================================================================
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if message.chat.id == ChannelId:
#         print(help(message))
#         print(message.chat.id, message.chat.username)
#         print(f"Received message from target chat: {message}")
#     else:
#         print(message.chat.id, message.message_id)
#         print("no")
#         bot.send_message(message.chat.id, "ah")
#         # Optionally, handle messages from other chats (e.g., ignore them)