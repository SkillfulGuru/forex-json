# -*- coding: utf-8 -*-
#this code displays data in a table
import datetime
import requests
from datetime import datetime, timedelta
import string


_myffurl = "https://mds-api.forexfactory.com/bars?interval=H1&instrument=EUR/USD&per_page=20"
#local_timezone = tzlocal.get_localzone()

_currency = input("Enter the currency conversion (leave blank for EUR/USD): ")
_interval = input("Enter the interval (M1, M5, H1, H4, D1, MN1) (leave blank for 1 hour): ")
_results = input("Enter number of results (leave blank for 20): ")
if len(_currency) > 0:
	_myffurl = _myffurl.replace('EUR/USD',_currency)

#_myffurl.replace('H4','H1')
if len(_interval) > 0:
	_myffurl = _myffurl.replace('H1',_interval)

#now = datetime.now()

if len(_results) > 0:
	_myffurl = _myffurl.replace('20',_results)

print ("")	
#local_tz = pytz.timezone("Pacific/Auckland")
header = {'x-requested-with': 'XMLHttpRequest'}
# retrieve API data 
response = requests.get(_myffurl, headers=header)
jdata = response.json()
newdata = jdata['data']
# the 'data' elements
#i = 0
print ("Date             Time     Open    High    Low     Close ")
print ("---------------------------------------------------------")  
for jd in newdata:

	_time = jd['timestamp']
#	floattime = float(_time)

	_utctime = datetime.utcfromtimestamp(_time)
	_gmttime = _utctime + timedelta(hours=13)
#	local_time = _utctime.replace(tzinfo=pytz.utc).astimezone(local_tz)
#	_gmttime = _gmttime.isoformat()
	local_time = _gmttime.strftime('%a %b %d, %Y %I:%M %p')

	_tt  =  local_time
	_open  = jd['open'] 
	_high  = jd['high'] 
	_low  = jd['low'] 
	_close  = jd['close'] 
	
	print("{0} {1} {2} {3} {4}".format("%s" % _tt, "%.5f" % _open, "%.5f" % _high, "%.5f" % _low, "%.5f" % _close))
#	i = i + 1

	

