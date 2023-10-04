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
    formatted_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = f"versions/web_static_{formatted_dt}.tgz"
    print(f"Packing web_static to versions/web_static_{formatted_dt}.tgz")
    local(f"{mkdir}&& tar -cvzf {path} web_static")


@task
def do_deploy(archive_path):
    """ method doc
        fab -f 2-do_deploy_web_static.py do_deploy:
        archive_path=versions/web_static_20231004201306.tgz
        -i ~/.ssh/id_rsa -u ubuntu
    """
    if os.path.exists(archive_path):
        fn_with_ext = os.path.basename(archive_path)
        fn_no_ext, ext = os.path.splitext(fn_with_ext)
        dpath = "/data/web_static/releases/"
        put_result = put(archive_path, "/tmp/")
        rm_result = run(f"rm -rf {dpath}{fn_no_ext}/")
        mkdir_result = run(f"mkdir -p {dpath}{fn_no_ext}/")
        tar_result = run(f"tar -xzf /tmp/{fn_with_ext} -C {dpath}{fn_no_ext}/")
        rm_tmp_result = run(f"rm /tmp/{fn_with_ext}")
        mv_result = run(f"mv {dpath}{fn_no_ext}/web_static/* {dpath}{fn_no_ext}/")
        rm_web_static_result = run(f"rm -rf {dpath}{fn_no_ext}/web_static")
        rm_current_result = run(f"rm -rf /data/web_static/current")
        ln_result = run(f"ln -s {dpath}{fn_no_ext}/ /data/web_static/current")
        if (
            put_result.failed or rm_result.failed or mkdir_result.failed or
            tar_result.failed or rm_tmp_result.failed or mv_result.failed or
            rm_web_static_result.failed or rm_current_result.failed or
            ln_result.failed
        ):
            return False
        else:
            return True
    else:
        return False
