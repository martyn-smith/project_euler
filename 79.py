# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 21:11:18 2015

@author: martyn
"""

def Euler_79():
	"""
	This should be quite easy.
	Pattern xxxxxx
	Each sample could be yyyxxx, yxyyxx.. xxxyyy
	Backwards search:
	"""
	pass

def delete_duplicates():
	with open("../79.dat") as f:
		data = f.readlines()
		newdata = []
		for line in data:
			if not (line in newdata):
				newdata.append(line)