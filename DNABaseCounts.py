from sys import argv
script, input = argv
dna = input

def count_letters(string):
	A, T, C, G, n  = 0, 0, 0, 0, 0
	for n in range(0, len(string) - 1):
		if string[n] == 'A':
			A += 1
		elif string[n] == 'T':
			T += 1
		elif string[n] == 'G':
			G +=1
		elif string[n] == 'C':
			C +=1
					
	return str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T) 

print count_letters(dna)