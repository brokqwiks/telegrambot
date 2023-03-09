from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import random
from aiogram.types import ReplyKeyboardRemove

from config import bot_token
from keyboard import kb, kb_photo,ikb
import attributes

bot = Bot(bot_token)
dp = Dispatcher(bot)

arr_photo = [
"https://chudo-prirody.com/uploads/posts/2021-08/1628637595_122-p-kotyata-milie-foto-132.jpg",
"https://natalyland.ru/wp-content/uploads/e/6/b/e6bc07798fadfaf768b2ec1b6f5585c2.jpeg",
"https://hdfon.ru/wp-content/uploads/hdfon.ru-217081719.jpg"
]

photo_description= dict(zip(arr_photo, ['Грустный котик','Веселый котик','Персик 2.0']))
random_photo = random.choice(list(photo_description.keys()))
flag = False

def on_startup():
    print('Bot is enabled')

async def send_random(message: types.Message):
    global random_photo
    random_photo = random.choice(list(photo_description))
    await bot.send_photo(chat_id=message.chat.id, photo=
                        random_photo,
                        caption=photo_description[random_photo],
                        reply_markup=ikb)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет",
                           reply_markup=kb)
    print(message.from_user.id)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, attributes.bot_help)

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(message.from_user.id, attributes.bot_description)

@dp.message_handler(Text(equals="Random photo"))
async def open_kb_photo(message: types.Message):
    await message.answer(text="Рандомная фотка",
                         reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()

@dp.message_handler(Text(equals="Главное меню"))
async def open_kb_photo(message: types.Message):
    await message.answer(text="Открыто главное меню",
                         reply_markup=kb)
    await message.delete()

@dp.callback_query_handler()
async def check_callback_data(callback: types.CallbackQuery):
    global random_photo
    global flag
    if callback.data == "like":
        if not flag :
            await callback.answer("Вам понравилась фотка")
            flag = not flag
        else:
            await callback.answer("Вы уже лайкнули эту фотку")

    elif callback.data == "dislike":
        await callback.answer('Вам не понравилась фотка')
    elif callback.data == "menu":
        await callback.message.answer(text="Открыто главное меню",
                                      reply_markup=kb)
        await callback.message.delete()
        await callback.answer()

    elif callback.data == "next_photo":
        random_photo = random.choice(list(filter(lambda x: x != random_photo,list(photo_description.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                          type = 'photo',
                                          caption = photo_description[random_photo]),
                                         reply_markup=ikb)
        await callback.answer()

if __name__ == '__main__':
    executor.start_polling(dp,on_startup=
                           on_startup(), skip_updates=True)