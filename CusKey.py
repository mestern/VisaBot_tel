from Func import *


# ============================================================================================
# ********************************************************************************************
# custom keyboard button
# ********************************************************************************************
# ============================================================================================

# custom keyboard main menu
def main_menu(types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    price = types.KeyboardButton(text="💸|استعلام قیمت")
    buy = types.KeyboardButton(text="💳|خرید")
    rules = types.KeyboardButton(text="⚖|قوانین")
    support = types.KeyboardButton(text="👨‍💻|پشتیبانی")
    home = types.KeyboardButton(text="🏠|خانه")
    markup.add(price, buy, rules, support, home)
    return markup


def inviter_code(types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    invite = types.KeyboardButton(text="/register")
    markup.add(invite)
    return markup


# ============================================================================================
# ********************************************************************************************
# inline button
# ********************************************************************************************
# ============================================================================================

# It is displayed when the user has not joined the channel
def inl_not_join(chat_id, types, bot):
    markup = types.InlineKeyboardMarkup()
    join = types.InlineKeyboardButton("join", callback_data="join", url="https://t.me/visapingadmin")
    check = types.InlineKeyboardButton("check", callback_data="check")
    markup.add(join, check)
    bot.send_message(chat_id=chat_id, text="اول جوین کانال شو !", reply_markup=markup)


# ============================================================================================

# show all available accounts time
def inl_acc_time(types):
    markup = types.InlineKeyboardMarkup()
    m1 = types.InlineKeyboardButton(text="یک ماه", callback_data="31")
    m3 = types.InlineKeyboardButton(text="سه ماه", callback_data="91")
    d1 = types.InlineKeyboardButton(text="تست", callback_data="1")
    cn = types.InlineKeyboardButton(text="❌انصراف", callback_data="cancel")
    markup.add(m1)
    markup.add(m3)
    markup.add(d1)
    markup.add(cn)
    return markup


# ============================================================================================

# handle monthly accou
def inl_acc_monthly(types):
    markup = types.InlineKeyboardMarkup()
    u1 = types.InlineKeyboardButton(text="تک کاربر", callback_data="m1u1")
    u2 = types.InlineKeyboardButton(text="دو کاربر", callback_data="m1u2")
    bk = types.InlineKeyboardButton(text="↩قبلی", callback_data="tback")
    cn = types.InlineKeyboardButton(text="❌انصراف", callback_data="cancel")
    markup.add(u1)
    markup.add(u2)
    markup.add(bk, cn)
    return markup


# ============================================================================================
def inl_acc_tree_moths(types):
    markup = types.InlineKeyboardMarkup()
    u1 = types.InlineKeyboardButton(text="تک کاربر", callback_data="m3u1")
    u2 = types.InlineKeyboardButton(text="دو کاربر", callback_data="m3u2")
    bk = types.InlineKeyboardButton(text="↩قبلی", callback_data="tback")
    cn = types.InlineKeyboardButton(text="❌انصراف", callback_data="cancel")
    markup.add(u1)
    markup.add(u2)
    markup.add(bk, cn)
    return markup


# ============================================================================================
def inl_acc_test(types):
    markup = types.InlineKeyboardMarkup()
    d1 = types.InlineKeyboardButton(text="تست یک روز", callback_data="d1u1")
    d2 = types.InlineKeyboardButton(text="تست دو کاربر", callback_data="d1u2")
    bk = types.InlineKeyboardButton(text="↩قبلی", callback_data="back")
    cn = types.InlineKeyboardButton(text="❌انصراف", callback_data="cancel")
    markup.add(d1)
    markup.add(d2)
    markup.add(bk, cn)
    return markup


# ============================================================================================

