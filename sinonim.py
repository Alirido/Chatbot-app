import json
# sumber thesaurus : https://theindonesianwriters.files.wordpress.com/2011/04/kamus-tesaurus_bahasa-indonesia.pdf

def load(filename):	
	with open(filename) as data_file:
		data = json.load(data_file)	

	return data

# load dictionary
mydict = load('dict.json')

def getSinonim(word):
	if word in mydict.keys():
		return mydict[word]['sinonim']
	else:
		return []



print (getSinonim('terhampir'))
