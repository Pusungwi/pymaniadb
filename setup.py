#!/usr/bin/env python

from distutils.core import setup

import os

def get_build():
	path = "./.build"
	
	if os.path.exists(path):
		fp = open(path, "r")
		build = eval(fp.read())
		if os.path.exists("./.increase_build"):
			build += 1
		fp.close()
	else:
		build = 1
	
	fp = open(path, "w")
	fp.write(str(build))
	fp.close()
	
	return str(build)

setup(name = "pymaniadb",
      version = "0.1." + get_build(),
      author = "Yi Yeon Jae <pusungwi@gmail.com>",
	  description = "A Python module for maniadb.com",
      author_email = "pusungwi@gmail.com",
      url = "http://github.com/pusungwi/pymaniadb/",
      py_modules = ("pymaniadb",),
	  license = "bsd"
	)
