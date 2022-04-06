from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData

from loader import dp
from states import RegisterState
from database import models

cb = CallbackData("group", "name")


@dp.message_handler(commands=['register'])
async def register(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=message.from_user.full_name, callback_data="name"))
    await message.answer(text="Привет, здесь ты можешь подписаться на авто-обновления расписания.\n\nВведите свое имя:",
                         reply_markup=keyboard)
    await RegisterState.name.set()


@dp.callback_query_handler(text="name", state=RegisterState.name)
async def state1(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(name=call.from_user.full_name)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text="1 корпус", callback_data="1"),
        types.InlineKeyboardButton(text="2 корпус", callback_data="2"),
        types.InlineKeyboardButton(text="3 корпус", callback_data="3"),
        types.InlineKeyboardButton(text="4 корпус", callback_data="4"),
    )

    await call.message.answer("Выберете ваш корпус:",
                              reply_markup=keyboard)
    await RegisterState.college_number.set()


@dp.callback_query_handler(state=RegisterState.college_number)
async def state1(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(college_number=call.data)

    def chunk_using_generators(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    groups = list(await models.GroupsImg().filter(college_building=int(call.data)))

    groups = [group for group in chunk_using_generators(groups, 10)]

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    for group in groups[0]:
        button = types.InlineKeyboardButton(
            text=group.name,
            callback_data=cb.new(name=group.name)
        )
        buttons.append(button)
    keyboard.add(*buttons)
    keyboard.add(
        types.InlineKeyboardButton(text="Вперед", callback_data="2"),
    )

    await call.message.answer("Для продолжения выберете название вашей группы:",
                              reply_markup=keyboard)

    await RegisterState.group.set()


@dp.callback_query_handler(cb.filter(), state=RegisterState.group)
async def state1(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await state.update_data(group=callback_data["name"])
    state_data = await state.get_data()
    name = state_data["name"]
    college_number = state_data["college_number"]
    group = state_data["group"]

    user = models.UserTg(
        id=call.from_user.id,
        name=name,
        college_building=college_number,
        group_id=group
    )

    await models.UserTg().bulk_create(objects=[user], on_conflict=['id'],
                                      update_fields=['name', 'college_building', 'group_id'])
    await call.message.answer("Вы добавлены в БД")

    await state.finish()
