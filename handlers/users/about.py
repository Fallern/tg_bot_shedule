from aiogram import types
from loader import dp


@dp.message_handler(commands=['about'])
async def command_start(message: types.Message):
    await message.answer(
        "Данный бот был создан студентом колледжа он не имеет никакого отношения к администрации колледжа.\n\n"
        "Техподдержка: @Fallern\n\n"
        "Мы во Вконтакте: https://vk.com/public201219488")
