import numpy as np
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from src.trello_boards import TrelloBoard
from src.trello_member import TrelloMember


keyboard_with_none = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Skip'),
            KeyboardButton(text='Cancel')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

Board = TrelloBoard()
board_members = Board.get_memberships()

Member = TrelloMember()

member_names = [Member.get_member(board_member.id_member).full_name for board_member in board_members]

keyboard_with_members = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=name) for name in member_names # TODO: Гибкую систему вывода множества исполнителей
        ],
        [
            KeyboardButton(text='Without worker'),
            KeyboardButton(text='Cancel')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

if __name__ == '__main__':
    print(member_names)