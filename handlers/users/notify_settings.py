from aiogram import types

from loader import dp
from database import models


@dp.callback_query_handler(text="user_data")
async def show_user_data(call: types.CallbackQuery):
    id_user = call.from_user.id
    user = await models.UserTg.get_or_none(id=id_user)
    if user is None:
        await call.message.answer(f"Вы не подписанны на рассылку")
    else:
        await call.message.answer(f"Ваше имя: {user.name}\n"
                                  f"Номер корпуса: {user.college_building}\n"
                                  f"Название группы: {await user.group}")
    await call.answer()


@dp.callback_query_handler(text="delete_user")
async def delete_user_data(call: types.CallbackQuery):
    id_user = call.from_user.id
    user = await models.UserTg.get_or_none(id=id_user)
    if user is None:
        await call.message.answer(f"Вы не подписанны на рассылку")
    else:
        await user.delete()
        await call.message.answer(f"Вы отписались от рассылки")
    await call.answer()
