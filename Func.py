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
                         "خوش اومدی \n\n اینجا میتونی فقط با چند تا کلیک ی فیلترشکن سریع"
                         " داشته باشی ! \n", reply_markup=inviter_code(types))
        if not is_registered(chat_id, "123321", "shater3"):
            bot.send_message(chat_id, "کد دعوتت رو به این پیام ریپلای کن!")

    else:
        inl_not_join(chat_id, types, bot)


# ================================================================================================

def is_registered(chat_id, admin_pass, admin_username):
    if load_tel_user_bot_with_chat_id(chat_id, admin_pass, admin_username) == "username already taken":
        return True
    return False

# ================================================================================================
# ********************************************************************************************
# api
# ********************************************************************************************
# ================================================================================================

# api to crate new account
def api_create(message, username, password, day, admin_pass, admin_username):
    # Define the API endpoint URL
    url = "https://lib2023.site/vping/admin/load_admin_data.php"

    # Prepare the data to be sent (assuming POST request with form data)
    data = {
        "action": "add_new_bagher_user",
        "token_key": "YOUR_TOKEN_KEY",
        "admin_username": str(admin_username),
        "admin_password": str(admin_pass),
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

def add_new_tel_user_bot(chat_id, tel_username, full_name, bio, seller_id, message):
    # Define the API endpoint URL
    url = "https://lib2023.site/vping/admin/load_admin_data.php"

    # Prepare the data to be sent (assuming POST request with form data)
    data = {
        "action": "add_new_tel_user_bot",
        "token_key": "request_from_bot",
        "chat_id": str(chat_id),
        "tel_username": str(tel_username),
        "full_name": str(full_name),
        "bio": str(bio),
        "seller_id": str(seller_id)

    }

    # Send the POST request
    response = requests.post(url, data=data)
    print(response.text)
    # Check for response
    if response.text.__contains__("chat_id exist already,sorry"):
        bot.send_message(message.chat.id, "نام کاربری انتخواب شده تکراریه")
        print()
        # Process the response data (if any)
        # response.text or response.json() depending on the API's response format
    elif response.text.__contains__("Registered Successfully"):
        print("Registered Successfully")


# ================================================================================================

# ================================================================================================

def load_tel_user_bot_with_chat_id(chat_id, admin_pass="shater3", admin_username="123321"):
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

# ================================================================================================

# ================================================================================================



