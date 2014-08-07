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

result
===
```python
searchDB('esti', 'artist')
[{'demographic': '남성솔로', 'link': 'http://www.maniadb.com/artist/404965', 'pubDate': 'Tue, 10 Jan 2012 18:51:23 +0900', 'title': 'ESTi', '{http://www.maniadb.com/api}majormembers': None, 'id': '404965', 'period': '1990s - ', '{http://www.maniadb.com/api}majorsongs': '\t\t\n\t\t', '{http://www.maniadb.com/api}linkgallery': 'http://www.maniadb.com/artist/404965/?o=g', '{http://www.maniadb.com/api}majorsonglist': None, 'image': 'http://img.maniadb.com', '{http://www.maniadb.com/api}majoractivity': '\n\t\t\t\t\n\t\t', 'author': 'maniadb', '{http://www.maniadb.com/api}linkdiscography': 'http://www.maniadb.com/artist/404965/?o=l', 'reference': None, 'description': 'ESTi (본명 : 박진배, 1980년 5월 8일 ~) 는 대한민국의 작곡가이다. 1998년 창세기전 외전 서풍의 광시곡의 게임 음악으로 데뷔했으며, 라그나로크 온라인, 테일즈위버', 'comments': 'http://www.maniadb.com/artist/404965#TALK', '{http://www.maniadb.com/api}relatedartistlist': None, 'guid': 'http://www.maniadb.com/artist/404965'}]

getAlbumInfoFromID('404965')
[{'{http://www.maniadb.com/api}albumartists': '홍순관', 'image': 'http://img.maniadb.com/images/album/404/404965_1_f.jpg', '{http://www.maniadb.com/api}artist': '\n\t\t\t', 'link': 'http://www.maniadb.com/album/404965/?s=0', 'releasedate': '2010', 'thumnail': 'http://img.maniadb.com/images/album_t/150/404/404965_1_f.jpg', '{http://www.maniadb.com/api}products': '\n\t\t\t\t', 'id': '404965', 'title': '홍순관 - 홍순관이 부르는 찬송가 - 양떼를 떠나서 (2010)', '{http://www.maniadb.com/api}tracks': '\n\t\t\t', 'description': None}]
```

install
===
python setup.py install
