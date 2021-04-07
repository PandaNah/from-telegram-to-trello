class WrongDateFormat(Exception):
    def __init__(self, date):
        super().__init__(f'Не верный формат даты : {date}')
