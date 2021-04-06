from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards import keyboard_empty, keyboard_with_members, keyboard_with_tags, keyboard_with_deadline
from keyboards.new_task_keyboards import keyboard_with_lists
from loader import dp
from src.states import NewTask


"""
Pipeline for creating New Task in Trello
"""


@dp.message_handler(Command('new_task'))
async def create_task(message: types.Message):
    await message.answer('<b>Choose list</b>',
                         reply_markup=keyboard_with_lists)
    await NewTask.first()


@dp.message_handler(state=NewTask.list)
async def get_list(message: types.Message, state: FSMContext):
    board_list = message.text
    await state.update_data({'list': board_list})
    await message.answer('<b>Input header</b>',
                         reply_markup=keyboard_empty)
    await NewTask.next()


@dp.message_handler(state=NewTask.header)
async def get_header(message: types.Message, state: FSMContext):
    header = message.text.capitalize()
    await state.update_data({'header': header})
    await message.answer('<b>Input the description</b>',
                         reply_markup=keyboard_empty)
    await NewTask.next()


@dp.message_handler(state=NewTask.description)
async def get_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data({'description': description})
    await message.answer('<b>Choose member</b>',
                         reply_markup=keyboard_with_members)
    await NewTask.next()


@dp.message_handler(state=NewTask.member)
async def get_member(message: types.Message, state: FSMContext):
    member = message.text
    await state.update_data({'member': member})
    await message.answer('<b>Select tag or input with spaces</b>',
                         reply_markup=keyboard_with_tags)
    await NewTask.next()


@dp.message_handler(state=NewTask.tags)
async def get_tags(message: types.Message, state: FSMContext):
    tags = message.text.split(' ')
    await state.update_data({'tags': tags})
    await message.answer('<b>Choose deadline date, or input:\n'
                         'in hours: %h \n'
                         'in days: %d</b>',
                         reply_markup=keyboard_with_deadline)
    await NewTask.next()


@dp.message_handler(state=NewTask.deadline)
async def get_deadline(message: types.Message, state: FSMContext):
    deadline = message.text.split(' ')
    await state.update_data({'deadline': deadline})
    await message.answer('<b>Input Urls to attachment</b>',
                         reply_markup=keyboard_empty)
    await NewTask.next()


@dp.message_handler(state=NewTask.attachment)
async def get_attachment(message: types.Message, state: FSMContext):
    attachment = message.text.split(' ')
    await state.update_data({'attachment': attachment})
    await message.answer('<b>Chose cover</b>',
                         reply_markup=keyboard_empty)
    await NewTask.next()


@dp.message_handler(state=NewTask.cover)
async def get_cover(message: types.Message, state: FSMContext):
    cover = message.text.split(' ')
    await state.update_data({'cover': cover})
    new_task_data = await state.get_data()
    await message.answer('Task created',
                         reply_markup=ReplyKeyboardRemove())
    print(new_task_data)
    await state.finish()
