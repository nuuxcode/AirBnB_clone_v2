#!/usr/bin/python3
""" module doc
"""
from fabric.api import task, local, env, put, run
from datetime import datetime
import os

env.hosts = ['18.207.1.87', '52.206.189.175']

@task
def do_pack():
    """ method doc
        sudo fab -f 1-pack_web_static.py do_pack
    """
    formatted_dt = f"$(date +%Y%m%d%H%M%S)"
    mkdir = "mkdir -p versions"
    path = f"versions/web_static_{formatted_dt}.tgz"
    print(f"Packing web_static to versions/web_static_{formatted_dt}.tgz")
    local(f"{mkdir}&& tar -cvzf {path} web_static")


@task
def do_deploy(archive_path):
    """ method doc
        sudo fab -f 1-pack_web_static.py do_pack
    """
    if os.path.exists(archive_path):
        fn_with_ext = os.path.basename(archive_path)
        fn_no_ext, ext = os.path.splitext(fn_with_ext)
        dpath = "/data/web_static/releases/"
        private_key = env.key_filename
        username = env.user
        put(archive_path, "/tmp/")
        run(f"mkdir -p {dpath}{fn_no_ext}/")
        run(f"tar -xzf /tmp/{fn_with_ext} -C {dpath}{fn_no_ext}/")
        run(f"rm /tmp/{fn_with_ext}")
        run(f"mv {dpath}{fn_no_ext}/web_static/* {dpath}{fn_no_ext}/")
        run(f"rm -rf {dpath}{fn_no_ext}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {dpath}{fn_no_ext}/ /data/web_static/current")
        print("New version deployed!")
        return True
    else:
        return False
