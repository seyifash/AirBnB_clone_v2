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

    loc_d = 'versions/'
    rem_dir = '/data/web_static/relaeses/'
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]

    for item in archives:
        local('rm {}{}'.format(loc_d, item))
    archives = run("ls -tr {}".format(rem_dir)).split()
    archives = [a for a in archives if "web_static_" in a]
    [archives.pop() for i in range(number)]
    [run("rm -rf {}{}".format(rem_dir, a)) for a in archives]
