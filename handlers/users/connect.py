from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import kb_menu


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    sticker = 'CAACAgIAAxkBAAEEVBdiRY_oY-7Vds-Fr1TzW8TIv1x2xwACFgADrscyCt5fUMuqSVWmIwQ'
    await message.answer_sticker(sticker=sticker)
    await message.answer(
        f"Привет, <b>{message.chat.full_name}</b>, Я - очень простой бот, которой поможет тебе очень просто получать"
        f" расписание занятий по корпусам.\n\n"
        f"Выбери команду для продолжения или напиши /help")
