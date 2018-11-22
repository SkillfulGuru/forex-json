# -*- coding: utf-8 -*-
import datetime
import requests
from datetime import datetime, timedelta
import pytz
import tzlocal

_myffurl = "https://mds-api.forexfactory.com/bars?interval=M1&instrument=EUR/USD&per_page=50"
local_timezone = tzlocal.get_localzone()

#now = datetime.now()

local_tz = pytz.timezone("Pacific/Auckland")
header = {'x-requested-with': 'XMLHttpRequest'}
# retrieve API data 
response = requests.get(_myffurl, headers=header)
jdata = response.json()
newdata = jdata['data']
# the 'data' elements
i = 0
print "Date             Time     Open    High    Low     Close "
print "---------------------------------------------------------"  
for jd in newdata:
	# 'o' open, 'h' high, 'l' low, 'c' close
#	convertedtime = datetime.utcfromtimestamp('timestamp').strftime('%Y-%m-%d %H:%M:%S')
#	stamp = 'timestamp'
	_time = newdata[i]['timestamp']
	floattime = float(_time)
#	utc_now = pytz.utc.localize(datetime.utcfromtimestamp(floattime).strftime('%a %b %d, %Y %I:%M %p'))

#	inputTime = datetime.utcfromtimestamp(floattime)
#	inputTime = local_tz.localize(inputTime)
#	naive = pytz.timezone("Pacific/Auckland").localize(inputTime)
#	convTime = inputTime.astimezone(local_tz)
#	utc_now =  datetime.utcfromtimestamp(floattime).strftime('%a %b %d, %Y %I:%M %p')
#	pst_now = utc_now.astimezone(pytz.timezone("Pacific/Auckland"))
#	_newtime = convTime.strftime('%a %b %d, %Y %I:%M %p')

	_utctime = datetime.utcfromtimestamp(floattime)
	#.strftime('%a %b %d, %Y %H:%M')
#	print _utctime.hour
#	%H = %H + 1
	local_time = _utctime.replace(tzinfo=pytz.utc).astimezone(local_tz)
	local_time = local_time.strftime('%a %b %d, %Y %I:%M %p')
	_tt  =  local_time
	_open  = jd['open'] 
	_high  = jd['high'] 
	_low  = jd['low'] 
	_close  = jd['close'] 
	
	print("{0} {1} {2} {3} {4}".format("%s" % _tt, "%.5f" % _open, "%.5f" % _high, "%.5f" % _low, "%.5f" % _close))
	i = i + 1
	#print("")
	

