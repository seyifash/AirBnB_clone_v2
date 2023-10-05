#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    generates a .tgz archive from the contents of webstatic
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions//web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
		.format(file_name))
