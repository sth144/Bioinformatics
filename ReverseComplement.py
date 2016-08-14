# Reverse Complement
import sys
from sys import argv
script, seq = argv

seq = str(seq)

class rComp(object):
	
	def __init__(self, string):
		self.string = string
		string = string[::-1].upper()
		pairs = {
			'A':'T', 'T':'A',
			'G':'C', 'C':'G'
		}
		l = list(string)
		n = []
		for char in l:
			n.append(pairs[char])
		print ''.join(n)
		
rComp(seq)

