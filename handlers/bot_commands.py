import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from src.utils import get_board_lists
from src.utils import get_cards_list
from src.utils import get_users_list

logging.basicConfig(level=logging.INFO)


@dp.message_handler(CommandStart())
async def start_function(message: types.Message):
    await message.answer(text='Welcome')


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(
    Text(
        equals=['cancel', 'Cancel'],
        ignore_case=True,
    ), state='*',
)
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


@dp.inline_handler(text='')
async def empty_inline(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id='empty',
                title='Start entry one of the list name, or users',
                input_message_content=types.InputTextMessageContent(
                    message_text='This is inline mode, '
                                 'enter the name of list or user',
                ),
            ),
        ],
        cache_time=5,
    )


@dp.inline_handler(lambda query: query.query.lower() in 'users')
async def users_inline(query: types.InlineQuery):
    user_list = get_users_list()
    results = [
        types.InlineQueryResultArticle(
            id=member.member_id,
            title=member.username,
            description=member.fullName,
            thumb_url=member.avatarUrl,
            input_message_content=types.InputTextMessageContent(
                message_text='TODO' + member.fullName,
            ),
        )
        for member in user_list
    ]
    await query.answer(
        results=results,
        cache_time=10,
    )


@dp.inline_handler()
async def lists_inline(query: types.InlineQuery):
    lists_list = get_board_lists()
    look_list = None
    for _list in lists_list:
        if query.query.lower() in _list.name.lower():
            look_list = _list.list_id

    cards_list = get_cards_list(list_id=look_list)
    results = [
        types.InlineQueryResultArticle(
            id=card.card_id,
            title=card.name,
            description=card.desc,
            input_message_content=types.InputTextMessageContent(
                message_text='TODO',
            ),
        )
        for card in cards_list
    ]

    await query.answer(
        results=results,
        cache_time=10,
    )
