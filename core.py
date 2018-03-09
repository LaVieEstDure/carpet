#!/usr/bin/python3
import click
from click import echo
from helpers import error, colour
import git
import os 
import sys
import config

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
@click.option("--executable", "-e", is_flag=True, help="Make executable project")
def new(name, executable):
    """
    Make a new project with accompaning virtual environment
    """
    current_dir = os.getcwd()
    new_dir = "{}/{}".format(current_dir, name)
    
    if os.path.exists(new_dir):
        error("Folder {} already exists!".format(name))
        sys.exit(1)
    
    os.mkdir(new_dir)
    os.mkdir(new_dir + "/.carpet/")
    os.chdir(new_dir)
    open("__init__.py", "a").close()
    open("Carpet.toml", "a").close()
    repo = git.Repo.init(path=new_dir)
    colour("BLUE", "Created new project!")
    
    config.build_default_config(new_dir, name=name)

@carpet.command(short_help="Run the program")
def run():
    """
    Run the project in the current directory
    """
    echo("IT WORKS")

if __name__ == "__main__":
    carpet()
