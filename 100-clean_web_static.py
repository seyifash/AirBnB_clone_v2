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
    files = local("ls versions", capture=True)
    file_names = files.split(" ")
    n = int(number)
    if n in (0, 1):
        n = 1
    else:
        n = len(file_names) - n
    for i in file_names[n:]:
        local("rm versions/{}".format(i))
    dir_server = run("ls /data/web_static/releases")
    dir_server_names = dir_server.split(" ")
    for i in dir_server_names[n:]:
        if i is 'test':
            continue
        run("rm -rf /data/web_static/releases/{}"
            .format(i))
