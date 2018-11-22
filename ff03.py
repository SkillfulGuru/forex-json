# -*- coding: utf-8 -*-
import datetime
import requests
from datetime import datetime
_myffurl = "https://mds-api.forexfactory.com/bars?interval=M1&instrument=EUR/USD&per_page=50"

now = datetime.now()
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")

header = {'x-requested-with': 'XMLHttpRequest'}
# retrieve API data 
response = requests.get(_myffurl, headers=header)
jdata = response.json()
newdata = jdata['data']
# the 'data' elements
i = 0
print ("{0} {1} {2} {3} {4} {5}".format("Date            " , "Time    ", "Open   ", "High   ", "Low   ", "Close "))  
for jd in newdata:
	# 'o' open, 'h' high, 'l' low, 'c' close
#	convertedtime = datetime.utcfromtimestamp('timestamp').strftime('%Y-%m-%d %H:%M:%S')
#	stamp = 'timestamp'
	_time = newdata[i]['timestamp']
	floattime = float(_time)
	_tt  =  datetime.utcfromtimestamp(floattime).strftime('%a %b %d, %Y %H:%M')
	_open  = jd['open'] 
	_high  = jd['high'] 
	_low  = jd['low'] 
	_close  = jd['close'] 
	
	print("{0} {1} {2} {3} {4}".format("%s" % _tt, "%.5f" % _open, "%.5f" % _high, "%.5f" % _low, "%.5f" % _close))
	i = i + 1
	#print("")
	

