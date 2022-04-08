from aiogram.utils.callback_data import CallbackData
from aiogram import types

from database import models

cb = CallbackData("group", "name")


async def generate(college_building: int, count_group: int, page=0, limit=10):
    groups = await models.GroupsImg().filter(college_building=college_building).limit(limit).offset(page * limit)
    count_page = (count_group // limit) - 1 if count_group % limit == 0 else (count_group // limit)
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = []
    keyboard.add(
        types.InlineKeyboardButton(text="Не выбирать группу", callback_data=cb.new(name="quit"))
    )
    for group in groups:
        button = types.InlineKeyboardButton(
            text=group.name,
            callback_data=cb.new(name=group.name)
        )
        buttons.append(button)
    keyboard.add(*buttons)
    if page == 0:
        keyboard.add(
            types.InlineKeyboardButton(text="Вперед", callback_data="next"),
        )
    elif page == count_page:
        keyboard.add(
            types.InlineKeyboardButton(text="Назад", callback_data="prev"),
        )
    else:
        keyboard.add(
            types.InlineKeyboardButton(text="Назад", callback_data="prev"),
            types.InlineKeyboardButton(text="Вперед", callback_data="next"),
        )

    return keyboard

kb_select_college = types.InlineKeyboardMarkup(row_width=2)
kb_select_college.add(
    types.InlineKeyboardButton(text="1 корпус", callback_data="1"),
    types.InlineKeyboardButton(text="2 корпус", callback_data="2"),
    types.InlineKeyboardButton(text="3 корпус", callback_data="3"),
    types.InlineKeyboardButton(text="4 корпус", callback_data="4"),
)
