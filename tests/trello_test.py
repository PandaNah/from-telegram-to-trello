import typing
from random import choice

import pytest
from faker import Faker

from src.trello_boards import TrelloBoard
from src.trello_cards import TrelloCard
from src.trello_dataclasses import SerializedCard
from src.trello_dataclasses import SerializedCardLabels
from src.trello_dataclasses import SerializedList
from src.trello_dataclasses import SerializedMember


class TestTrelloBoard:
    """
    Future description
    """

    @staticmethod
    def get_test_list():
        _b = TrelloBoard()
        test_list_id = None
        for _list in _b.get_lists():
            if _list.name == 'TESTCASE1':
                test_list_id = _list.list_id
        if test_list_id:
            return test_list_id
        raise Exception

    @classmethod
    @pytest.fixture()
    def setup_list(cls):
        _b = TrelloBoard()
        for _list in _b.get_lists(list_filter='all'):
            if _list.name == 'TESTCASE1':
                if _list.closed:
                    _b.archive_list(
                        list_id=_list.list_id,
                        archive=False,
                    )
                    break
        else:
            _b.create_list(
                list_name='TESTCASE1',
                list_pos='top',
            )

        yield

        _b.archive_list(
            list_id=cls.get_test_list(),
            archive=True,
        )

    @classmethod
    @pytest.fixture()
    def setup_cards(cls):
        fake = Faker()
        _b = TrelloBoard()
        _c = TrelloCard()

        test_list_id = cls.get_test_list()
        to_remove_list = []

        for _ in range(5):
            test_case = {
                'name': fake.name(),
                'desc': fake.text(),
                'pos': choice(['top', 'bottom']),
                'due': fake.iso8601(),
                'idList': test_list_id,
                'idMembers': choice([
                    user.member_id
                    for user in _b.get_members()
                ] + ['']),
                'idLabels': choice([
                    label.label_id
                    for label in _b.get_labels()
                ] + ['']),
            }

            r = _c.post_card(**test_case)
            assert r.status_code == 200
            to_remove_list.append(r.json().get('id'))

        yield

        for _ in to_remove_list:
            _c.delete_card(card_id=_)

    @classmethod
    @pytest.fixture()
    def setup_demons(cls):
        fake = Faker()
        _b = TrelloBoard()

        to_remove_list = []

        for _ in range(3):
            _n = fake.name()
            r = _b.invite_member(
                email=fake.ascii_free_email(),
                full_name=_n,
            )
            assert r.status_code == 200
            to_remove_list.append(_n)

        yield

        _members = _b.get_members()
        for _ in _members:
            if _.fullName in to_remove_list:
                to_remove_list[to_remove_list.index(_.fullName)] = _.member_id

        for _ in to_remove_list:
            _b.remove_member(member_id=_)

    @staticmethod
    @pytest.fixture()
    def setup_env() -> typing.List:
        _b = TrelloBoard()
        _c = TrelloCard()
        return [_b, _c]

    @staticmethod
    def test_get_members(setup_env, setup_demons):
        _b, _ = setup_env
        _demons = _b.get_members()
        assert isinstance(_demons, typing.List)
        assert isinstance(_demons[0], SerializedMember)

    @staticmethod
    def test_get_member(setup_env, setup_demons):
        _b, _ = setup_env
        _demons = _b.get_members()
        r = _b.get_member(member_id=choice(_demons).member_id)
        assert isinstance(r, SerializedMember)

    @staticmethod
    def test_get_lists(setup_env, setup_list):
        _b, _ = setup_env
        r = _b.get_lists()
        assert isinstance(r, typing.List)
        assert isinstance(r[0], SerializedList)

    @staticmethod
    def test_invite_remove_member(setup_env):
        _b, _ = setup_env
        fake = Faker()
        _email = fake.ascii_free_email()
        _name = fake.name()
        r = _b.invite_member(
            email=_email,
            full_name=_name,
        )
        assert r.status_code == 200

        _members = _b.get_members()
        _remove_id = None

        for _ in _members:
            if _.fullName == _name:
                _remove_id = _.member_id

        assert _remove_id

        r = _b.remove_member(member_id=_remove_id)

        assert r.status_code == 200

    @staticmethod
    def test_create_list(setup_env):
        _b, _ = setup_env
        r = _b.create_list(
            list_name='lyalya',
            list_pos='bottom',
        )
        assert r.status_code == 200

    @staticmethod
    def test_archive_list(setup_env):
        _b, _ = setup_env
        _list_id = None
        for _ in _b.get_lists():
            if _.name == 'lyalya':
                _list_id = _.list_id
        r = _b.archive_list(list_id=_list_id)

        assert r.status_code == 200

    @staticmethod
    def test_get_cards(setup_env, setup_list, setup_cards):
        _b, _ = setup_env
        r = _b.get_cards()
        assert isinstance(r, typing.List)
        assert isinstance(r[0], SerializedCard)

    @staticmethod
    def test_get_card(setup_env, setup_list, setup_cards):
        _b, _ = setup_env
        _cards = _b.get_cards()
        _card = choice(_cards).card_id
        r = _b.get_card(card_id=_card)

        assert isinstance(r, SerializedCard)

    @staticmethod
    def test_get_labels(setup_env):
        _b, _ = setup_env
        r = _b.get_labels()

        assert isinstance(r, typing.List)
        assert isinstance(r[0], SerializedCardLabels)

    @staticmethod
    def test_create_label(setup_env):
        _b, _ = setup_env
        for _ in range(3):
            r = _b.create_label(
                label_name=_,
                label_color=choice([_.color for _ in _b.get_labels()]),
            )
            assert r.status_code == 200

    @staticmethod
    def test_delete_label(setup_env):
        _b, _ = setup_env
        _labels = [
            _.label_id for _ in _b.get_labels(
            ) if _.name in map(str, range(3))
        ]
        for _ in _labels:
            r = _b.delete_label(label_id=_)

            assert r.status_code == 200
