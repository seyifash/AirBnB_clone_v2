#!/usr/bin/python3
"""Fabfile to distribute an archive to a web server.
"""

from fabric.api import put, run, env
from os.path import exists
from datetime import datetime
from fabric.api import local
from os.path import isdir
env.hosts = ['54.160.106.104', '54.146.74.156']


def do_pack():
    """
    generates a .tgz archive from the contents of webstatic
    """
    the_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    local("mkdir -p versions")
    file_name = "versions/web_static_{}.tgz".format(the_time)
    arch_created = local("tar -cvzf {} web_static".format(file_name))
    if arch_created is not None:
        return file_name
    else:
        return None


def do_deploy(archive_path):
    """
    copies the archive files from my local machine to the servers
    """

    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}".format(file_name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))
        run("rm /tmp/{}.tgz".format(file_name))
        run("mv /data/web_static/releases/{}"
            "/web_static/* /data/web_static/releases/{}/"
            .format(file_name, file_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    deply = do_deploy(archive_path)
    if (deply is False):
        return False
    return deply
