# locate input motif in input sequence 
import re
from re import finditer
import sys
from sys import argv
script, motif, seq = argv
seq, motif = str(seq), str(motif)
for m in re.finditer(motif, seq):
	print 'motif located', m.start(), '-', m.end()