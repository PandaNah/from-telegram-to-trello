import typing

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from src.trello_boards import TrelloBoard
from src.trello_member import TrelloMember


class KeyboardBuilder:
    """
    Helps to create KeyBoards
    """
    def __init__(self, list_of_values: typing.List[typing.Any]):
        self.list_of_values = list_of_values
        self.skip_cancel_buttons = [
            KeyboardButton(text='Skip'),
            KeyboardButton(text='Cancel')
        ]

    def create_new_keyboard(self) -> ReplyKeyboardMarkup:
        """
        Create new keyboard with your list of values and Skip&Cancel buttons.

        :return: ReplyKeyboardMarkup
        """
        list_of_values = self.convert_to_buttons(self.list_of_values)
        if len(self.list_of_values) not in range(2):
            list_of_values = self.to_table_buttons(list_of_values=list_of_values,
                                                   n_in_row=2)
        keyboard = ReplyKeyboardMarkup(
            keyboard=[*list_of_values, self.skip_cancel_buttons],
            resize_keyboard=True,
            one_time_keyboard=True
        )
        return keyboard

    @staticmethod
    def to_table_buttons(list_of_values: typing.List[typing.Any], n_in_row: int = 2) -> typing.List[typing.Any]:
        """
        Help function to make matrix from list of values

        :param list_of_values: any list with values
        :param n_in_row: number of elements in a row
        :return: List[Any] (matrix[n_in_row, -1])
        """
        return [list_of_values[i:i+n_in_row] for i in range(0, len(list_of_values), n_in_row)]

    @staticmethod
    def convert_to_buttons(list_of_values: typing.List[typing.Any]) -> typing.List[KeyboardButton]:
        """
        Help function to make KeyboardButton from values

        :param list_of_values: any list with values
        :return: List[KeyboardButton]
        """
        return [KeyboardButton(text=value) for value in list_of_values]


Board = TrelloBoard()
board_lists = [board_list.list_name for board_list in Board.get_lists()]
board_members = Board.get_memberships()
Member = TrelloMember()
member_names = [Member.get_member(board_member.member_id).member_fullname for board_member in board_members]
tags_colors = Board.get_labels()
tags_colors = [label.cardlabel_color.title() for label in tags_colors]
deadline_times = [1, 2, 5, 24, 48, 72, 96, 120]


keyboard_empty = KeyboardBuilder([]).create_new_keyboard()
keyboard_with_lists = KeyboardBuilder(board_lists).create_new_keyboard()
keyboard_with_members = KeyboardBuilder(member_names).create_new_keyboard()
keyboard_with_tags = KeyboardBuilder(tags_colors).create_new_keyboard()
keyboard_with_deadline = KeyboardBuilder(deadline_times).create_new_keyboard()
keyboard_with_position = KeyboardBuilder(['top', 'bottom']).create_new_keyboard()
