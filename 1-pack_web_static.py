#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    generates a .tgz archive from the contents of webstatic
    """
    local("mkdir -p versions")
    the_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(the_time)
    arch_created = local("tar -cvzf {} web_static".format(file_name))
    if arch_created is not None:
        return file_name
    else:
        return None
