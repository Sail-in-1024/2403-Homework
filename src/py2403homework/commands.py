"""
面向行，解析和运行命令。

Orienting towards rows, parse and run commands.
"""

import argparse
try:
    from . import utils
except ImportError:
    import utils


parser = argparse.ArgumentParser(
    # prog='python -m py2403homework',
    description = 'A tool to generate reST content for homework',
)
parser.add_argument('-t', '--type', default='Homework')

def run(args, parser: argparse.ArgumentParser=parser):
    """
    运行指定的命令。
    
    Run specified command.
    """
    namespace = parser.parse_args(args)
    try:
        event_type = getattr(utils, namespace.type)
    except AttributeError:
        raise ValueError(f'event type "{namespace.type}" not found')
    print(event_type())