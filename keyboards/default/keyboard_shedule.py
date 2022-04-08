from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_shedule = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚 1 корпус 📚'),
            KeyboardButton(text='📚 2 корпус 📚'),
        ],
        [
            KeyboardButton(text='📚 3 корпус 📚'),
            KeyboardButton(text='📚 4 корпус 📚'),
        ],
        [
            KeyboardButton(text='🔙 Назад'),
        ]
    ],
    resize_keyboard=True
)