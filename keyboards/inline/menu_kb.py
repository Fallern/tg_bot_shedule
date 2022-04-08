from aiogram.utils.callback_data import CallbackData
from aiogram import types

kb_settings_notify = types.InlineKeyboardMarkup(row_width=1)
kb_settings_notify.add(
    types.InlineKeyboardButton(text="Ваши данные", callback_data="user_data"),
    types.InlineKeyboardButton(text="Выключить", callback_data="delete_user"),
)