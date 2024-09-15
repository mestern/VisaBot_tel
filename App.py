import time

from CusKey import *
from Func import *
from Config import *
import Func

# ===============================================================================================
# commands handler
# ===============================================================================================


# Commands handles /start, /help, /status and ...
@bot.message_handler(commands=['start'])
def start_handler(message):
    start(message, message.chat.id, types)


# ===============================================================================================

# handle register
@bot.message_handler(commands=['register'])
def register_handler(message):
    register(message.chat.id)


# ===============================================================================================
# message handler
# ===============================================================================================

# register function to register a new member
@bot.message_handler(func=lambda message: message.message_id == ids[0])
def register_hand(message):
    if str(message.text).lower() in admins.keys():
        user = api_new_tel_user(message, str(message.text).lower())
        bot.send_message(message.chat.id, user)
        start(message, message.chat.id, types)

    else:
        bot.send_message(message.chat.id, "seller id not exist")

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
                                                   f"\n🔰تک کاربره {price["m1u1"]} هزارتومان"
                                                   f"\n🔰دو کاربره {price["m1u2"]} هزارتومان"
                                                   f"\n🗓 سه ماهه:\n🔰تک کاربره {price["m3u1"]} هزارتومان"
                                                   f"\n🔰دو کاربره {price["m3u2"]} هزارتومان\n. ")
    else:
        inl_not_join(message.chat.id, types, bot)


# ===============================================================================================
# inline button handler
# ===============================================================================================

# join button handler
@bot.callback_query_handler(func=lambda call: call.data == "check")
def not_join_hand(call):
    if is_join(bot=bot, chat_id=call.message.chat.id):
        start(call.message, call.message.chat.id, types)
    else:
        bot.answer_callback_query(call.id, "اول جوین شو دیگه!!")


# ===============================================================================================

@bot.callback_query_handler(func=lambda call: call.data == "register")
def inl_register_hand(call):
    if not is_registered(call.message.chat.id, "123321", "shater3"):
        register(call.message.chat.id)


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
                                  reply_markup=inl_acc_three_month(types),
                                  chat_id=call.message.chat.id,
                                  text="اکانت سه ماهه\n تعداد کاربر رو انتخاب کن:")
        case '1':
            bot.answer_callback_query(call.id, text="درحال انتقال...")
            bot.edit_message_text(message_id=call.message.id,
                                  chat_id=call.message.chat.id,
                                  text="شما قادر به دریافت اکانت تست نیستید")
            time.sleep(5.0)
            bot.edit_message_text(message_id=call.message.id,
                                  chat_id=call.message.chat.id,
                                  reply_markup=inl_acc_time(types),
                                  text="یکی رو انتخاب کن:")


# ===============================================================================================

# handle monthly inline button menu
@bot.callback_query_handler(func=lambda call: call.data in ["m1u1", 'm1u2'])
def inl_acc_monthly_hand(call):
    match call.data:
        case 'm1u1':
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_payment(types, "m1b", api_payment(call.message.chat.id,
                                                                                     int(price["m1u1"] + "000"))),
                                  chat_id=call.message.chat.id,
                                  text="اکانت یک ماه تک کاربر\n"
                                       f"قیمت : {price["m1u1"]} هزارتومان")

        case 'm1u2':
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_payment(types, "m1b", api_payment(call.message.chat.id,
                                                                                     int(price["m1u2"] + "000"))),
                                  chat_id=call.message.chat.id,
                                  text="اکانت یک ماه دو کاربر\n"
                                       f"قیمت : {price["m1u2"]} هزارتومان")


# ===============================================================================================
# handle three months inline button menu
@bot.callback_query_handler(func=lambda call: call.data in ["m3u1", 'm3u2'])
def inl_acc_three_month_hand(call):
    match call.data:

        case 'm3u1':
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_payment(types, "m3b", api_payment(call.message.chat.id,
                                                                                     int(price["m3u1"] + "000"))),
                                  chat_id=call.message.chat.id,
                                  text="اکانت یک ماه تک کاربر\n"
                                       f"قیمت : {price["m3u1"]} هزارتومان")

        case 'm3u2':
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_payment(types, "m3b", api_payment(call.message.chat.id,
                                                                                     int(price["m3u2"] + "000"))),
                                  chat_id=call.message.chat.id,
                                  text="اکانت یک ماه تک کاربر\n"
                                       f"قیمت : {price["m3u2"]} هزارتومان")


# ===============================================================================================
@bot.callback_query_handler(func=lambda call: call.data in ['tback', 'cancel', 'm1b', 'm3b', 'pay'])
def inl_acc_back_hand(call):
    match call.data:
        case 'tback':
            bot.answer_callback_query(call.id, text="درحال برگشت ...")
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_time(types),
                                  chat_id=call.message.chat.id,
                                  text="قدم اول\n مدت زمان اکانتت رو انتخاب کن:")
        case 'cancel':
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_time(types),
                                  chat_id=call.message.chat.id,
                                  text="یکی رو انتخاب کن")

        case 'm1b':
            bot.answer_callback_query(call.id, text="درحال برگشت ...")
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_monthly(types),
                                  chat_id=call.message.chat.id,
                                  text="اکانت یک ماهه\n تعداد کاربر رو انتخاب کن:")

        case 'm3b':
            bot.answer_callback_query(call.id, text="درحال برگشت ...")
            bot.edit_message_text(message_id=call.message.id,
                                  reply_markup=inl_acc_three_month(types),
                                  chat_id=call.message.chat.id,
                                  text="اکانت سه ماهه\n تعداد کاربر رو انتخاب کن:")



# ===============================================================================================



# ===============================================================================================


if __name__ == '__main__':
    print("polling ...")
    bot.infinity_polling()
