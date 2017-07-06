"""
Created on Tue Aug 12 22:24:58 2014

author: martyn
"""

def smartsum(data):
	#apparently we only have to find the total, not the path
	"""
	this algorithm will look at each number on each row,
	and add to it the maximum of the - up to - two numbers
	above that could be reached by adjacent path.
	The end result is a row of numbers at the bottom,
	with the maximum being the result.

	So for:
	3
	7 4
	2 4 6
	8 5 9 3

	we have:
	3
	10 7
	12 14 13
	20 19 23 16
	"""
	prev_row = [0]
	#rowcount = 0
	for row in data:
		#rowcount += 1
		for i in range(0, len(row)):
			#print i, row[i], prev_row
			if (i==0):
				row[i] += prev_row[i]
			elif (i==len(row)-1):
				row[i] += prev_row[i-1]
			else:
				row[i] += max(prev_row[i], prev_row[i-1])
		prev_row = row
		#print data[i]
		#data[i][j] += max(data[i-1][j-1], data[i][j-1])
	return max(row)
