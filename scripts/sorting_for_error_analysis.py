
import json
import re
import glob

file = 'data/input_for_reliabiliy/11.json'

text = json.load(open(file, 'r'))

def filter_agreements(anno: list):
	
	disagreed = []
	agreed = []
	for sent in text:
		disagree = False
		for t in sent:
			if t['token1'] == t['token2']:
				if t['tag1'] != t['tag2']:
					print(t['tag1'], t['tag2'])
					disagree = True
		if disagree:
			disagreed.append(sent)
		else:
			agreed.append(sent)
	return (disagreed, agreed)

def writebysent(sent: list, outfile: str, outdir: str):
	with open(outdir + outfile + ".txt", 'a') as outf:
		outf.write("#New sent below\n")
		for token in sent:
			outf.write("\t".join([token['token1'], token['token2'], token['tag1'], token['tag2']]))
			outf.write("\n")
		outf.write("\n\n")


files = glob.glob('data/input_for_reliabiliy/*.json')

for file in files:
	text = json.load(open(file, 'r'))
	dagr, agr = filter_agreements(text)
	
	for sent in dagr:
		label_pair = []

		for t in sent:
			
			if t['token1'] == t['token2']:
				if t['tag1'] != t['tag2']:
					label_pair.append("{}-{}".format(t['tag1'], t['tag2']))

		if len(label_pair) > 0:
			for pair in label_pair:
				writebysent(sent, pair, 'data/disagreed_sentences/')
	