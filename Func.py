from telebot import types
import telebot
from Config import *
from CusKey import *
import requests

# ===============================================================================================

# some variable like telegram and TeleBot as bot
types = types
bot = telebot.TeleBot('7366730929:AAE071bwbTaEXsSOcKBi35bkETlhxzpjKQY')


# ================================================================================================

# check the status of user on telegram channel
def user_status(message):
    user_id = message.chat.id


# ================================================================================================

# check if user is joined on channel
def is_join(chat_id, bot):
    member = bot.get_chat_member(ChannelId, chat_id)
    if member.status in ['member', 'administrator', 'creator']:
        return True


# ================================================================================================

# return the user id
def chat_id(message):
    return message.chat.id


# ================================================================================================

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

