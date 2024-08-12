from Func import *
import Func


# Commands handles /start, /help, /status and ...
@bot.message_handler(commands=['start'])
def start_handler(message):
    Func.start(message)


@bot.callback_query_handler(func=lambda call.data: "joinede")
def not_join_hand(call):
    if True:
        print(call.data)


if __name__ == '__main__':
    bot.infinity_polling()
