from aiogram import types
from loader import dp, redis_client


async def get_shedule_(message: types.Message, number_college: int):
    id_file = redis_client.hget("id_colleges_img", f"college_{number_college}")
    print(id_file)
    if id_file is None:
        path_file = f"media/college_building_img/download_zamena{number_college}.png"
        file = types.InputFile(path_file)
        id_photo = await message.answer_photo(photo=file, caption=f"Расписание {number_college} корпуса")
        redis_client.hset("id_colleges_img", f"college_{number_college}", id_photo.photo[-1].file_id)
    else:
        await message.answer_photo(photo=id_file, caption=f"Расписание {number_college} корпуса")


@dp.message_handler(commands=['get_1'])
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 1)


@dp.message_handler(commands=['get_2'])
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 2)


@dp.message_handler(commands=['get_3'])
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 3)


@dp.message_handler(commands=['get_4'])
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 4)


@dp.message_handler(regexp="^(\d(\w|\d)[А-Я])(.*)(\d{3})$")  # reg = 9ИС-281, 9АТП-281...
async def get_group(message: types.Message):
    path_file = f"media/group_img/{message.text}.jpg"
    file = types.InputFile(path_file)
    await message.answer_photo(photo=file)
