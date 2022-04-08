from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Regexp, Text

from keyboards.inline.register_kb import generate, cb, kb_select_college
from keyboards.default.keyboard_menu import kb_menu
from loader import dp
from states import RegisterState
from database import models


@dp.message_handler(commands=['register'])
async def input_name(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=message.from_user.full_name, callback_data="name"))
    kb_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_cancel.add("Отмена")
    await message.answer(
        text="Привет, здесь ты можешь подписаться на авто-обновления расписания.\n Для отмены действий, "
             "можешь нажать на кнопку снизу)", reply_markup=kb_cancel)
    await message.answer(text="Введите или выберите свое имя:",
                         reply_markup=keyboard)
    await RegisterState.name.set()


@dp.message_handler(Text(equals="отмена", ignore_case=True), state=RegisterState.all_states)
async def input_name(message: types.Message, state: FSMContext):
    await message.answer("Все действия отменены", reply_markup=kb_menu)
    await state.finish()


@dp.callback_query_handler(text="name", state=RegisterState.name)
async def input_college_building(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(name=call.from_user.full_name)

    await call.message.answer("Выберете корпус колледжа, в котором вы обучаетесь:",
                              reply_markup=kb_select_college)
    await RegisterState.college_number.set()
    await call.answer()


@dp.callback_query_handler(Regexp("\d"), state=RegisterState.college_number)
async def input_group(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(college_number=call.data)

    count_group = await models.GroupsImg().filter(college_building=int(call.data)).count()
    page = 0
    limit = 15

    keyboard = await generate(college_building=call.data, count_group=count_group, page=page, limit=limit)

    await call.message.answer("Для продолжения выберете название вашей группы:",
                              reply_markup=keyboard)
    await state.update_data(page_data=(call.data, count_group, page, limit))
    await RegisterState.group.set()
    await call.answer()


@dp.callback_query_handler(cb.filter(), state=RegisterState.group)
async def final_registration(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(group=callback_data["name"])
    state_data = await state.get_data()
    name = state_data["name"]
    college_number = state_data["college_number"]
    group = state_data["group"] if callback_data["name"] != "quit" else None

    user = models.UserTg(
        id=call.from_user.id,
        name=name,
        college_building=college_number,
        group_id=group
    )
    await models.UserTg().bulk_create(objects=[user], on_conflict=['id'],
                                      update_fields=['name', 'college_building', 'group_id'])
    await call.message.answer("Вы успешно подписались на рассылку расписания:\n\n"
                              f"Ваше имя: {name}\n"
                              f"Номер корпуса: {college_number} корпус\n"
                              f"Ваша группа: {group}",
                              reply_markup=kb_menu)
    await call.answer()
    await state.finish()


@dp.callback_query_handler(text=['next', 'prev'], state=RegisterState.group)
async def group_page_paginator(call: types.CallbackQuery, state: FSMContext):
    page_data = (await state.get_data())["page_data"]
    college_building = page_data[0]
    count_page = page_data[1]
    page = page_data[2]
    limit = page_data[3]
    if call.data == "next":
        keyboard = await generate(college_building, count_page, page + 1, limit)
        await state.update_data(page_data=(college_building, count_page, page + 1, limit))
    elif call.data == "prev":
        keyboard = await generate(college_building, count_page, page - 1, limit)
        await state.update_data(page_data=(college_building, count_page, page - 1, limit))
    await call.message.edit_reply_markup(keyboard)
    await call.answer()
