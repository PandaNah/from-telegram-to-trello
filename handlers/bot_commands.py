import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

logging.basicConfig(level=logging.INFO)


@dp.message_handler(CommandStart())
async def start_function(message: types.Message):
    user_data = message.from_user.to_python()
    # TODO: управление, хранение, в общем какую-ту отчетность по доскам от пользователя
    # TODO: сделать бд
    await message.answer(text='Welcome')


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals=['cancel', 'Cancel'], ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())