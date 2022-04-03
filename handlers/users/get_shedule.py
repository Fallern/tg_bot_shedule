from aiogram import types
from loader import dp
import database


async def get_shedule_(message: types.Message, number_college: int):
    # path_file = f"media/college_building_img/download_zamena{number_college}.png"
    file_id = 'AgACAgIAAxkDAANlYkfjLCyQIp1-Usb-m6DxwaW4AtcAAjC3MRt0RUBKjnFi5ZWvO90BAAMCAAN3AAMjBA'
    # await message.delete()
    # file = types.InputFile(path_file)
    await message.answer_photo(photo=file_id, caption=f"Расписание {number_college} корпуса")


@dp.message_handler(commands=['get1'])
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 1)


@dp.message_handler(commands=['get2'])
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 2)


@dp.message_handler(commands=['get3'])
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 3)


@dp.message_handler(commands=['get4'])
async def get_shedule_1(message: types.Message):
    await get_shedule_(message, 4)


@dp.message_handler(regexp="^(\d(\w|\d)[А-Я])(.*)(\d{3})$")  # reg = 9ИС-281, 9АТП-281...
async def get_group(message: types.Message):
    path_file = f"media/group_img/{message.text}.jpg"
    file = types.InputFile(path_file)
    await message.answer_photo(photo=file)
