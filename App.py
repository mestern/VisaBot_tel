from Func import *
import Func


# Commands handles /start, /help, /status and ...
@bot.message_handler(commands=['start'])
def start_handler(message):
    Func.start(message)


# ===============================================================================================
# inline button handler
# ===============================================================================================

# join button handler
@bot.callback_query_handler(func=lambda call: call.data in ["join", "check"])
@bot.message_handler(func=lambda message: True)
def not_join_hand(call, message):
    if call.data == "check":
        if Func.is_join(message, bot):
            start(message)
        else:
            bot.send_message(message.chat.id, "هنوز جوین نشدیا!")


if __name__ == '__main__':
    bot.infinity_polling()
