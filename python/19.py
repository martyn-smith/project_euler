# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 16:48:30 2014

@author: c1346299
"""
from datetime import date, timedelta
#date implements all the calendar generation.  This is easy...

def Euler_19():
	#verified
	trial_date = date(1901, 1, 1)	
	end_date = date(2001,1,1) #one extra to account for range()
	result = 0
	while (trial_date < end_date):
		if (trial_date.day == 1) and (trial_date.isoweekday() == 7):
			result += 1
		trial_date += timedelta(days=1)
			
	return result
			
print(Euler_19())
"""	
def generate_days(start_date, end_date):
	"""