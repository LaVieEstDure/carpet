#!/usr/bin/python3
import click
from click import echo
import virtual
import os


@click.group()
@click.pass_context
def carpet(command):
    """
    A cargo-like utility to manage virtual environments
    and dependencies in Python, in a natural and logical
    manner
    """
    pass


@carpet.command(short_help="Make a new project")
@click.argument("name")
@click.option("--executable", "-e", 
              is_flag=True, default=True,
              help="Make executable project")
def new(name, executable):
    """
    Make a new project with accompaning virtual environment
    """
    current_dir = os.getcwd()
    print("executable", executable)
    virtual.create_project(current_dir, name, executable)


@carpet.command(short_help="Run the program")
def run():
    """
    Run the project in the current directory
    """
    virtual.run_project(os.getcwd())

if __name__ == "__main__":
    carpet()
