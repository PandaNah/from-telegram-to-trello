from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

board_none = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='None'),
            KeyboardButton(text='Cancel')
        ]
    ],
    resize_keyboard=True
)
