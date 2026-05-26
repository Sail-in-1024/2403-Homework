"""
面向行，解析和运行命令。

*Orienting towards line, parse and run commands.*

.. hint::
   
   这个模块只提供解析和执行命令的接口。要在命令行中调用，请使用 ``python -m py2403homework`` 以运行 ``__main__.py``。
   
   This module only provides interfaces for parsing and executing commands. To invoke in command line, use ``python -m py2403homework`` to run ``__main__.py``.

使用样例
--------

Sample

.. code-block:: console
   
   python -m py2403homework -u Event

选项
----

Options

.. option:: -u <util>, --use <util>, --util=<util>
   
   选择一个事件类型。``<util>`` 必须存在于 :mod:`py2403homework.utils` 中，否则将引发 :exc:`ValueError`。
   
   Select an event type, which must exist in :mod:`py2403homework.utils`, or a :exc:`ValueError` will be raised.
"""

from argparse import ArgumentParser
try:
    from . import utils
except ImportError:
    import utils


#: 用于解析命令行参数。:func:`run` 的默认值。
#:
#: Used to parse command line parameters. The default value of :func:`run`. 
parser: ArgumentParser = ArgumentParser(
    # prog='python -m py2403homework',
    description = 'A tool to generate reST content for homework',
)
parser.add_argument('-u', '--use', '--util', default='Homework', help='event type')

def run(args=None, parser: ArgumentParser = parser):
    r"""
    运行指定的命令。
    
    Run specified command.
    
    :arg args: 待解析的命令行参数，调用时将作为 ``parser`` 的 :meth:`argparse.ArgumentParser.parse_args` 方法中的 ``args`` 参数。可以是一个由字符串组成的序列，或是一个字符串；若 ``args`` 为空，则使用 :data:`sys.argv` （详见 :mod:`argparse` 文档）
       
       command line parameters to be parased, which will be as argument ``args`` of method :meth:`argparse.ArgumentParser.parse_args` of ``parser``. It could be a sequence consists of strings, or a simply a string; if it's ``None``, :data:`sys.argv` will be used instead (To learn more, visit :mod:`argparse`\ 's documentation)
    :type args: collections.abc.Sequence[str] or str or None
    :arg parser: 用于解析 ``args`` 的 :class:`argparse.ArgumentParser` 对象，一般使用默认值即可
       
       :class:`argparse.ArgumentParser` object to parse ``args``. Generally, using the default values is sufficient
    """
    namespace = parser.parse_args(args)
    try:
        event_type = getattr(utils, namespace.type)
    except AttributeError:
        raise ValueError(f'event type "{namespace.type}" not found')
    ...
