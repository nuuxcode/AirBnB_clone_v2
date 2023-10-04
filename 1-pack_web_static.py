#!/usr/bin/python3
""" module doc
"""
from fabric.api import task, local
from datetime import datetime

@task
def do_pack():
    """ method doc
    """
    formatted_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    print(f"Packing web_static to versions/web_static_{formatted_dt}.tgz")
    local(f"mkdir -p versions && tar -cvzf versions/web_static_{formatted_dt}.tgz web_static")
