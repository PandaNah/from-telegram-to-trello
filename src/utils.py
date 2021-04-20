import typing
from datetime import datetime
from datetime import timedelta

from src.exceptions import WrongDateFormat
from src.trello_boards import TrelloBoard
from src.trello_cards import TrelloCard


def reformat_and_post(
        query: typing.Dict[str, typing.Union[str, typing.List]],
) -> typing.Tuple[int, str]:
    """
    Help function to modify dict with
    states from /new_task and post it to Trello

    :param query: Dictionary with states from /new_task
    :return: response.status_code, response.shortUrl
    """
    # Swap Skip to empty string
    for key, value in query.items():
        if value == 'Skip':
            query.update({key: ''})
    # Get columns and members from Trello
    board = TrelloBoard()
    trello_board_lists = board.get_lists()
    trello_board_members = board.get_members()
    trello_board_labels = board.get_labels()
    # Swap list.name to list.id
    if query.get('idList', None):
        for _ in trello_board_lists:
            if _.name == query.get('idList'):
                query.update({'idList': _.list_id})
    # Swap member.name to member.id
    if query.get('idMembers', None):
        for _ in trello_board_members:
            if _.fullName == query.get('idMembers'):
                query.update({'idMembers': _.member_id})
    # Swap label color.name to color.id
    if query.get('idLabels', None):
        for _ in trello_board_labels:
            if _.color == query.get('idLabels').lower():
                query.update({'idLabels': _.label_id})
    # Set due
    if query.get('due', None):
        current_datetime = datetime.now()
        users_hours = query.get('due')
        if users_hours.isnumeric():
            current_datetime += timedelta(hours=int(users_hours))
        elif ('h' in users_hours) & (users_hours[:-1].isnumeric()):
            current_datetime += timedelta(hours=int(users_hours[:-1]))
        elif ('d' in users_hours) & (users_hours[:-1].isnumeric()):
            current_datetime += timedelta(days=int(users_hours[:-1]))
        else:
            raise WrongDateFormat(users_hours)

        query.update(
            {'due': current_datetime.strftime('%Y-%m-%dT%H:%M:00.000Z')},
        )
    # Post query to Trello
    client = TrelloCard()
    print(query)
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
        board_lists = [
            board_list.name for board_list in TrelloBoard().get_lists()
        ] + ['Skip']
        return True if text in board_lists else False

    @staticmethod
    def validate_member(text: typing.Union[str]) -> bool:
        """
        Validate available member

        :param text: message.text from user
        :return: bool
        """
        member_names = [
            member.fullName for member in TrelloBoard().get_members()
        ] + ['Skip']
        return True if text in member_names else False

    @staticmethod
    def validate_tags(text: typing.Union[str]) -> bool:
        """
        Validate available tag

        :param text: message.text from user
        :return: bool
        """
        board_tags = [
            label.color.title()
            for label in TrelloBoard().get_labels()
        ] + ['Skip']
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
