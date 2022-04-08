from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📆 Расписание'),
            KeyboardButton(text='📖 Расписание звонков'),
        ],
        [KeyboardButton(text='📩 Настройки уведомлений')],
    ],
    resize_keyboard=True
)
