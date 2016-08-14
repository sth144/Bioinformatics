from __future__ import division
import numpy as np

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

input = raw_input(
'''enter sequences of same length
separated by \',\' :'''
).upper()

tuples = []
l = input.split(', ')
s = len(l[0])
t = len(l)

for e in l:
	el = list(e)
	tuples.append(el)

print '\nSEQUENCE TUPLES:'
print tuples

print '\nSEQUENCE ARRAY:'
array = np.array(tuples)
print array

print '\nBASE DISTRIBUTION:'
print '         A T C G     Concensus'     
concensus = []
for i in range(0, s):
	a, t, c, g = 0, 0, 0, 0
	for vector in array:
		if vector[i] == 'A':
			a += 1
		elif vector[i] == 'T':
			t += 1
		elif vector[i] == 'C':
			c += 1
		else:
			g += 1
	x = {
	'A':a, 'T':t,
	'C':c, 'G':g
	}
	print 'p%d      ' % i, a, t, c, g, '\t', keywithmaxval(x)
	concensus.append(keywithmaxval(x))
	
print '\nCONCENSUS SEQUENCE:'
print ''.join(concensus)



	

	