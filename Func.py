from telebot import types
<<<<<<< HEAD
import telebot
from CusKey import *

# ===============================================================================================

# some variable like telegram channel id and TeleBot as bot
types = types
ChannelId = ''
bot = telebot.TeleBot()
=======
from Config import *
from CusKey import *
import telebot
import requests


# ===============================================================================================

# some variable like telegram and TeleBot as bot
types = types
bot = telebot.TeleBot('7366730929:AAE071bwbTaEXsSOcKBi35bkETlhxzpjKQY')
>>>>>>> 0dbc9fc (all)


# ================================================================================================

# check the status of user on telegram channel
def user_status(message):
    user_id = message.chat.id


# ================================================================================================

# check if user is joined on channel
<<<<<<< HEAD
def is_join(message, bot):
    member = bot.get_chat_member(ChannelId, message.chat.id)
=======
def is_join(chat_id, bot):
    member = bot.get_chat_member(ChannelId, chat_id)
>>>>>>> 0dbc9fc (all)
    if member.status in ['member', 'administrator', 'creator']:
        return True


# ================================================================================================

# return the user id
def chat_id(message):
    return message.chat.id


# ================================================================================================

# commands functions

<<<<<<< HEAD
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
=======
def start(message, chat_id):
    if is_join(chat_id=chat_id, bot=bot):
        bot.send_message(chat_id,
                         f"سلام {message.chat.first_name} \n به ربات visa ping "
                         f"خوش اومدی \n\n اینجا میتونی فقط با چند تا کلیک ی فیلترشکن سریع"
                         f" داشته باشی ! \n.", reply_markup=main_menu(types))

    else:
        inl_not_join(chat_id, types, bot)


# ================================================================================================


# ================================================================================================

# api to crate new account
def api_create(message, username, password, day, admin_pass, admin_username):
    # Define the API endpoint URL
    url = "https://lib2023.site/vping/admin/load_admin_data.php"

    # Prepare the data to be sent (assuming POST request with form data)
    data = {
        "action": "add_new_bagher_user",
        "token_key": "YOUR_TOKEN_KEY",
        "maker_username": "shater3",
        "maker_password": "123321",
        "supporter": "supporter",
        "description": "description",
        "days": "31",
        "android_id2": "android_id2",
        "is_pc": "1",
        "username1": "username1",
        "password1": "password1",
        "app_version_code": "app_version_code",
    }

    # Send the POST request
    response = requests.post(url, data=data)
    print(response.text, response.status_code)
    # Check for response
    if response.text == "username exist already,sorry":
        bot.send_message(message.chat.id, "نام کاربری انتخواب شده تکراریه")
        # Process the response data (if any)
        # response.text or response.json() depending on the API's response format
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # May contain error details

>>>>>>> 0dbc9fc (all)
