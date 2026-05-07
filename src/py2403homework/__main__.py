import sys
try:
    from .commands import run
except ImportError:
    from commands import run

if __name__ == '__main__':
    if len(sys.argv) == 1:
        args = input('$ ').split()
        run(args)
    else:
        run(sys.argv[1:])