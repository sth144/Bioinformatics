# DNA transcriber

import sys
from sys import argv
script, input = argv

class Transcriber(object):

	def transcribe(self, DNA):
		DNA = DNA.replace('T', 'U')
		print DNA
		
t = Transcriber()
t.transcribe(input)