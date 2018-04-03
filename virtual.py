"""
Main project management file for carpet
"""
import os
import sys
import shutil
import subprocess
from helpers import error, colour
import virtualenv
import git
import config

def create_project(location, name,  executable=False):
    """
    Creates a project folder given a env new_dir
    """
    new_dir = "{}/{}".format(location, name)
    
    if os.path.exists(new_dir):
        error("Folder {} already exists!".format(name))
        sys.exit(1)
    # Make boilerplate files
    try:
        os.mkdir(new_dir)
        os.mkdir(new_dir + "/.carpet/")
        os.chdir(new_dir)
        open("__init__.py", "a").close()
        open("Carpet.toml", "a").close()
        _repo = git.Repo.init(path=new_dir)
        config.build_default_config(new_dir, name=name)
        
        # If the project is meant to be executable,
        # add a __main__.py 
        if executable:
            main = open("__main__.py", "a")
            main.write("print('Hello World')")
            main.close()
        else:
            config.set_config(new_dir, "package/executable", False)
        
        virtualenv.create_environment(new_dir + "/.carpet/env")
    except Exception as e:
        shutil.rmtree(new_dir)
        colour("FAIL", "Failed to create project")
        echo("Have you checked your permissions?")

    colour("BLUE", "Created new project!")

def run_project(location):
    if os.name == "nt":
        raise NotImplementedError
    if not os.path.isfile("Carpet.toml"):
        colour("FAIL", "Not in a Carpet project directory!")
        sys.exit(1)
    pyloc = location + "/.carpet/env/bin/python"
    subprocess.Popen([pyloc, location + "/__main__.py"], 
                     shell=True, 
                     stdin=subprocess.PIPE)
