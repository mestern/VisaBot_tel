# ============================================================================================
# ********************************************************************************************
# custom keyboard button
# ********************************************************************************************
# ============================================================================================

<<<<<<< HEAD
# custom keyboard main menu
def main_menu(message, bot, types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    price = types.KeyboardButton(text="استعلام قیمت", callback_data="price")
    buy = types.KeyboardButton(text="خرید", callback_data="buy")
    rules = types.KeyboardButton(text="قوانین", callback_data="rules")
    support = types.KeyboardButton(text="پشتیبانی", callback_data="support")
    markup.add(price, buy, rules, support)
    bot.send_message(message.chat.id, "Select option:", reply_markup=markup)
=======



# custom keyboard main menu
def main_menu(types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    price = types.KeyboardButton(text="استعلام قیمت")
    buy = types.KeyboardButton(text="خرید")
    rules = types.KeyboardButton(text="قوانین")
    support = types.KeyboardButton(text="پشتیبانی")
    markup.add(price, buy, rules, support)
    return markup

>>>>>>> 0dbc9fc (all)

# =====================================================================================


# custom keyboard buy menu (after click on خرید key)
<<<<<<< HEAD
def buy_menu(message, bot, types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    m1u1 = types.KeyboardButton(text="یک ماه تک کاربر", callback_data="m1u1")
=======
def buy_menu(chat_id, bot, types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    m1u1 = types.KeyboardButton(text="یک ماه تک کاربر", callback_data="m1u1", )
>>>>>>> 0dbc9fc (all)
    m1u2 = types.KeyboardButton(text="یک ماه دو کاربر", callback_data="m1u2")
    m3u1 = types.KeyboardButton(text="سه ماه تک کاربر", callback_data="m3u1")
    m3u2 = types.KeyboardButton(text="سه ماه دو کاربر", callback_data="m3u2")
    d1u1 = types.KeyboardButton(text="تست یک روز تک کاربر", callback_data="d1u1")
    d1u2 = types.KeyboardButton(text="تست یک روز تک کاربر", callback_data="d1u2")
    d2u1 = types.KeyboardButton(text="پشتیبانی", callback_data="d2u1")
    d2u2 = types.KeyboardButton(text="پشتیبانی", callback_data="d2u2")
    markup.add(m1u1, m1u2, m3u1, m3u2, d2u2, d2u1, d1u1, d1u2)
<<<<<<< HEAD
    bot.send_message(message.chat.id, "Select option:", reply_markup=markup)
=======
    bot.send_message(chat_id, "Select option:", reply_markup=markup)
>>>>>>> 0dbc9fc (all)


# ============================================================================================
# ********************************************************************************************
# inline button
# ********************************************************************************************
# ============================================================================================

# inline button
<<<<<<< HEAD
def in_not_join(message, types, bot):
    markup = types.InlineKeyboardMarkup()
    join = types.InlineKeyboardButton("join", callback_data="join", url="https://t.me/Visa_Ping_vpn")
    check = types.InlineKeyboardButton("check", callback_data="check")
    markup.add(join, check)
    bot.send_message(chat_id=message.chat.id, text="اول جوین کانال شو !", reply_markup=markup)


=======
def inl_not_join(chat_id, types, bot):
    markup = types.InlineKeyboardMarkup()
    join = types.InlineKeyboardButton("join", callback_data="join", url="https://t.me/visapingadmin")
    check = types.InlineKeyboardButton("check", callback_data="check")
    markup.add(join, check)
    bot.send_message(chat_id=chat_id, text="اول جوین کانال شو !", reply_markup=markup)


def inl_acc_time(chat_id, types, bot):
    markup = types.InlineKeyboardMarkup()
    m1 = types.InlineKeyboardButton(text=".       یک ماه تک کاربر       .", callback_data="31")
    d2 = types.InlineKeyboardButton(text="تست دو روز", callback_data="2")
    m3 = types.InlineKeyboardButton(text="سه ماه تک کاربر", callback_data="91")
    d1 = types.InlineKeyboardButton(text="تست یک روز", callback_data="1")
    markup.add(m1, m3, d1, d2)
    return bot.send_message(chat_id=chat_id, text="یکی از اینارو انتخواب کن:", reply_markup=markup)
>>>>>>> 0dbc9fc (all)
# ============================================================================================

# check if user joined button


