"""
returns the product of three numbers a,b,c of sum 1000 that satisfy
the equality a^2 = b^2 + c^2.

I forget what's impressive about that...
"""

def Euler_9():
	#verified
	#and weirdly easy
	for a in range(1, 1000):
		for b in range(1, 1000-a):
			c = (1000 - (a + b))
			if ((a**2) == (b**2) + (c**2)):
				return (a*b*c)

if __name__ == "__main__":
	print(Euler_9())
