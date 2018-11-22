# -*- coding: utf-8 -*-
import datetime
import requests

_myffurl = "https://mds-api.forexfactory.com/bars?interval=H1&instrument=EUR/USD&per_page=10"

header = {'x-requested-with': 'XMLHttpRequest'}
# retrieve API data 
response = requests.get(_myffurl, headers=header)
jdata = response.json()

# the 'data' elements  
for jd in jdata['data']:
	# 'o' open, 'h' high, 'l' low, 'c' close
	_tt  = jd['timestamp'] 
	_open  = jd['open'] 
	_high  = jd['high'] 
	_low  = jd['low'] 
	_close  = jd['close'] 
	
	print("{0} {1} {2} {3} {4}".format(_tt, "%.5f" % _open, "%.5f" % _high, "%.5f" % _low, "%.5f" % _close))
	#print("")
	

