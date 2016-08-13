# Compute and rank GC contents of FASTA sequences
from __future__ import division
import sys
from sys import argv
script, seq = argv
seq = str(seq)
seq = seq.upper()

class Content(object):
	
	def calc_gc(self, string):
		n = 0
		for char in string:
			if char == 'G':
				n += 1
			elif char == 'C':
				n += 1
			else:
				pass
		return float(n) / float(len(seq))
		
x = Content()
print x.calc_gc(seq)
		