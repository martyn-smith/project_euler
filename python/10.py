"""
the sum of all primes up to two million.
"""
import primegen

def Euler_10():
	#verified
	primes = primegen.all_primes(2e+6)
	return sum(primes)

if __name__ == "__main__":
	print(Euler_10())
