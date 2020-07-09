#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pydev")


name = "dns_naptr_query"
default_task = "publish"


@init
def initialize(project):
    project.build_depends_on("dnspython")
    project.version = "0.1.20200709"
    project.set_property('logging_steam', 'sys.stderr')    
    project.set_property('logging_level', 'DEBUG')    
    pass
