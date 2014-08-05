pymaniadb
===========

A python module for maniadb.com.

required
===
Python 3.x
lxml

etc
===
http://www.maniadb.com/api/

example
===

import pymaniadb 

if __name__ == "__main__":
	pymania = pymaniadb(apiKey="example")
	resultsArray = pymania.searchDB(queryStr="muse", itemtypeStr="album")
	print(resultsArray) // results in array[dicts, ...]