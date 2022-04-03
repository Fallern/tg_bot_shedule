from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='2'),
            KeyboardButton(text="3"),
        ]
    ],
    resize_keyboard=True
)
