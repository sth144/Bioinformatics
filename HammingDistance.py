# Calculate the Hamming distance between two nucleotide sequences
import sys
from sys import argv
script, input1, input2 = argv

class Hamming(object):
	
	def hamming(self, seq1, seq2):
		score = 0
		if len(seq1) == len(seq2):
			for n in range (0, len(seq1)):
				if seq1[n] != seq2[n]:
					score += 1
			return score
		else:
			print "Make them the same length"		
	
Ham = Hamming()
print Ham.hamming(input1, input2)