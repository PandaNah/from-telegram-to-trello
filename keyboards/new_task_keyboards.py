import typing

from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

from src.trello_boards import TrelloBoard


class KeyboardBuilder:
    """
    Helps to create KeyBoards
    """

    @classmethod
    def create_new_keyboard(
            cls,
            list_of_values: typing.List[typing.Any],
            need_skip=True,
    ) -> ReplyKeyboardMarkup:
        """
        Create new keyboard with your list of values and Skip&Cancel buttons.

        :return: ReplyKeyboardMarkup
        """
        list_of_values = cls.convert_to_buttons(list_of_values)
        if len(list_of_values) not in range(2):
            list_of_values = cls.to_table_buttons(
                list_of_values=list_of_values,
                n_in_row=2,
            )
        keyboard = ReplyKeyboardMarkup(
            keyboard=list_of_values,
            resize_keyboard=True,
        )
        keyboard.add('Skip' * need_skip, 'Cancel')
        return keyboard

    @staticmethod
    def to_table_buttons(
            list_of_values: typing.List[typing.Any],
            n_in_row: int = 2,
    ) -> typing.List[typing.Any]:
        """
        Help function to make matrix from list of values

        :param list_of_values: any list with values
        :param n_in_row: number of elements in a row
        :return: List[Any] (matrix[n_in_row, -1])
        """
        return [
            list_of_values[i:i + n_in_row]
            for i in range(0, len(list_of_values), n_in_row)
        ]

    @staticmethod
    def convert_to_buttons(
            list_of_values: typing.List[typing.Any],
    ) -> typing.List[KeyboardButton]:
        """
        Help function to make KeyboardButton from values

        :param list_of_values: any list with values
        :return: List[KeyboardButton]
        """
        return [KeyboardButton(text=value) for value in list_of_values]


Board = TrelloBoard()
board_lists = [board_list.name for board_list in Board.get_lists()]
member_names = [member.fullName for member in Board.get_members()]
tags_colors = Board.get_labels()
tags_colors = [label.color.title() for label in tags_colors]
deadline_times = [1, 2, 5, 24, 48, 72, 96, 120]
positions = ['top', 'bottom']

keyboard_empty = KeyboardBuilder.create_new_keyboard([])
keyboard_with_lists = KeyboardBuilder.create_new_keyboard(
    list_of_values=board_lists, need_skip=False,
)
keyboard_with_members = KeyboardBuilder.create_new_keyboard(
    list_of_values=member_names,
)
keyboard_with_tags = KeyboardBuilder.create_new_keyboard(
    list_of_values=tags_colors,
)
keyboard_with_deadline = KeyboardBuilder.create_new_keyboard(
    list_of_values=deadline_times,
)
keyboard_with_position = KeyboardBuilder.create_new_keyboard(
    list_of_values=positions, need_skip=False,
)
