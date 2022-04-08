from aiogram import types

from loader import dp
from keyboards.default.keyboard_shedule import kb_shedule
from keyboards.inline.menu_kb import kb_settings_notify


@dp.message_handler(text="📆 Расписание")
async def command_shedule_menu(message: types.Message):
    await message.answer("Вы открыли вкладку расписание", reply_markup=kb_shedule)


@dp.message_handler(text="📖 Расписание звонков")
async def command_get_shedule_time(message: types.Message):
    await message.answer("В ближайшие дни функция появится")


@dp.message_handler(text='📩 Настройки уведомлений')
async def command_settings_notify(message: types.Message):
    await message.answer("🛠 НАСТРОЙКИ УВЕДОМЛЕНИЙ", reply_markup=kb_settings_notify)
