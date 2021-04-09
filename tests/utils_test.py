import typing

import pytest

from src.exceptions import WrongDateFormat
from src.utils import ValidateAnswers


def test_validateanswers() -> typing.NoReturn:
    """
    Tests for ValidateAnswers

    :return: NoReturn
    """
    test_validator = ValidateAnswers()
    test_data = {
        'list': ['test', 'Готово'],
        'member': ['test', 'PandaNah'],
        'tags': ['test', 'Green'],
        'deadline': ['test', '1d', '24', '3h'],
        'position': ['test', 'top', 'bottom']
    }

    assert not test_validator.validate_list(test_data.get('list')[0])
    assert test_validator.validate_list(test_data.get('list')[1])

    assert not test_validator.validate_member(test_data.get('member')[0])
    assert test_validator.validate_member(test_data.get('member')[1])

    assert not test_validator.validate_tags(test_data.get('tags')[0])
    assert test_validator.validate_tags(test_data.get('tags')[1])

    assert not test_validator.validate_deadline(test_data.get('deadline')[0])
    assert test_validator.validate_deadline(test_data.get('deadline')[1])
    assert test_validator.validate_deadline(test_data.get('deadline')[2])
    assert test_validator.validate_deadline(test_data.get('deadline')[3])

    assert not test_validator.validate_position(test_data.get('position')[0])
    assert test_validator.validate_position(test_data.get('position')[1])
    assert test_validator.validate_position(test_data.get('position')[2])
