from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards import keyboard_empty, keyboard_with_members, keyboard_with_tags, keyboard_with_deadline, \
    keyboard_with_position
from keyboards.new_task_keyboards import keyboard_with_lists
from loader import dp
from src.states import NewTask
from src.utils import reformat_and_post, ValidateAnswers

"""
Pipeline for creating New Task in Trello
"""


@dp.message_handler(lambda message: not ValidateAnswers.validate_list(message.text), state=NewTask.list)
@dp.message_handler(lambda message: not ValidateAnswers.validate_member(message.text), state=NewTask.member)
@dp.message_handler(lambda message: not ValidateAnswers.validate_tags(message.text), state=NewTask.tags)
@dp.message_handler(lambda message: not ValidateAnswers.validate_deadline(message.text), state=NewTask.deadline)
@dp.message_handler(lambda message: not ValidateAnswers.validate_position(message.text), state=NewTask.position)
async def invalid_input(message: types.Message):
    return await message.reply('Invalid input')


@dp.message_handler(Command('new_task'))
async def create_task(message: types.Message):
    await message.answer('<b>Choose list</b>',
                         reply_markup=keyboard_with_lists)
    await NewTask.first()


@dp.message_handler(lambda message: ValidateAnswers.validate_list(message.text), state=NewTask.list)
async def get_list(message: types.Message, state: FSMContext):
    board_list = message.text
    await state.update_data({'idList': board_list})
    await message.answer('<b>Input header</b>',
                         reply_markup=keyboard_empty)
    await NewTask.next()


@dp.message_handler(state=NewTask.header)
async def get_header(message: types.Message, state: FSMContext):
    header = message.text.capitalize()
    await state.update_data({'name': header})
    await message.answer('<b>Input the description</b>',
                         reply_markup=keyboard_empty)
    await NewTask.next()


@dp.message_handler(state=NewTask.description)
async def get_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data({'desc': description})
    await message.answer('<b>Choose member</b>',
                         reply_markup=keyboard_with_members)
    await NewTask.next()


@dp.message_handler(lambda message: ValidateAnswers.validate_member(message.text), state=NewTask.member)
async def get_member(message: types.Message, state: FSMContext):
    member = message.text
    await state.update_data({'idMembers': member})
    await message.answer('<b>Select tag </b>',
                         reply_markup=keyboard_with_tags)
    await NewTask.next()


@dp.message_handler(lambda message: ValidateAnswers.validate_tags(message.text), state=NewTask.tags)
async def get_tags(message: types.Message, state: FSMContext):
    tags = message.text
    await state.update_data({'idLabels': tags})
    await message.answer('<b>Choose hours for work, or input:\n'
                         'in hours: %h \n'
                         'in days: %d</b>',
                         reply_markup=keyboard_with_deadline)
    await NewTask.next()


@dp.message_handler(lambda message: ValidateAnswers.validate_deadline(message.text), state=NewTask.deadline)
async def get_deadline(message: types.Message, state: FSMContext):
    deadline = message.text
    await state.update_data({'due': deadline})
    await message.answer('<b>Choose position</b>',
                         reply_markup=keyboard_with_position)
    await NewTask.next()


@dp.message_handler(lambda message: ValidateAnswers.validate_position(message.text), state=NewTask.position)
async def get_position(message: types.Message, state: FSMContext):
    position = message.text
    await state.update_data({'pos': position})
    new_task_data = await state.get_data()
    await message.answer('Task created',
                         reply_markup=ReplyKeyboardRemove())
    response_status_code, short_url = reformat_and_post(query=new_task_data)
    if response_status_code in range(200, 300):
        await message.answer(f'Task posted in trello:\n'
                             f'{short_url}')

    await state.finish()
