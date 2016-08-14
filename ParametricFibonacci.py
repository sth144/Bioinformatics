# Fibonacci sequence. Population after n generations with k offspring per litter
import sys
from sys import argv
script, n, k = argv
n, k = int(n), int(k)

class paramFibo(object):
	
	def population(self, t, m):
		if t < 2:
			return t
		else:
			return (
				self.population(t-1, m) +
				self.population(t-2, m) * m
			)
		
x = paramFibo()
print x.population(n, k)