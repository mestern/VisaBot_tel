import json
import time
from telebot import types
import telebot
import CusKey
from Config import *
import requests
from flask import redirect

global_id = None
ids = ["0"]

# ===============================================================================================

# some variable like telegram and TeleBot as bot
types = types
bot = telebot.TeleBot('7366730929:AAE071bwbTaEXsSOcKBi35bkETlhxzpjKQY')

# ================================================================================================

# check the status of user on telegram channel
def user_status(ChannelId, chat_id):
    member = bot.get_chat_member(ChannelId, chat_id)
    return member.status


# ================================================================================================

# check if user is joined on channel
def is_join(chat_id, bot):
    member = bot.get_chat_member(ChannelId, chat_id)
    if member.status in ['member', 'administrator', 'creator']:
        return True


# ================================================================================================

# it's work when user send start command and forced the usr to join to the channel
def start(message, chat_id, types):
    if is_join(chat_id=chat_id, bot=bot):
        if not is_registered(chat_id, "123321", "shater3"):
            bot.send_message(chat_id,
                             f"سلام {message.chat.first_name} \n به ربات visa ping "
                             "خوش اومدی \n\n اینجا میتونی فقط با چند تا کلیک ی فیلترشکن سریع"
                             " داشته باشی ! \n"
                             "فقط قبلش ریجستر کن !", reply_markup=CusKey.inl_register(types))
        else:
            bot.send_message(chat_id,
                             f"سلام {message.chat.first_name} \n به ربات visa ping "
                             "خوش اومدی \n\n اینجا میتونی فقط با چند تا کلیک ی فیلترشکن سریع"
                             " داشته باشی ! \n", reply_markup=CusKey.rep_main_menu(types))


    else:
        CusKey.inl_not_join(chat_id, types, bot)


# ================================================================================================

# check if user was registered
def is_registered(chat_id, admin_pass, admin_username):
    ss = api_load_tel_user_chat_id(chat_id, admin_pass, admin_username)
    print("sssssdddddd")
    if ss == "chat_id not exist":
        print(ss)
        return False
    else:
        print(ss, "else")
        return True


# ================================================================================================

# start registering the user
def register(chat_id):
    id = bot.send_message(chat_id, "کد دعوتت رو بفرست :")
    global_id = id.id + 1
    ids.append(global_id)
    if len(ids) > 1:
        del ids[0]


# ================================================================================================
# ********************************************************************************************
# api
# ********************************************************************************************
# ================================================================================================

# api to crate new account
def api_create_acc(message, username, password, day, admin_username):
    # Define the API endpoint URL
    url = "https://lib2023.site/vping/admin/load_admin_data.php"

    # Prepare the data to be sent (assuming POST request with form data)
    data = {
        "action": "add_new_bagher_user",
        "token_key": "YOUR_TOKEN_KEY",
        "admin_username": str(admin_username),
        "admin_password": "default",
        "supporter": "supporter",
        "description": "description",
        "days": str(day),
        "android_id2": "android_id2",
        "is_pc": "1",
        "username1": str(username),
        "password1": str(password),
        "app_version_code": "app_version_code",
    }

    # Send the POST request
    response = requests.post(url, data=data)
    print(response.text, response.status_code)
    # Check for response
    if response.text == "username exist already,sorry":
        bot.send_message(message.chat.id, "نام کاربری انتخواب شده تکراریه")
        return "username already taken"
    else:
        print(f"Error: {response.status_code}")
        return response.text


# ================================================================================================

# ================================================================================================

# api to add new telegram user to the databasfe
def api_new_tel_user(message, seller_id):
    # Define the API endpoint URL
    url = "https://lib2023.site/vping/admin/load_admin_data.php"

    # Prepare the data to be sent (assuming POST request with form data)
    data = {
        "action": "add_new_tel_user_bot",
        "token_key": "request_from_bot",
        "chat_id": message.chat.id,
        "tel_username": message.chat.username,
        "full_name": str(message.chat.first_name) + str(message.chat.last_name),
        "bio": message.chat.bio,
        "seller_id": str(seller_id)

    }

    # Send the POST request
    response = requests.post(url, data=data)
    # Check for response
    return response.text


# ================================================================================================

# ================================================================================================

# send the data of a user with chat id
def api_load_tel_user_chat_id(chat_id, admin_pass="123321", admin_username="shater3"):
    # Define the API endpoint URL
    url = "https://lib2023.site/vping/admin/load_admin_data.php"

    # Prepare the data to be sent (assuming POST request with form data)
    data = {
        "action": "load_tel_user_bot_with_chat_id",
        "token_key": "request_from_bot",
        "chat_id": chat_id,
        "username1": admin_username,
        "password1": admin_pass

    }

    # Send the POST request
    response = requests.post(url, data=data)
    return response.text

# ================================================================================================

# ================================================================================================


def api_payment(chat_id, amount):
    url = "https://lib2023.site/vping/admin/gateway.php"
    data = {
        "action": "start_request",
        "username1": "shater3",
        "amount": str(amount),
        "payment_type": "payment_type",
        "now1": str(time.strftime("%Y-%m-%d %H:%M:%S")),
        "last_id": "",
    }

    response = json.loads(requests.post(url, data=data).text)
    authority = response['data']['authority']

    data2 = {
        "action": "start_payment",
        "username1": "shater3",
        "amount": str(amount),
        "authority": authority
    }

    return requests.get(url, data2).url

