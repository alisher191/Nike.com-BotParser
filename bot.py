from time import sleep

from aiogram import Bot, Dispatcher, executor, types

import config, prs, clothes_prs

TOKEN = config.API_TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    button = [
            [
                types.KeyboardButton('/shoes'),
                types.KeyboardButton('/clothes'),
            ]
        ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=button,
        resize_keyboard=True
    )
    await message.reply('Choose your thing:', reply_markup=keyboard)


@dp.message_handler(commands=['shoes'])
async def shoes(message: types.Message):
    for i in prs.shoes:
        # sleep(3)
        await message.reply(i)


@dp.message_handler(commands=['clothes'])
async def clothes(message: types.Message):
    for i in clothes_prs.clothes:
        # sleep(3)
        await message.reply(i)


if __name__ == "__main__":
    executor.start_polling(dp)
