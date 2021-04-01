from dotenv import load_dotenv
import os
from dataclasses import dataclass
import typing


@dataclass
class GetEnv:
    TELEGRAM_TOKEN: typing.AnyStr
    ADMIN_LIST: typing.List[str]


load_dotenv()
envSettings = GetEnv(TELEGRAM_TOKEN=os.getenv('TELEGRAM_TOKEN'),
                     ADMIN_LIST=os.getenv('ADMIN_LIST').split(', '))

