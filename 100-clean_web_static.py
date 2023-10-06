#!/usr/bin/python3
"""Fabfile to delete out of date archives.
"""
import os
from fabric.api import *
env.hosts = ['54.160.106.104', '54.146.74.156']


def do_clean(number=0):
    """
    Keep it cleanning the repositories
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    if len(archives) > number:
        [archives.pop() for i in range(number)]
        with lcd("versions"):
            [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        if len(archives) > number:
            [archives.pop() for i in range(number)]
            [run("rm -rf ./{}".format(a)) for a in archives]
