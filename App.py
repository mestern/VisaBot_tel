from _ctypes_test import func

from Func import *
from Config import *
import Func


user_data = {}

@bot.message_handler(commands=['register'])
def start_registration(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    bot.send_message(chat_id, "Please enter your first name:")
    hand_reg(message)
def hand_reg(message):
    @bot.message_handler()
    def handle_registration(message):
        chat_id = message.chat.id
        if chat_id in user_data:
            if 'name' not in user_data[chat_id]:
                user_data[chat_id]['name'] = message.text
                bot.send_message(chat_id, "Please enter your last name:")
            elif 'last_name' not in user_data[chat_id]:
                user_data[chat_id]['last_name'] = message.text
                bot.send_message(chat_id, "Please enter your age:")
            elif 'age' not in user_data[chat_id]:
                try:
                    age = int(message.text)
                    user_data[chat_id]['age'] = age
                    bot.send_message(chat_id, f"Registration successful! Your name is {user_data[chat_id]['name']} {user_data[chat_id]['last_name']} and your age is {age}.")
                    del user_data[chat_id]
                except ValueError:
                    bot.send_message(chat_id, "Invalid age. Please enter a valid number.")


# ===============================================================================================
# commands handler
# ===============================================================================================

# Commands handles /start, /help, /status and ...
@bot.message_handler(commands=['start'])
def start_handler(message):
    start(message, message.chat.id)


# ===============================================================================================

# handle register
@bot.message_handler(commands=['redsdsgister'])
def register_handler(message):
    print(message.text)
    @bot.message_handler(func=lambda message: True)
    def registering(message):
        print("reg2")
        if message.text in sellers:
            resp = add_new_tel_user_bot(message, message.text)
            bot.send_message(message.chat.id, resp)

        else:
            bot.send_message(message.chat.id, "seller id not exist")


# ===============================================================================================
# message handler
# ===============================================================================================

# register function to register a new member

# ===============================================================================================
# replay keyboard handler
# ===============================================================================================

# handle reply keyboard markup
@bot.message_handler()
def rep_key_hand(message):
    if is_join(message.chat.id, bot):
        match message.text:
            case "💳|خرید":
                bot.send_message(message.chat.id, "یکی رو انتخاب کن:",
                                 reply_to_message_id=message.id,
                                 reply_markup=inl_acc_time(types))
            case "⚖|قوانین":
                bot.send_message(message.chat.id, "توجه، استفاده از سرویس کاهش پینگ ویزا (Visa Ping)"
                                                  " برای انجام مقاصد مجرمانه به هر نحوی جرم بوده و درصورت "
                                                  "مشاهده حساب کاربری شما مسدود خواهد شد.",
                                 reply_to_message_id=message.id)
            case "👨‍💻|پشتیبانی":
                bot.export_chat_invite_link(message.chat.id, "@ping_support1")
            case "💸|استعلام قیمت":
                bot.reply_to(message=message, text="✅لیست قیمت\n🗓 یک‌ ماهه:"
                                                   f"\n🔰تک کاربره ۱۱۰ هزارتومان"
                                                   f"\n🔰دو کاربره ۱۶۰ هزارتومان"
                                                   f"\n🗓 سه ماهه:\n🔰تک کاربره ۲۴۰ هزارتومان"
                                                   f"\n🔰دو کاربره ۳۸۰ هزارتومان\n. ")
    else:
        inl_not_join(message.chat.id, types, bot)

# ===============================================================================================
# inline button handler
# ===============================================================================================

# join button handler
@bot.callback_query_handler(func=lambda call: call.data == "check")
def not_join_hand(call):
    if is_join(bot=bot, chat_id=call.message.chat.id):
        start(call.message, call.message.chat.id)
    else:
        bot.answer_callback_query(call.id, "اول جوین شو دیگه!!")


# ===============================================================================================

# handle acc exists time handle
@bot.callback_query_handler(func=lambda call: call.data in ['31', '91', '1'])
def inl_acc_time_hand(call):
    match call.data:

        case '31':
            bot.answer_callback_query(call.id, text="درحال انتقال...")
            bot.edit_message_text(message_id=call.message.id,
                                  chat_id=call.message.chat.id,
                                  reply_markup=inl_acc_monthly(types),
                                  text="اکانت یک ماهه\n تعداد کاربر رو انتخاب کن:")
        case '91':
            bot.answer_callback_query(call.id, text="درحال انتقال...")
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_tree_moths(types),
                                  chat_id=call.message.chat.id,
                                  text="اکانت سه ماهه\n تعداد کاربر رو انتخاب کن:")
        case '1':
            bot.answer_callback_query(call.id, text="درحال انتقال...")
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_monthly(types),
                                  chat_id=call.message.chat.id,
                                  text="شما قادر به دریافت اکانت تست نیستید")


# handle monthly inline button menu
@bot.callback_query_handler(func=lambda call: call.data in ["m1u1", 'm1u2'])
def inl_acc_monthly_hand(call):
    match call.data:
        case 'm1u1':
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_monthly(types),
                                  chat_id=call.message.chat.id)
        case 'm1u2':
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_monthly(types),
                                  chat_id=call.message.chat.id)


# ===============================================================================================
# handle three months inline button menu
@bot.callback_query_handler(func=lambda call: call.data in ["m3u1", 'm3u2'])
def inl_acc_three_month_hand(call):
    match call.data:
        case 'm3u1':
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_monthly(types),
                                  chat_id=call.message.chat.id)
        case 'm3u2':
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_monthly(types),
                                  chat_id=call.message.chat.id)


# ===============================================================================================
@bot.callback_query_handler(func=lambda call: call.data in ['tback', 'cancel'])
def inl_acc_monthly_hand(call):
    match call.data:
        case 'tback':
            bot.answer_callback_query(call.id, text="درحال برگشت ...")
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_time(types),
                                  chat_id=call.message.chat.id,
                                  text="قدم اول\n مدت زمان اکانتت رو انتخاب کن:")
        case 'cancel':
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_monthly(types),
                                  chat_id=call.message.chat.id)


# ===============================================================================================


if __name__ == '__main__':
    print("polling ...")
    bot.infinity_polling()
