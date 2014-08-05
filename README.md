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

```python
import pymaniadb

pymania = pymaniadb.pymaniadb(apiKey="example")
resultsArray = pymania.searchDB(queryStr="muse", itemtypeStr="album")
print(resultsArray)
```

install
===
python setup.py install
