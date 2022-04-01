

import csv
import glob
import re
import json

sample = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/conllu/MICUSP_4.xml.tsv"

holder = []

def return_match(idx, dir_list):
	for file in dir_list:
		with open(file, 'r') as f:
			text = f.read()
			chunk = text.split("\n\n")
			print(chunk)
			for sent in chunk:
				if idx in sent:
					return sent


def make_batch_list(sent_list: list, batch_size: int = 20):
	""" Returns two-level nested list, each for a batch of filenames.
	
	Parameters
	----------
	filenames : list
		The entire text filenames.
	batch_size : int, optional
		The number of documents for each batch. The default is 20

	Returns
	-------
	nested list of filenames.

	"""
	batches = []
	batch_count = 1
	current_batch = []
	for x, sent in enumerate(sent_list, start=1):
		if batch_count < batch_size:
			current_batch.append(sent)
			batch_count += 1
			print(x)
		else:
			current_batch.append(sent)
			batches.append(current_batch)
			print(x)
			batch_count = 1
			current_batch = []
			print('Reset')
	if len(current_batch) > 0:
		batches.append(current_batch) #this is the leftovers
	return (batches)


jn_file = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/3_training_data2/shuffled_ICNALE_MICUSP.json"

with open(jn_file, 'r') as jsn:
    shuffled_order = json.load(jsn)

filenames = glob.glob("/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/conllu/*.tsv")

reordered_conll = []
for idx, sent in shuffled_order:
    reordered_conll.append(return_match(idx, filenames))


new_batch = make_batch_list(reordered_conll)

def output_txt(sent_list, name, saving_dir, batch: int = 20):
	with open(saving_dir + name + ".txt", "w") as outf:
		#tsv_writer = csv.writer(outf, delimiter = "\t")
		for sent in sent_list:
			#print(sent)
			outf.write(sent)
			outf.write("\n\n")


for id, batch in enumerate(new_batch, start = 1):
	
	output_txt(batch, "training_{}".format(id), "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/reordered_conll/")