#!/usr/bin/env python 

#Title : pymaniadb
#Version : 0.3
#Author : Yi 'Pusungwi' Yeon Jae
#Description : a codes of pymaniadb

import urllib.request
import urllib.parse
import io
from lxml import etree

MANIADB_ROOT_URL = 'http://www.maniadb.com/api/'
MANIADB_SEARCH_URL = 'search/' #검색 asp 파일 정보. example: http://www.maniadb.com/api/search/metallica/?sr=artist&display=10&key=example&v=0.5
MANIADB_ALBUM_URL = 'album/' # example: http://www.maniadb.com/api/album/712017/?key=example&v=0.5

class pymaniadb:
	def __init__(self, apiKey, debug=False):
		#EloManager main class init method
		if debug == True:
			print("paymaniadb Init...")

		self.debug = debug
		self.apiKey = apiKey

	def searchDB(self, queryStr, itemtypeStr, targetStr="artist", displayNum=10):
		SEARCH_PARAM = urllib.parse.urlencode({'key': self.apiKey, 'target': targetStr, 'itemtype':itemtypeStr, 'display':displayNum, 'v':'0.5'},
			encoding='utf-8')
		resultDictsArray = []
	
		try:
			requestFullUrl = MANIADB_ROOT_URL + MANIADB_SEARCH_URL + '/' + queryStr + '/?' + SEARCH_PARAM
			print(requestFullUrl)
			recvSearchXml = urllib.request.urlopen(requestFullUrl)
		except IOError:
			print("URL address or maniadb Error")
		else:
			parseEvents = ("start", "end")
			tParseXml = io.BytesIO(recvSearchXml.read())
			recvParsedXml = etree.iterparse(tParseXml, events=parseEvents)

			for action, elem in recvParsedXml:
				if action in ("start") and elem.tag == "item":
					tmpResultDict = {'id':elem.values()[0]}
					for subElem in elem.getchildren():
						tmpResultDict[subElem.tag] = subElem.text

					resultDictsArray.append(tmpResultDict)

		return resultDictsArray

	def getAlbumInfoFromID(self, idStr):
		SEARCH_PARAM = urllib.parse.urlencode({'v':'0.5'}, encoding='utf-8')
		resultDictsArray = []
	
		try:
			requestFullUrl = MANIADB_ROOT_URL + MANIADB_ALBUM_URL + '/' + idStr + '/?' + SEARCH_PARAM
			print(requestFullUrl)
			recvSearchXml = urllib.request.urlopen(requestFullUrl)
		except IOError:
			print("URL address or maniadb Error")
		else:
			parseEvents = ("start", "end")
			tParseXml = io.BytesIO(recvSearchXml.read())
			recvParsedXml = etree.iterparse(tParseXml, events=parseEvents)

			for action, elem in recvParsedXml:
				if action in ("start") and elem.tag == "item":
					tmpResultDict = {'id':elem.values()[0]}
					for subElem in elem.getchildren():
						tmpResultDict[subElem.tag] = subElem.text

					resultDictsArray.append(tmpResultDict)

		return resultDictsArray

if __name__ == "__main__":
	print('maniadb ver 0.3')
	pymania = pymaniadb(apiKey="example")

	print('searching keyword muse... (item type : album)')
	dbSearchArray = pymania.searchDB(queryStr="muse", itemtypeStr="album")
	print(dbSearchArray)
	
	print('search album id 712017...')
	albumSearchArray = pymania.getAlbumInfoFromID('712017')
	print(albumSearchArray)
