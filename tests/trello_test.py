import typing

from requests import Response

from src.trello_boards import TrelloBoard
from src.trello_cards import TrelloCard
from src.trello_dataclasses import BoardMembership, BoardList, BoardMember, TrelloCardBase, TrelloCardLabels
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

    test_cards = test_board.get_cards()
    f = False
    if not test_cards:
        t = TrelloCard()
        q = {'idList': '606d78d2c576327a2615dd01',
             'name': '1'}
        t.post_card(**q)
        test_cards = test_board.get_cards()
        f = True
    assert isinstance(test_cards, typing.List)
    assert isinstance(test_cards[0], TrelloCardBase)
    if f:
        for card in test_cards:
            if card.card_header == q.get('name'):
                card_to_remove = card.card_id
        t.delete_card(card_id=card_to_remove)

    test_labels = test_board.get_labels()
    assert isinstance(test_labels, typing.List)
    assert isinstance(test_labels[0], TrelloCardLabels)


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


def test_trellocard() -> typing.NoReturn:
    """
    Test for TrelloCard

    :return: NoReturn
    """
    test_cards = TrelloCard()
    assert test_cards.primary_url == 'cards/'

    test_query = {'idList': '606d78d2c576327a2615dd01',
                  'name': '1',
                  'desc': '2',
                  'idMembers': ['6065a3598039446570cdda2a'],
                  'idLabels': '6065a3a4184d2c731b7f0751',
                  'due': '2021-04-07T18:43:00.000Z',
                  'pos': 'bottom'}

    response = test_cards.post_card(**test_query)
    assert isinstance(response, Response)
    assert response.status_code in range(200, 300)
    assert 'trello' in response.json().get('shortUrl')

    card_id = TrelloBoard().get_cards()[0].card_id
    assert isinstance(card_id, str)
    test_card = test_cards.get_card(card_id=card_id)
    assert isinstance(test_card, TrelloCardBase)

    cards_on_board = TrelloBoard().get_cards()
    for card in cards_on_board:
        if card.card_header == test_query.get('name'):
            card_to_remove = card.card_id

    response = test_cards.delete_card(card_id=card_to_remove)
    assert response.status_code in range(200, 300)
    cards_on_board = [card.card_id for card in TrelloBoard().get_cards()]
    assert card_to_remove not in cards_on_board
