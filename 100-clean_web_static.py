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
    try:
        number = int(number)
    except Exception:
        return False
    nb_of_arch = local('ls -ltr versions | wc -l', capture=True).stdout
    nb_of_arch = int(nb_of_arch) - 1
    if nb_of_arch <= 0 or nb_of_arch == 1:
        return True
    if number == 0 or number == 1:
        arch_to_rm = nb_of_arch - 1
    else:
        arch_to_rm = arch_to_rm - number
        if arch_to_rm <= 0:
            return True
    archives = local("ls -ltr versions | tail -n " + str(nb_of_arch) + "\
            | head -n \
            " + str(arch_to_rm) + "\
            | awk '{print $9}'", capture=True)
    archives_list = archives.rsplit('\n')
    if len(archives_list) >= 1:
        for arch in archives_list:
            if (arch != ''):
                local("rm versions/" + arch)
                run('rm -rf /data/web_static/releases/\
                    ' + arch.split('.')[0]) 
