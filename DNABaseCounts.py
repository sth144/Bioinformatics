from sys import argv
script, input = argv
dna = input

def count_letters(string):
	A = 0
	T = 0
	C = 0
	G = 0
	n = 0
	for n in range(0, len(string) - 1):
		if string[n] == 'A':
			A += 1
			#n += 1
		elif string[n] == 'T':
			T += 1
			#n += 1
		elif string[n] == 'G':
			G +=1
			#n +=1
		elif string[n] == 'C':
			C +=1
			#n +=1
		
	return str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T) 

print count_letters(dna)