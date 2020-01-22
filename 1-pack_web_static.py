#!/usr/bin/python3
import datetime
from fabric import operations
from fabric.contrib import files
import os
"""this function creates an archive"""


def do_pack():
    """this function creates archives"""
    t = datetime.datetime.now()
    name = "web_static_{}{}{}{}{}{}.tgz".format(
        t.year,
        t.month,
        t.day,
        t.hour,
        t.minute,
        t.second
        )
    print(name)
    if not os.path.isdir('./versions'):
        operations.local("mkdir versions")

    try:
        operations.local("tar -cvzf versions/{} web_static".format(name))
    except Exception:
        return None
    return "versions/{}".format("name")
