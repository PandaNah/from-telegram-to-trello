import typing

from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

from keyboards.new_task_keyboards import KeyboardBuilder


def test_keyboardbuilder() -> typing.NoReturn:
    """
    Test for KeyboardBuilder

    :return: NoReturn
    """
    test_list_of_values_1 = [1, 2, 3, 4, 5, 6]

    test_table_buttons = KeyboardBuilder.to_table_buttons(
        list_of_values=test_list_of_values_1,
        n_in_row=2,
    )

    assert len(test_table_buttons) == 3
    assert len(test_table_buttons[-1]) == 2

    test_convert_to_buttons = KeyboardBuilder.convert_to_buttons(
        list_of_values=test_list_of_values_1,
    )

    assert isinstance(test_convert_to_buttons, typing.List)
    assert isinstance(test_convert_to_buttons[0], KeyboardButton)

    test_keyboard = KeyboardBuilder.create_new_keyboard(
        list_of_values=test_list_of_values_1,
    )

    assert isinstance(test_keyboard, ReplyKeyboardMarkup)
    assert len(test_keyboard.keyboard) == 4
    assert test_keyboard.keyboard[-1] == ['Skip', 'Cancel']
