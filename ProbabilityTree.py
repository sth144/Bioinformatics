# Given: Three positive integers k, m, and n, representing 
# a population containing k + m + n organisms: k individuals
# are homozygous dominant for a factor, m are heterozygous, 
# and n are homozygous recessive.

# Return: The probability that two randomly selected mating 
# organisms will produce an individual possessing a dominant
# allele (and thus displaying the dominant phenotype). Assume 
# that any two organisms can mate.

import sys
from sys import argv
script, k, m, n = argv

k, m, n = float(k), float(m), float(n)

def Pdom(a, b, c):
	pop = k + m + n
	prob = (k / pop) + (m / (2 * pop))
	return prob
	
print Pdom(k, m, n)