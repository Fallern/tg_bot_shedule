from aiogram import types
from loader import dp


@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
    await message.answer("1️⃣ /start - запустить/перезапустить бота\n\n"
                         "2️⃣ /get_1, /get_2, /get_3, /get_4 с помощью этих команд, ты сможешь получить расписание "
                         "занятий выбранного тобой корпуса, цифра означает номер корпуса\n\n"
                         "3️⃣ Набрав название своей группы, ты сможешь получить расписание именно этой группы, "
                         "а не всего колледжа, пример -> 9ИС-281, 9АТП-281 и так далее\n\n"
                         "4️⃣ Есть возможность подписаться на рассылку расписания каждый день, для этого тебе надо "
                         "набрать команду /register и пройти короткую процедуру заполнения данных, в итоге каждый день "
                         "будешь получать расписание. Важный момент -> ты можешь не выбирать название своей группы, "
                         "тогда ты будешь получать расписание на весь твой корпус.\n\n"
                         "5️⃣ /about здесь ты сможешь узнать информацию о создателе бота\n\n"
                         "❗ При возникновении ошибок, вопросов, предложений, Вы можете связаться со мной - @Fallern")
