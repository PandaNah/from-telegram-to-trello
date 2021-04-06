import typing

from src.trello_boards import TrelloBoard
from src.trello_dataclasses import BoardMembership, BoardList, BoardMember
from settings import trelloSettings
from src.trello_lists import TrelloList
from src.trello_member import TrelloMember


def test_trelloboard() -> typing.NoReturn:
    """
    Tests for TrelloBoard

    :return: NoReturn
    """
    test_board = TrelloBoard()
    assert test_board.primary_url == f'boards/{trelloSettings.BOARD_ID}/'

    test_members = test_board.get_memberships()
    assert isinstance(test_members, typing.List)
    assert isinstance(test_members[0], BoardMembership)

    test_lists = test_board.get_lists()
    assert isinstance(test_lists, typing.List)
    assert isinstance(test_lists[0], BoardList)


def test_trellolist() -> typing.NoReturn:
    """
    Tests for TrelloList

    :return: NoReturn
    """
    test_list = TrelloList()
    assert test_list.primary_url == 'lists/'

    list_id = TrelloBoard().get_lists()[0].list_id
    test_board_list = test_list.get_list(list_id=list_id)
    assert isinstance(test_board_list, BoardList)


def test_trellomember() -> typing.NoReturn:
    """
    Tests for TrelloMember

    :return: NoReturn
    """
    test_member = TrelloMember()
    assert test_member.primary_url == 'members/'

    member_id = TrelloBoard().get_memberships()[0].member_id
    member = test_member.get_member(member_id=member_id)
    assert isinstance(member, BoardMember)
