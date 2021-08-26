#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder of the AirBnB Clone repo
"""
from fabric.operations import local
from datetime import datetime as d


def do_pack():
    """ generates a .tgz archive """
    name = "versions/web_static_" + str(d.now().year)
    name += str(d.now().month) + str(d.now().day) + str(d.now().hour)
    name += str(d.now().minute) + str(d.now().second) + ".tgz"
    result = local("mkdir -p versions; tar -cvzf \"%s\" web_static" % name)
    if result.failed:
        return None
    else:
        return name
