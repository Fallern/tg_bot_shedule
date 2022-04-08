from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    name = State()
    college_number = State()
    page_data = State()
    group = State()

