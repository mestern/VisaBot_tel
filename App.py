from Func import *
<<<<<<< HEAD
import Func


# Commands handles /start, /help, /status and ...
@bot.message_handler(commands=['start'])
def start_handler(message):
    Func.start(message)
=======
from Config import *
import Func


@bot.message_handler()
def all(message):
    is_join(message.chat.id, bot)


# ===============================================================================================
# commands handler
# ===============================================================================================

# Commands handles /start, /help, /status and ...
@bot.message_handler(commands=['start'])
def start_handler(message):
    start(message, message.chat.id)


# ===============================================================================================
# replay keyboard handler
# ===============================================================================================

@bot.message_handler()
def rep_key_hand(message):
    match message.text:
        case "خرید":
            bot.reply_to(message, inl_acc_time(message.chat.id, types, bot))
>>>>>>> 0dbc9fc (all)


# ===============================================================================================
# inline button handler
# ===============================================================================================

# join button handler
<<<<<<< HEAD
@bot.callback_query_handler(func=lambda call: call.data in ["join", "check"])
@bot.message_handler(func=lambda message: True)
def not_join_hand(call, message):
    if call.data == "check":
        if Func.is_join(message, bot):
            start(message)
        else:
            bot.send_message(message.chat.id, "هنوز جوین نشدیا!")


if __name__ == '__main__':
=======
@bot.callback_query_handler(func=lambda call: call.data == "check")
def not_join_hand(call):
    if is_join(bot=bot, chat_id=call.message.chat.id):
        start(call.message, call.message.chat.id)
    else:
        bot.answer_callback_query(call.id, "اول جوین شو دیگه!!")


# ===============================================================================================


if __name__ == '__main__':
    print("polling ...")
>>>>>>> 0dbc9fc (all)
    bot.infinity_polling()
