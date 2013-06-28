#!/usr/bin/env python 

#Title : pymaniadb
#Version : 0.1
#Author : Yi 'Pusungwi' Yeon Jae
#Description : a codes of pymaniadb

import urllib.request
import urllib.parse
import io
from lxml import etree

MANIADB_ROOT_URL = 'http://www.maniadb.com/api/'
MANIADB_SEARCH_URL = 'search.asp' #검색 asp 파일 정보

class pymaniadb:
	def __init__(self, apiKey, debug=False):
		#EloManager main class init method
		print("paymaniadb Init...")
		self.apiKey = apiKey

	def searchMusic(self, queryStr, itemtypeStr, targetStr='music', displayNum=10):
		SEARCH_PARAM = urllib.parse.urlencode({'key': self.apiKey, 'target': targetStr, 'itemtype':itemtypeStr, 'query':queryStr, 'display':displayNum},
			encoding='utf-8')
		resultDictsArray = []
	
		try:
			requestFullUrl = MANIADB_ROOT_URL + MANIADB_SEARCH_URL + '?' + SEARCH_PARAM
			recvSearchXml = urllib.request.urlopen(requestFullUrl)
		except IOError:
			print("URL address Error")
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
	pymania = pymaniadb(apiKey='[HERE IS API KEY]')
	resultsArray = pymania.searchMusic(queryStr="muse", itemtypeStr="artist")
	print(resultsArray)
