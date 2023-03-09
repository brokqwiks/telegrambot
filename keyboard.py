from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('Random photo')

kb.add(b1,b2,b3)

kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text="Рандом")
bp2 = KeyboardButton(text="Главное меню")

kb_photo.add(bp1,bp2)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text="❤", callback_data="like")
ib2 = InlineKeyboardButton(text="👎", callback_data="dislike")
ib3 = InlineKeyboardButton(text="➡", callback_data="next_photo")
ib4 = InlineKeyboardButton(text="Главное меню", callback_data="menu")
ikb.add(ib1,ib2,ib3,ib4)