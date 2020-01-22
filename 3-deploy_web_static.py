#!/usr/bin/python3
import datetime
from fabric import operations
from fabric.api import env
from fabric.contrib import files
import os
"""Full Depoy modual"""
env.hosts = ['35.237.245.13', '35.243.169.209']


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
    return "versions/{}".format(name)


def do_deploy(archive_path):
    """this function deploys the archive to the server"""
    # check for path existance
    if not os.path.isfile(archive_path):
        return False

    # without the the parent dir and the extension
    mid = archive_path[9:-4]
    # print(mid)

    # /tmp/tempfile
    midend = archive_path[9:]
    tempfile = '/tmp/{}'.format(midend)
    # print("midend = " + midend, "new tempfile = " + tempfile)

    # /data/web_static/releases/mid
    dirname = '/data/web_static/releases/' + mid + '/'
    # print(dirname)
    try:
        # put achive path to tmp directory of webserver
        operations.put(archive_path, '/tmp/')

        # creating the directory for the archive
        operations.run('mkdir -p {}'.format(dirname))

        # run uncommpress the archive to the created directory
        operations.run('tar -xzf {} -C {}'.format(tempfile, dirname))

        # remove archive
        operations.run('rm {}'.format(tempfile))

        # delete symbolic link
        operations.run(
            'mv /data/web_static/releases/{0}/web_static/* \
                /data/web_static/releases/{0}/'.format(mid))
        operations.run(
            'rm -rf /data/web_static/releases/{}/web_static'.format(mid))
        operations.run('rm -rf /data/web_static/current')
        operations.run(
            'ln -s /data/web_static/releases/{}/ \
                /data/web_static/current'.format(mid))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """This function can fully deploy an archive"""
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
