from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_shedule = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='๐ 1 ะบะพัะฟัั ๐'),
            KeyboardButton(text='๐ 2 ะบะพัะฟัั ๐'),
        ],
        [
            KeyboardButton(text='๐ 3 ะบะพัะฟัั ๐'),
            KeyboardButton(text='๐ 4 ะบะพัะฟัั ๐'),
        ],
        [
            KeyboardButton(text='๐ ะะฐะทะฐะด'),
        ]
    ],
    resize_keyboard=True
)