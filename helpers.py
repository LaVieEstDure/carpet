import click
from click import echo

colours = {
    "HEADER" : '\033[95m',
    "BLUE" : '\033[94m',
    "GREEN" : '\033[92m',
    "WARNING" : '\033[93m',
    "FAIL" : '\033[91m',
    "ENDL" : '\033[0m',
    "BOLD" : '\033[1m',
    "UNDERLINE" : '\033[4m'
}

def error(text):
    echo(colours["FAIL"] + "\nERROR:\n" + colours["ENDL"])
    echo(text)

def colour(col, text):
    echo(colours[col] + text + colours["ENDL"])
