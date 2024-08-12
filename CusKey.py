# ============================================================================================
# ********************************************************************************************
# custom keyboard button
# ********************************************************************************************
# ============================================================================================

# custom keyboard main menu
def main_menu(message, bot, types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    price = types.KeyboardButton(text="استعلام قیمت", callback_data="price")
    buy = types.KeyboardButton(text="خرید", callback_data="buy")
    rules = types.KeyboardButton(text="قوانین", callback_data="rules")
    support = types.KeyboardButton(text="پشتیبانی", callback_data="support")
    markup.add(price, buy, rules, support)
    bot.send_message(message.chat.id, "Select option:", reply_markup=markup)

# =====================================================================================


# custom keyboard buy menu (after click on خرید key)
def buy_menu(message, bot, types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    m1u1 = types.KeyboardButton(text="یک ماه تک کاربر", callback_data="m1u1")
    m1u2 = types.KeyboardButton(text="یک ماه دو کاربر", callback_data="m1u2")
    m3u1 = types.KeyboardButton(text="سه ماه تک کاربر", callback_data="m3u1")
    m3u2 = types.KeyboardButton(text="سه ماه دو کاربر", callback_data="m3u2")
    d1u1 = types.KeyboardButton(text="تست یک روز تک کاربر", callback_data="d1u1")
    d1u2 = types.KeyboardButton(text="تست یک روز تک کاربر", callback_data="d1u2")
    d2u1 = types.KeyboardButton(text="پشتیبانی", callback_data="d2u1")
    d2u2 = types.KeyboardButton(text="پشتیبانی", callback_data="d2u2")
    markup.add(m1u1, m1u2, m3u1, m3u2, d2u2, d2u1, d1u1, d1u2)
    bot.send_message(message.chat.id, "Select option:", reply_markup=markup)


# ============================================================================================
# ********************************************************************************************
# inline button
# ********************************************************************************************
# ============================================================================================

# inline button
def in_not_join(message, types, bot):
    markup = types.InlineKeyboardMarkup()
    join = types.InlineKeyboardButton("join", callback_data="join", url="https://t.me/Visa_Ping_vpn")
    check = types.InlineKeyboardButton("check", callback_data="check")
    markup.add(join, check)
    bot.send_message(chat_id=message.chat.id, text="اول جوین کانال شو !", reply_markup=markup)


# ============================================================================================

# check if user joined button


