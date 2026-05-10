"""
提供了一些有用的类型，用于生成作业文档源文件。

This module provides some useful types to generate source files of homework documentation.
"""

import logging
import datetime
import abc
import time
import unicodedata

__all__ = ['Library', 'Generatable', 'Simple', 'Event', 'Homework']

logger = logging.getLogger(__name__)

date_like = datetime.date | str | None

class Generatable(metaclass=abc.ABCMeta):
    
    """
    :term:`可生成文档类型 <doc-generatable>`\ 的抽象基类。
    
    Abstract base class of :term:`doc-generatable` types.
    """

    @abc.abstractmethod
    def dumps(self) -> str:
        """
        实现生成 reStructuredText 形式的文档的功能。
        
        Implement generating reStructuredText format of a documentation.
        
        :return: reStructuredText 源码
           sourcecode
        :rtype: str
        """
        pass

class Simple(Generatable):
    
    """
    :term:`可生成文档类型`\ 的一个简单实现。
    
    A simple implementation of a :term:`doc-generatable` type.
    
    :arg title: 章节标题，不能超过一行
       section title within a line
    :arg content: 标题后的正文
       the body after ``title``
    """
    
    #: 装饰标题所使用的标点符号
    #:
    #: punctuation character for marking titles
    TITLE_SYMBOL: str = '~'

    def __init__(self,
                 title: str,
                 content: str | None = None):
        #: 由 ``title`` 参数设置
        #:
        #: set by argument ``title``
        self.title = title
        if content:
            #: 由 ``content`` 参数设置
            #:
            #: set by argument ``content``
            self.content = content
        else:
            self.content = ''

    def __str__(self):
        """
        :meth:`.dumps` 方法的快捷方式。
        
        The shortcut for :meth:`.dumps`.
        
        :rtype: str
        """
        return self.dumps()

    def dumps(self) -> str:
        r"""
        生成文档。
        
        Generate the documentation.
        
        先调用 :meth:`.generate_title` 生成标题部分，与后面的 :attr:`content` 以 ``\n\n`` 相隔，即一个空行。
        
        Call :meth:`.generate_title` first to generate the title part, followed by ``\n\n`` (A blank line), then :attr:`content`.
        """
        return self.generate_title() + '\n\n' + self.content

    def generate_title(self) -> str:
        """
        生成文档标题部分的 reStructuredText 形式。
        
        Generate reStructuredText format of the title part of the documentation.
        
        标题最先出现，再是一些用于装饰的标点符号。
        
        The title comes first, then punctuation characters for marking.
        
        :return: reStructuredText 格式的章节标记
        :rtype: str
        """
        width = 0
        for char in self.title:
            eaw = unicodedata.east_asian_width(char)
            if eaw in ('F', 'W'):
                width += 2
            else:
                width += 1
        return self.title + '\n' + self.TITLE_SYMBOL * width

class Event(Simple):

    """
    普通事件类型，也是所有 :term:`event type` 的基类。
    
    General event type, also the base class of all :term:`event type`\ s.
    
    :arg description: 对于事件的描述，若不为空，则标题后会加上 `` --- {description}``
    """

    #: 默认事件类型名称，作为 ``name`` 参数的默认值使用
    #:
    #: default event format name, used as the default value of argument ``name``
    DEFAULT_NAME: str = '事件'

    #: 默认内容，作为 ``content`` 参数的默认值使用
    #:
    #: default content, used as the default value of argument ``content``
    DEFAULT_CONTENT: str = ''

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
                date = time.strftime('%Y/%m/%d')
        else:
            date = time.strftime('%Y/%m/%d')
        title = f'{date} {name}{addition}'
        if content is None:
            content = self.DEFAULT_CONTENT
        super().__init__(title, content)

class Homework(Event):

    DEFAULT_NAME = '作业'

    def __init__(self,
                 date: date_like = None,
                 date_limit: str | None = None,
                 description: str | None = None,
                 content: str | None = None,
                 content_fmt: str | None = None):
        if date_limit:
            if content:
                content = f'*{date_limit.strip()}*\n\n{content}'
            else:
                content = date_limit
        if content_fmt is not None:
            content = content_fmt.format(content)
        super().__init__(description, date=date, content=content)
        self.content_fmt = content_fmt
        self.subjects: list['Subject'] = []

    def dumps(self):
        return super().dumps()

    def update_content(self):
        content = f''
        for subject in self.subjects:
            content += subject.dumps()

class Subject(Simple):

    TITLE_SYMBOL = '-'

    def __init__(self, name: str, content: str | None = None):
        super().__init__(name, content)

class Library:
    ...

if __name__ == '__main__':
    print(Homework(date_limit='4.28~4.29', description='description', content='content', content_fmt='Content:\n{}'))