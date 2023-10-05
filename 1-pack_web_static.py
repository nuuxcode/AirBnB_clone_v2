#!/usr/bin/python3
""" module doc
"""
from fabric.api import task, local
from datetime import datetime


@task
def do_pack():
    """ method doc
        sudo fab -f 1-pack_web_static.py do_pack
    """
    formatted_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(formatted_dt)
    print("Packing web_static to {}".format(path))
    if local("{} && tar -cvzf {} web_static".format(mkdir, path)).succeeded:
        return path
    return None
