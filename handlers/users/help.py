from aiogram import types
from loader import dp


@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
    await message.answer("Блин, пока не могу тебе помочь")
