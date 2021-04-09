import typing
from datetime import datetime, timedelta

from src.exceptions import WrongDateFormat
from src.trello_boards import TrelloBoard
from src.trello_cards import TrelloCard
from src.trello_member import TrelloMember


def reformat_and_post(query: typing.Dict[str, typing.Union[str, typing.List]]) -> typing.Tuple[int, str]:
    """
    Help function to modify dict with states from /new_task and post it to Trello

    :param query: Dictionary with states from /new_task
    :return: response.status_code, response.shortUrl
    """
    # Swap Skip to empty string
    for key, value in query.items():
        if value == 'Skip':
            query.update({key: ''})
    # Get columns and members from Trello
    trello_board = TrelloBoard()
    trello_board_lists = trello_board.get_lists()
    trello_board_members = trello_board.get_memberships()
    # Get members names and labels from board
    trello_member = TrelloMember()
    trello_members = [trello_member.get_member(member_id=member.member_id) for member in trello_board_members]
    trello_labels = trello_board.get_labels()
    # Swap list.name to list.id
    if query.get('idList'):
        for _ in trello_board_lists:
            if _.list_name == query.get('idList'):
                query.update({'idList': _.list_id})
    # Swap member.name to member.id
    if query.get('idMembers'):
        for _ in trello_members:
            if _.member_fullname == query.get('idMembers'):
                query['idMembers'] = [_.member_id]
    # Swap label color.name to color.id
    if query.get('idLabels'):
        for _ in trello_labels:
            if _.cardlabel_color == query.get('idLabels').lower():
                query.update({'idLabels': _.cardlabel_id})
    # Set due
    if query.get('due'):
        _hours = datetime.now()
        _users_hours = query.get('due')
        if _users_hours.isnumeric():
            _hours += timedelta(hours=int(_users_hours))
        elif ('h' in _users_hours) & (_users_hours[:-1].isnumeric()):
            _hours += timedelta(hours=int(_users_hours[:-1]))
        elif ('d' in _users_hours) & (_users_hours[:-1].isnumeric()):
            _hours += timedelta(days=int(_users_hours[:-1]))
        else:
            raise WrongDateFormat(_users_hours)

        query.update({'due': _hours.strftime('%Y-%m-%dT%H:%M:00.000Z')})
    # Post query to Trello
    client = TrelloCard()
    response = client.post_card(**query)
    short_url = response.json().get('shortUrl')

    return response.status_code, short_url


class ValidateAnswers:
    @staticmethod
    def validate_list(text: typing.Union[str]) -> bool:
        """
        Validate available lists

        :param text: message.text from user
        :return: bool
        """
        board_lists = [board_list.list_name for board_list in TrelloBoard().get_lists()]
        board_lists += ['Skip']
        return True if text in board_lists else False

    @staticmethod
    def validate_member(text: typing.Union[str]) -> bool:
        """
        Validate available member

        :param text: message.text from user
        :return: bool
        """
        member_names = TrelloMember().get_members_names()
        member_names += ['Skip']
        return True if text in member_names else False

    @staticmethod
    def validate_tags(text: typing.Union[str]) -> bool:
        """
        Validate available tag

        :param text: message.text from user
        :return: bool
        """
        board_tags = [label.cardlabel_color.title() for label in TrelloBoard().get_labels()]
        board_tags += ['Skip']
        return True if text in board_tags else False

    @staticmethod
    def validate_deadline(text: typing.Union[str]) -> bool:
        """
        Validate available deadline

        :param text: message.text from user
        :return: bool
        """
        if text.isnumeric():
            return True
        elif (text[-1] == 'h') & (text[:-1].isnumeric()):
            return True
        elif (text[-1] == 'd') & (text[:-1].isnumeric()):
            return True
        elif text == 'Skip':
            return True
        else:
            return False

    @staticmethod
    def validate_position(text: typing.Union[str]) -> bool:
        """
        Validate available position

        :param text: message.text from user
        :return: bool
        """
        return True if text in ['top', 'bottom', 'Skip'] else False
