import typing

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.new_task_keyboards import KeyboardBuilder


def test_keyboardbuilder() -> typing.NoReturn:
    """
    Test for KeyboardBuilder

    :return: NoReturn
    """
    test_list_of_values_1 = [1, 2, 3, 4, 5, 6]

    test_keyboard_1 = KeyboardBuilder(test_list_of_values_1)
    assert test_keyboard_1.list_of_values == test_list_of_values_1
    assert test_keyboard_1.skip_cancel_buttons == [KeyboardButton(text='Skip'), KeyboardButton(text='Cancel')]

    test_table_buttons = test_keyboard_1.to_table_buttons(list_of_values=test_list_of_values_1, n_in_row=2)
    assert len(test_table_buttons) == 3
    assert len(test_table_buttons[-1]) == 2

    test_convert_to_buttons_1 = test_keyboard_1.convert_to_buttons(list_of_values=test_list_of_values_1)
    assert isinstance(test_convert_to_buttons_1, typing.List)
    assert isinstance(test_convert_to_buttons_1[0], KeyboardButton)

    test_new_keyboard_1 = test_keyboard_1.create_new_keyboard()
    assert isinstance(test_new_keyboard_1, ReplyKeyboardMarkup)
    assert len(test_new_keyboard_1.keyboard) == 4
    assert test_new_keyboard_1.resize_keyboard
    assert test_new_keyboard_1.one_time_keyboard

