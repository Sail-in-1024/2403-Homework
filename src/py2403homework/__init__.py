import logging
import datetime
import time

__all__ = ['Library', 'Event', 'Homework']

logger = logging.getLogger(__name__)

date_like = datetime.date | str | None


class Event:

    DEFAULT_NAME = '事件'
    DEFAULT_CONTENT = ''
    TITLE_SYMBOL = '~'

    def __init__(self,
                 description: str | None = None,
                 name: str | None = None,
                 date: date_like = None,
                 content: str | None = None):
        if description:
            addition = ' --- ' + description
        else:
            addition = ''
        if name is None:
            name = self.DEFAULT_NAME
        if date:
            try:
                date = f'{date.year:0>4}/{date.month:0>2}/{date.day:0>2}'
            except AttributeError:
                pass
        else:
            date = time.strftime('%Y/%m/%d')
        self.title = f'{date} {name}{addition}'
        if content:
            self.content = content
        else:
            self.content = self.DEFAULT_CONTENT

    def dumps(self):
        return f"{self.title}\n{self.TITLE_SYMBOL * len(self.title)}\n\n{self.content}"

class Homework(Event):

    DEFAULT_NAME = '作业'

    def __init__(self,
                 date: date_like = None,
                 date_limit: str | None = None,
                 description: str | None = None,
                 content: str | None = None):
        if date_limit:
            if content:
                content = f'*{date_limit.strip()}*\n\n{content}'
            else:
                content = date_limit
        super().__init__(description, date=date, content=content)
        self.subjects = []

class Subject:

    def __init__(self, name: str):
        self.name = name

class Library:
    ...

if __name__ == '__main__':
    pass