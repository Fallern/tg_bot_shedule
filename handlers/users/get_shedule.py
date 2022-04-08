from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, redis_client
from keyboards.default.keyboard_menu import kb_menu


async def get_shedule_(message: types.Message, number_college: int):
    id_file = redis_client.hget("id_colleges_img", f"college_{number_college}")
    if id_file is None:
        path_file = f"media/college_building_img/download_zamena{number_college}.png"
        file = types.InputFile(path_file)
        id_photo = await message.answer_photo(photo=file, caption=f"Расписание {number_college} корпуса")
        redis_client.hset("id_colleges_img", f"college_{number_college}", id_photo.photo[-1].file_id)
    else:
        await message.answer_photo(photo=id_file, caption=f"Расписание {number_college} корпуса")


@dp.message_handler(Text(equals=['📚 1 корпус 📚', '/get_1']))
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 1)


@dp.message_handler(Text(equals=['📚 2 корпус 📚', '/get_2']))
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 2)


@dp.message_handler(Text(equals=['📚 3 корпус 📚', '/get_3']))
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 3)


@dp.message_handler(Text(equals=['📚 4 корпус 📚', '/get_4']))
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 4)


@dp.message_handler(regexp="^(\d(\w|\d)[А-Я])(.*)(\d{3})$")  # reg = 9ИС-281, 9АТП-281...
async def get_group(message: types.Message):
    path_file = f"media/group_img/{message.text}.jpg"
    file = types.InputFile(path_file)
    await message.answer_photo(photo=file)


@dp.message_handler(text='🔙 Назад')
async def get_group(message: types.Message):
    await message.answer('Вы вернулись в главное меню', reply_markup=kb_menu)
