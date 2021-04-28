import argparse
from textwrap import dedent

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=('''
--------------------------------
example usage: python DesktopNotifier/app.py -t "Hello" -m "World"
--------------------------------
''')
)
parser.add_argument(
    '-t','--title',
    type=str, 
    help="echo the string you use here", 
    default="Hello World"
    )
parser.add_argument(
    '-m','--message',
    type=str,
    help="echo the string you use here",
    default="Default message")