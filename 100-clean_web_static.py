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
    if number == 0 or number == 1:
        with lcd('./versions/'):
            local("ls -lv | rev | cut -f 1 | rev | \
            head -n +1 | xargs -d '\n' rm -rf")
        with cd('/data/web_static/releases/'):
            run("sudo ls -lv | rev | cut -f 1 | \
            rev | head -n +1 | xargs -d '\n' rm -rf")
    else:
        with lcd('./versions/'):
            local("ls -lv | rev | cut -f 1 | rev | \
            head -n +{} | xargs -d '\n' rm -rf".format(number))
        with cd('/data/web_static/releases/'):
            run("sudo ls -lv | rev | cut -f 1 | \
            rev | head -n +{} | xargs -d '\n' rm -rf".format(number))
