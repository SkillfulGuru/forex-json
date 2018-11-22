# -*- coding: utf-8 -*-
# this code finds lowest and highest opening price in the last 10 days
import datetime
import requests
from datetime import datetime, timedelta
import string


_myffurl = "https://mds-api.forexfactory.com/bars?interval=D1&instrument=EUR/USD&per_page=10"

_currency = input("Enter the currency conversion (leave blank for EUR/USD): ")

if len(_currency) > 0:
	_myffurl = _myffurl.replace('EUR/USD',_currency)
	

header = {'x-requested-with': 'XMLHttpRequest'}
# retrieve API data 
response = requests.get(_myffurl, headers=header)
jdata = response.json()
newdata = jdata['data']
# the 'data' elements

_highest_open = newdata[0]['open']
_lowest_open = newdata[0]['close']

for jd in newdata:
	if jd['open'] > _highest_open:
		_highest_open = jd['open']
	if jd['open'] < _lowest_open:
		_lowest_open = jd['open']
		
print ("{0} \n{1}".format("highest open price: %0.5f " % _highest_open, "lowest open price:  %.5f" % _lowest_open))

