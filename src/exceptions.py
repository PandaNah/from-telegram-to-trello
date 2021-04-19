class WrongDateFormat(Exception):
    def __init__(self, date):
        super().__init__(f'Не верный формат даты : {date}')


class WrongCallMethod(Exception):
    def __init__(self, call_method):
        super().__init__(
            f'Call method should be '
            f'GET, PUT, POST or DELETE '
            f'not {call_method}',
        )


class UnAuthorized(Exception):
    def __init__(self):
        super().__init__(
            'Wrong trello settings. Trello key or Trello token',
        )


class ResourceUnavailable(Exception):
    def __init__(self):
        super().__init__('Trello is unavailable now.')
