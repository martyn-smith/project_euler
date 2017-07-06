"""
Cracks a banking password from single samples, e.g.
"1st digit y, 3rd x" etc.  Known no more than 6 digits in pw.
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
	with open("../data/79.dat") as f:
		data = f.readlines()
		newdata = []
		for line in data:
			if not (line in newdata):
				newdata.append(line)

if __name__ == "__main__":
	print(Euler_79())
