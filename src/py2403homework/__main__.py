import sys
import argparse
try:
    from . import _types
except ImportError:
    import _types


parser = argparse.ArgumentParser(
    # prog='python -m py2403homework',
    description = 'A tool to generate reST content for homework',
)
parser.add_argument('-t', '--type', default='Homework')

def run(args):
    namespace = parser.parse_args(args)
    try:
        event_type = getattr(_types, namespace.type)
    except AttributeError:
        raise ValueError(f'event type "{namespace.type}" not found')
    print(event_type())

if len(sys.argv) == 1:
    args = input('$ ').split()
    run(args)
else:
    run(sys.argv[1:])