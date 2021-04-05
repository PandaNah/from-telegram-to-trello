import typing
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


def to_matrix(ls: typing.List[str], to_columns: int = 2):
    assert len(ls) not in [0, 1], 'List cant be empty'
    assert to_columns not in [0, 1,
                              range(len(ls) // 2, len(ls))], 'Modifier to_columns should be in range(2, len(ls)//2)'
    if len(ls) % 2 == 0:
        return [ls[i:i + to_columns] for i in range(0, len(ls), to_columns)]
    else:
        return [ls[i:i + to_columns] for i in range(0, len(ls) - 1, to_columns)] + [[ls[-1]]]


member_names = [Member.get_member(board_member.id_member).full_name for board_member in board_members]
member_names = [KeyboardButton(text=name) for name in member_names]
member_names = to_matrix(member_names)
keyboard_with_members = ReplyKeyboardMarkup(
    keyboard=[
        *member_names,
        [
            KeyboardButton(text='Without worker'),
            KeyboardButton(text='Cancel')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

tags_colors = ['Green🟩', 'Yellow🟨', 'Orange🟧', 'Red🟥', 'Purple🟪', 'Blue🟦']
tags_colors = [KeyboardButton(text=color) for color in tags_colors]
tags_colors = to_matrix(ls=tags_colors, to_columns=2)
keyboard_with_tags = ReplyKeyboardMarkup(
    keyboard=[
        *tags_colors,
        [
            KeyboardButton(text='Skip'),
            KeyboardButton(text='Cancel')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

if __name__ == '__main__':
    print(tags_colors)
