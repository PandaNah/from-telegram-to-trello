from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup


class NewTask(StatesGroup):
    header = State()
    description = State()
    member = State()
    tags = State()
    deadline = State()
    attachment = State()
    cover = State()