from dotenv import load_dotenv
import os
from dataclasses import dataclass
import typing


@dataclass
class TelegramEnv:
    TELEGRAM_TOKEN: typing.AnyStr
    ADMIN_LIST: typing.List[str]


@dataclass
class TrelloEnv:
    TRELLO_KEY: typing.AnyStr
    TRELLO_TOKEN: typing.AnyStr
    BOARD_ID: typing.AnyStr


load_dotenv()

envSettings = TelegramEnv(
    TELEGRAM_TOKEN=os.getenv('TELEGRAM_TOKEN'),
    ADMIN_LIST=os.getenv('ADMIN_LIST').split(', ')
)

trelloSettings = TrelloEnv(
    TRELLO_KEY=os.getenv('TRELLO_KEY'),
    TRELLO_TOKEN=os.getenv('TRELLO_TOKEN'),
    BOARD_ID=os.getenv('BOARD_ID'),
)
