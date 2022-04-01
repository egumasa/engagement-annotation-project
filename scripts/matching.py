
import re
import csv
import json



file1 = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/Annotated_files_ME/training_15.tsv"
file2 = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/Annotated_files_ALM/training_15_ALM.tsv"

conll1 = open(file1, 'r').read()
conll2 = open(file2, 'r').read()

def conll2list(conllfile):
	holder = []
	for chunk in conllfile.split('\n\n'):
		temp = []
		for line in chunk.split("\n"):
			if len(line) < 1:
				continue
			elif "#" in line[0]:
				#print(line)
				pass
			else:
				temp.append(line)
		holder.append(temp)
	return holder

list1 = conll2list(conll1)
list2 = conll2list(conll2)

def clean_tag(label: str) -> str:
	'''This function cleans the token labels.
	'''
	pat = r"(.*)\[\d+\]"
	match = re.match(pat, label)
	if match:
		#print(label)
		newlabel = match.group(1)
		#print(newlabel)
	else:
		newlabel = label
	return newlabel

def list2alignedtokens(list1, list2):
	sent = []
	for sent1,sent2 in zip(list1[1:],list2[1:]):
		tokens = []
		if len(sent1) == len(sent2):
			for t1, t2 in zip(sent1, sent2):
				tid, charid, token1, e, tag1 = t1.strip().split("\t")
				tid, charid, token2, e, tag2 = t2.strip().split('\t')
				tag1 = clean_tag(tag1)
				tag2 = clean_tag(tag2)
				line = {'token1': token1,
						'token2': token2,
						'tag1': tag1,
						'tag2': tag2}
				tokens.append(line)
				#print(line)
		else:
			for t1, t2 in zip(sent1, sent2):
				print(t1, t2)
		sent.append(tokens)
	return sent

for fileno in range(11,27):
	file1 = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/Annotated_files_ME/training_{}.tsv".format(fileno)
	file2 = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/Annotated_files_ALM/training_{}_ALM.tsv".format(fileno)
	conll1 = open(file1, 'r').read()
	conll2 = open(file2, 'r').read()
	list1 = conll2list(conll1)
	list2 = conll2list(conll2)
	aln_list = list2alignedtokens(list1, list2)
	with open("/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/input_for_reliabiliy/{}.json".format(fileno), 'w') as f:
		json.dump(aln_list, f)

for line in conll2.split('\n'):
	if len(line) < 1:
		continue
	elif "#" in line[0]:
		#print(line)
		pass
	else:
		print(line)
