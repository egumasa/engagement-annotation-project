#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 13:42:54 2021

@author: masakieguchi

This is based on Kris's code on accuracy calculator
"""

import json
import pprint as pp
import csv
import glob
import re


# =============================================================================
#  Accurary functions here
# =============================================================================
def simple_acc(extracted_data: dict) -> dict:
    '''Return simple parcentage accuracy figure yes/no match
	
	Parameters
	----------
	extracted_data : dict
		NEsted dict
		{id: {"gold": value, 'tag2': value}}

	Returns
	-------
	dict
		accuracy
				{'k': 0,
			  'correct': 0,
			  'incorrect': 0,
			  'accuracy': 0}.

	'''

    holder = {'k': 0, 'correct': 0, 'incorrect': 0, 'accuracy': 0}

    for idx, item in extracted_data.items():
        if item["tag1"] == item['tag2']:
            holder['correct'] += 1
            holder['k'] += 1

        else:
            holder['incorrect'] += 1
            holder['k'] += 1

    holder['accuracy'] = holder['correct'] / holder['k']

    return (holder)


def possible_tags(
    dataset
):  #create preliminary accuracy dictionary (used in tag_prec_rec_doc() below)
    acc_dict = {}
    for row, data in dataset.items():
        #print(data['tag1'])
        if data["tag1"] not in acc_dict:
            acc_dict[str(data["tag1"])] = {"TP": 0, "FP": 0, "FN": 0}
        if data["tag2"] not in acc_dict:
            acc_dict[str(data["tag2"])] = {"TP": 0, "FP": 0, "FN": 0}

    return (acc_dict)


#code for compilation of true positives, false positives, and false negatives for each tag
def tag_prec_rec_sent(data, acc_dict):

    for idx, item in data.items():
        if str(item["tag1"]) == str(item['tag2']):
            acc_dict[str(item["tag1"])]["TP"] += 1
        else:
            acc_dict[str(item["tag1"])]["FN"] += 1
            acc_dict[str(item['tag2'])]["FP"] += 1


#code for precision, recall, and F1 formulas
def prec_rec(accuracy_dict):
    accuracy_dict["TC"] = accuracy_dict["TP"] + accuracy_dict["FN"]
    if accuracy_dict["TP"] + accuracy_dict["FN"] == 0:
        accuracy_dict["recall"] = 0
    else:
        accuracy_dict["recall"] = accuracy_dict["TP"] / (accuracy_dict["TP"] +
                                                         accuracy_dict["FN"])

    if accuracy_dict["TP"] + accuracy_dict["FP"] == 0:
        accuracy_dict["precision"] = 0
    else:
        accuracy_dict["precision"] = accuracy_dict["TP"] / (
            accuracy_dict["TP"] + accuracy_dict["FP"])
    if accuracy_dict["precision"] == 0 and accuracy_dict["recall"] == 0:
        accuracy_dict["f1"] = 0
    else:
        accuracy_dict["f1"] = 2 * (
            (accuracy_dict["precision"] * accuracy_dict["recall"]) /
            (accuracy_dict["precision"] + accuracy_dict["recall"]))


def calc_recall_prec_f1(extracted_data: dict):

    acc_dict = possible_tags(extracted_data)

    tag_prec_rec_sent(extracted_data, acc_dict)

    for x in acc_dict:
        prec_rec(acc_dict[x])

    return acc_dict


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


def list2dict(input: list):
    holder = {}
    for sentid, sent in enumerate(input):
        for tid, token in enumerate(sent):
            #clean the tag here
            tag1 = clean_tag(token['tag1'])
            tag2 = clean_tag(token['tag2'])
            cleaned_token = {
                "tid": token['tid'],
                "token1": token['token1'],
                "token2": token['token2'],
                "tag1": tag1,
                "tag2": tag2
            }
            holder["{}-{}".format(sentid, tid)] = cleaned_token
    return holder


with open(
        "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/input_for_reliabiliy/batch1_A0_test.json",
        'r') as f:
    temp = json.load(f)

for l in temp:
    print(l)


def reduce_entry(anno: list):
    '''
      {
    "chunkid": 1,
    "sentid": "0413d.xml_s1.5;p4.47",
    "text": "It is important to mention here that I am using the Gramscian idea of hegemony in this paper.",
    "lines": [{},

    '''
    reduced = []

    for sent in anno:
        s_anno = []
        id_pairs = {}
        for l in sent['lines']:  #sent is a dictionary
            id_pair = "{}-{}".format(l['id1'], l['id2'])

            if l['tag1'] == "_" and l['tag2'] == "_":
                continue  #
            elif id_pair == "-":
                s_anno.append(l)
            elif id_pair not in id_pairs:
                s_anno.append(l)
                id_pairs[id_pair] = 1
                # print("FIRST pair: {}".format(str(l)))
            else:
                id_pairs[id_pair] += 1
                # print("\t|-: {}".format(str(l)))
        # print("\n")
        reduced.append(s_anno)
    return reduced


inputfiles = glob.glob(
    "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/input_for_reliabiliy/Aaron_completed_As/batch1_*.json"
)

holder = []
for file in inputfiles:

    with open(file, 'r') as f:
        lst = reduce_entry(json.load(f))

        holder.extend(lst)

temp_dict = list2dict(holder)
simple_acc(temp_dict)
pp.pprint(calc_recall_prec_f1(temp_dict))

with open(
        "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/data_for_reliability_20220524.json",
        'w') as f:
    json.dump(temp_dict, f, indent=2)

for file in inputfiles:
    with open(file, 'r') as f:
        lst = reduce_entry(json.load(f))
        temp_dict = list2dict(lst)
        with open(
                "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/data_for_reliability_{}.json"
                .format(file.split("/")[-1]), 'w') as f:
            json.dump(temp_dict, f, indent=2)

        simple_acc(temp_dict)
        pp.pprint(calc_recall_prec_f1(temp_dict))

# inputfiles = glob.glob("/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/input_for_reliabiliy/*.json")
# len(inputfiles)
# holder = []
# for file in inputfiles:

#     with open(file, 'r') as f:
#         lst = json.load(f)
#         holder.extend(lst)

#         with open(file.replace("data/input_for_reliabiliy/", "data/manual_inspection/").replace(".json", '.tsv'), 'w') as outf:
#             for idx, sent in enumerate(lst, start = 1):
#                 outf.write("\n")

#                 for tid, token in enumerate(sent):
#                     #clean the tag here
#                     tag1 = clean_tag(token['tag1'])
#                     tag2 = clean_tag(token['tag2'])
#                     cleaned_token = {"token1": token['token1'],
#                         "token2": token['token2'],
#                         "tag1": tag1,
#                         "tag2": tag2}
#                     outf.write("\t".join([token['token1'], token['token1'], tag1, tag2]))
#                     outf.write("\n")

# temp_dict = list2dict(holder)
# simple_acc(temp_dict)
# pp.pprint(calc_recall_prec_f1(temp_dict))

# =============================================================================
# feature extraction
# =============================================================================


def feature_extract(dataset, feature, store_sent=False):
    result = {}
    for id, data in dataset.items():
        result[id] = {"tag1": [], "tag2": [], 'sent': ''}

        result[id]['tag1'] = data[feature]
        if data['results'] == None:
            result[id]['tag2'] = [""]
        else:
            result[id]['tag2'] = data['results']['theme'][feature]

        if store_sent:
            result[id]['sent'] = data["Sent"]

        if feature == 'text':  #normalize the texts for comparison

            if len(result[id]['tag2']) > 0:
                result[id]['tag2'] = " ".join(result[id]['tag2'])
            else:
                result[id]['tag2'] = ""

            result[id]['tag1'] = result[id]['tag1'].replace(",", "").strip()
            result[id]['tag2'] = result[id]['tag2'].replace(",", "").strip()

        if feature not in ["text", 'Interpersonal', "Textual"]:

            if result[id]['tag1'] == "0":
                result[id]['tag1'] = False
            elif result[id]['tag1'] == "1":
                result[id]['tag1'] = True

            if type(result[id]['tag2']) == list:
                result[id]['tag2'] = None

    return result


def fix_sub_type_tags(data):
    for idx, mainverb in data.items():
        try:
            theme_info = mainverb['results']['theme']
        except TypeError:
            continue
        for funct, role in zip(theme_info['functions'], theme_info['roles']):
            if theme_info['sub_type'] in [
                    'Equative', 'Predicated', 'Thematized comment'
            ]:
                continue
            elif funct in ["Topical", 'Interpersonal/Topical']:
                if role in [
                        "nsubjpass", 'nsubj', 'csubj', 'csubjpass', 'Equative'
                ]:
                    sub_type = "Subject"

                elif role in [
                        'ccomp', 'attr', 'parataxis', 'dobj', 'acomp', 'dative'
                ]:
                    sub_type = 'Complement'
                elif role in ['prep', 'advcl', 'advmod', 'mark', 'npadvmod']:
                    sub_type = 'Adjunct'

                elif role in ['expl']:
                    sub_type = 'Existential'
                elif role in ['ROOT']:
                    sub_type = 'Predicator'
                elif role in ["dep"]:
                    sub_type = 'Ambiguous'

                elif role in ['Equative']:
                    sub_type = 'Equative'
                elif role in ['predicated']:
                    sub_type = 'Predicated'

                theme_info['sub_type'] = sub_type


for idx, mainverb in data.items():
    try:
        functions = mainverb['results']['theme']['functions']
        mainverb['results']['theme']['Interpersonal'] = 0
        mainverb['results']['theme']['Textual'] = 0
    except TypeError:
        continue
    for funct in functions:
        if funct == 'Interpersonal':
            mainverb['results']['theme']['Interpersonal'] += 1
        if funct == 'Textual':
            mainverb['results']['theme']['Textual'] += 1

# =============================================================================
# Loading dataset
# =============================================================================
test_dir = 'test_parse/'

with open(test_dir + "1_accuracy_test_set_20210715.json", "r") as f:
    data = json.load(f)
fix_sub_type_tags(data)

pp.pprint(data, sort_dicts=False)

#manual examination yield 86.42% accuracy on theme boundary
text_acc = simple_acc(feature_extract(data, 'text', store_sent=True))

types = calc_recall_prec_f1(feature_extract(data, 'theme_type'))

sub_type = calc_recall_prec_f1(feature_extract(data, 'sub_type'))

sub_type = calc_recall_prec_f1(feature_extract(data, 'Interpersonal'))

mark = calc_recall_prec_f1(feature_extract(data, 'marked'))
mood = calc_recall_prec_f1(feature_extract(data, 'mood_type'))
equative = calc_recall_prec_f1(feature_extract(data, 'equative'))

text_comp = feature_extract(data, 'text', store_sent=True)
with open(test_dir + "1_Theme_text_testset_20210715.txt", "w") as outf:
    tsv_writer = csv.writer(outf, delimiter='\t')

    tsv_writer.writerow('id\ttag1\tPredicted\tSentence'.split("\t"))
    for idx, content in text_comp.items():
        tsv_writer.writerow([
            str(idx),
            str(content['tag1']),
            str(content['tag2']),
            str(content['sent'])
        ])

theme_type = feature_extract(data, 'theme_type', store_sent=True)
with open(test_dir + "1_Theme_type_testset_20210715.txt", "w") as outf:
    tsv_writer = csv.writer(outf, delimiter='\t')

    tsv_writer.writerow('id\ttag1\tPredicted\tSentence'.split("\t"))
    for idx, content in theme_type.items():
        tsv_writer.writerow([
            str(idx),
            str(content['tag1']),
            str(content['tag2']),
            str(content['sent'])
        ])

Interpersonal = feature_extract(data, 'Interpersonal', store_sent=True)
with open(test_dir + "1_Tnterpersonal_testset_20210715.txt", "w") as outf:
    tsv_writer = csv.writer(outf, delimiter='\t')

    tsv_writer.writerow('id\ttag1\tPredicted\tSentence'.split("\t"))
    for idx, content in Interpersonal.items():
        tsv_writer.writerow([
            str(idx),
            str(content['tag1']),
            str(content['tag2']),
            str(content['sent'])
        ])

Textual = feature_extract(data, 'Textual', store_sent=True)
with open(test_dir + "1_Textual_testset_20210715.txt", "w") as outf:
    tsv_writer = csv.writer(outf, delimiter='\t')

    tsv_writer.writerow('id\ttag1\tPredicted\tSentence'.split("\t"))
    for idx, content in Textual.items():
        tsv_writer.writerow([
            str(idx),
            str(content['tag1']),
            str(content['tag2']),
            str(content['sent'])
        ])

sub_types = feature_extract(data, 'sub_type', store_sent=True)
with open(test_dir + "1_sub_type_testset_20210715.txt", "w") as outf:
    tsv_writer = csv.writer(outf, delimiter='\t')

    tsv_writer.writerow('id\ttag1\tPredicted\tSentence'.split("\t"))
    for idx, content in sub_types.items():
        tsv_writer.writerow([
            str(idx),
            str(content['tag1']),
            str(content['tag2']),
            str(content['sent'])
        ])

examples

text_acc = simple_acc(feature_extract(examples, 'text', store_sent=True))

types = calc_recall_prec_f1(feature_extract(examples, 'theme_type'))

sub_type = calc_recall_prec_f1(feature_extract(examples, 'sub_type'))

sub_type = calc_recall_prec_f1(feature_extract(examples, 'Interpersonal'))

mark = calc_recall_prec_f1(feature_extract(examples, 'marked'))
mood = calc_recall_prec_f1(feature_extract(examples, 'mood_type'))
equative = calc_recall_prec_f1(feature_extract(examples, 'equative'))

text_acc = simple_acc(feature_extract(test_set, 'text', store_sent=True))

types = calc_recall_prec_f1(feature_extract(test_set, 'theme_type'))

sub_type = calc_recall_prec_f1(feature_extract(test_set, 'sub_type'))

mood = calc_recall_prec_f1(feature_extract(test_set, 'mood_type'))

# =============================================================================
#  Original code from Kris's tutorial
# =============================================================================


#code for precision, recall, and F1 formulas
def prec_rec(accuracy_dict):
    accuracy_dict["TC"] = accuracy_dict["TP"] + accuracy_dict["FN"]
    if accuracy_dict["TP"] + accuracy_dict["FN"] == 0:
        accuracy_dict["recall"] = 0
    else:
        accuracy_dict["recall"] = accuracy_dict["TP"] / (accuracy_dict["TP"] +
                                                         accuracy_dict["FN"])

    if accuracy_dict["TP"] + accuracy_dict["FP"] == 0:
        accuracy_dict["precision"] = 0
    else:
        accuracy_dict["precision"] = accuracy_dict["TP"] / (
            accuracy_dict["TP"] + accuracy_dict["FP"])
    if accuracy_dict["precision"] == 0 and accuracy_dict["recall"] == 0:
        accuracy_dict["f1"] = 0
    else:
        accuracy_dict["f1"] = 2 * (
            (accuracy_dict["precision"] * accuracy_dict["recall"]) /
            (accuracy_dict["precision"] + accuracy_dict["recall"]))


def possible_tags(
    dataset
):  #create preliminary accuracy dictionary (used in tag_prec_rec_doc() below)
    acc_dict = {}
    for sent in dataset:
        for token in sent:
            if token["pos"] not in acc_dict:
                acc_dict[token["pos"]] = {"TP": 0, "FP": 0, "FN": 0}
    return (acc_dict)


#code for compilation of true positives, false positives, and false negatives for each tag
def tag_prec_rec_sent(gold, tested, tag_d):
    for idx, item in enumerate(gold):
        if item["pos"] == tested[idx]["pos"]:
            tag_d[item["pos"]]["TP"] += 1
        else:
            tag_d[item["pos"]]["FN"] += 1
            tag_d[tested[idx]["pos"]]["FP"] += 1


#code to apply the above function to a full dataset
def tag_prec_rec_doc(gold, tested, feature_d, full_data):
    tag_d = possible_tags(full_data)

    for idx, item in enumerate(gold):
        tag_prec_rec_sent(item, tested[idx], tag_d)

    for x in tag_d:
        prec_rec(tag_d[x])

    return (tag_d)


#get detailed tag information for our model
tested_simple_4_pr = tag_prec_rec_doc(test_data, test_simple_4_tagged,
                                      top_featured_freq, full_data)

#sort the dictionary by tag frequency to make it easier to read:
from operator import *

simple_4_pr_sorted = sorted(tested_simple_4_pr.items(),
                            key=lambda x: getitem(x[1], 'TC'),
                            reverse=True)

#Check out precision and recall for the five most frequent tags
for x in simple_4_pr_sorted[:5]:
    print(x)

####

import glob

tagged_files = glob.glob(
    "1_corpora/1_reference/_extracted_brown//*.txt")  #get list of files
len(tagged_files)  #500 files

#divide into sentences
full_data = []
for x in tagged_files[1:10]:
    text = open(x).read().split("\n\n")  #split into sentences
    for sent in text:  #iterate through sentences
        items = []  #start sentence-level text
        for word in sent.split("\n"):  #iterate through words
            if " " not in word:
                continue
            if word == "":
                continue
            if word == '':  #skip extra spaces
                continue
            else:
                items.append({
                    "word": word.split(" ")[0],
                    "pos": word.split(" ")[1]
                })  #add dictionary representation of word and tag to list
        if len(items) == 0:
            continue
        full_data.append(items)

import random

random.seed(10)  #set seed so we get the same results each time

#number of sentences for training set:
print(len(full_data) * .67)  #34912.36
train_data = random.sample(full_data,
                           688)  #create training set with 67% of sentences

#then, we will put any sentences that are NOT in train_data in test_data (this loop will take a little while)
test_data = []
for x in full_data:
    if x not in train_data:
        test_data.append(x)

print(len(train_data))  #34912
print(len(test_data))  #17029


def freq_add(item, d):
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1


#iterate through sentences, get tabulate tags for each word
def tag_freq(data_set):
    freq = {}
    for sent in data_set:
        for item in sent:
            if item["word"] not in freq:
                freq[item["word"]] = {}
            freq_add(item["pos"], freq[item["word"]])

    return (freq)


#create frequency dictionary
word_tags = tag_freq(train_data)

#check
print(word_tags["the"])
print(word_tags["The"])
print(word_tags["run"])


def unambiguous_tags(freq_dict, prob_thresh=.98, occur_thresh=5):
    unam = {}  #for unambiguous word:tag pairs

    for x in freq_dict:  #iterate through words in dataset
        total = sum(freq_dict[x].values()
                    )  #get total word frequency (sum of all tag frequencies)
        if total < occur_thresh:
            continue
        for y in freq_dict[x]:
            if freq_dict[x][y] / total >= prob_thresh:
                unam[x] = y
    return (unam)


unambiguous = unambiguous_tags(word_tags)

# =============================================================================
# print(unambiguous["the"]) #DT
# print(unambiguous["The"]) #key error! not unambiguous (also tagged as NNP!)
# print(unambiguous["run"]) #key error! not unambiguous
#
# =============================================================================


def simple_model_1(sent_to_tag, unam_d):
    tagged = []
    for x in sent_to_tag:
        word = x["word"]
        if word in unam_d:  #if the word is unambiguous, assign the tag
            tagged.append({"word": word, "pos": unam_d[word]})
        else:  #else, assign tag as "none"
            tagged.append({"word": word, "pos": "none"})

    return (tagged)


def simple_model_1_doc(doc_to_tag, unam_d):
    tagged = []
    for sent in doc_to_tag:
        tagged.append(simple_model_1(sent, unam_d))

    return (tagged)


test_simple_1_tagged = simple_model_1_doc(
    test_data, unambiguous)  #tag test data with simple model
print(test_simple_1_tagged[0])  #check results


def accuracy_sent(gold, tested, acc_dict):
    for idx, item in enumerate(gold):
        if item["pos"] == tested[idx]["pos"]:
            acc_dict["correct"] += 1
        else:
            acc_dict["false"] += 1


def accuracy_doc(gold, tested):
    acc_dict = {"correct": 0, "false": 0}

    for idx, item in enumerate(gold):
        accuracy_sent(item, tested[idx], acc_dict)

    accuracy = acc_dict["correct"] / (acc_dict["correct"] + acc_dict["false"])
    acc_dict["acc"] = accuracy

    return (acc_dict)


tested_simple_1 = accuracy_doc(test_data, test_simple_1_tagged)
print(tested_simple_1)

import operator


def sort_tags(freq, only_top=True):
    sort_freq = {}
    for x in freq:  #iterate through dictionary
        if only_top == True:
            sort_freq[x] = sorted(freq[x].items(),
                                  key=operator.itemgetter(1),
                                  reverse=True)[0][0]  #get most frequent tag
        else:
            sort_freq[x] = sorted(
                freq[x].items(), key=operator.itemgetter(1),
                reverse=True)  #so we can see all tags if we want

    return (sort_freq)


top_hits = sort_tags(word_tags)  #get dictionary of word:top_tag pairs

print(word_tags["run"])  #all hits
print(top_hits["run"])  #top hit


def simple_model_2(sent_to_tag, unam_d, known_d):
    tagged = []
    for x in sent_to_tag:
        word = x["word"]
        if word in unam_d:  #if the word is unambiguous, assign the tag
            tagged.append({"word": word, "pos": unam_d[word]})
        #this is new in model 2:
        elif word in known_d:
            tagged.append({"word": word, "pos": known_d[word]})
        else:  #else, assign tag as "none"
            tagged.append({"word": word, "pos": "none"})

    return (tagged)


def simple_model_2_doc(doc_to_tag, unam_d, known_d):
    tagged = []
    for sent in doc_to_tag:
        tagged.append(simple_model_2(sent, unam_d, known_d))

    return (tagged)


test_simple_2_tagged = simple_model_2_doc(test_data, unambiguous, top_hits)
print(test_simple_2_tagged[0])

tested_simple_2 = accuracy_doc(test_data, test_simple_2_tagged)
print(tested_simple_2)


def item_freq(data_set, item_name):
    freq = {}
    for sent in data_set:
        for item in sent:
            freq_add(item[item_name], freq)
    return (freq)


pos_freq = item_freq(train_data, "pos")  #get frequency of tags

pos_freq_sort = sorted(pos_freq.items(),
                       key=operator.itemgetter(1),
                       reverse=True)  #sort tags

print(pos_freq_sort[:10])  #most frequent is NN


def simple_model_3(sent_to_tag, unam_d, known_d, unknown_tag):
    tagged = []
    for x in sent_to_tag:
        word = x["word"]
        if word in unam_d:  #if the word is unambiguous, assign the tag
            tagged.append({"word": word, "pos": unam_d[word]})
        #this is new in model 2:
        elif word in known_d:
            tagged.append({"word": word, "pos": known_d[word]})
        else:  #else, assign tag as "none"
            tagged.append({"word": word, "pos": unknown_tag})

    return (tagged)


def simple_model_3_doc(doc_to_tag, unam_d, known_d, unknown_tag):
    tagged = []
    for sent in doc_to_tag:
        tagged.append(simple_model_3(sent, unam_d, known_d, unknown_tag))

    return (tagged)


test_simple_3_tagged = simple_model_3_doc(test_data, unambiguous, top_hits,
                                          "NN")
print(test_simple_3_tagged[0])

tested_simple_3 = accuracy_doc(test_data, test_simple_3_tagged)
print(tested_simple_3)


def add_features(
    input_sent, idx, token
):  #takes a sentence as input (with word and tag specified), outputs a more feature-rich version
    features = {}
    features["word"] = token["word"]
    features["pos"] = token["pos"]
    if idx == 0:
        features["prev_pos"] = "<start>"  #no previous pos
        features["prev_pos_bg"] = "<start>_<start>"  #no  previous pos_bg
        features["prev_word"] = "<first_word>"  #no previous word

    elif idx == 1:
        features["prev_pos"] = input_sent[idx - 1]["pos"]  #previos pos_tag
        features["prev_pos_bg"] = "<start>_" + input_sent[idx - 1]["pos"]
        features["prev_word"] = input_sent[idx - 1]["word"]  #no previous word

    else:
        features["prev_pos"] = input_sent[idx - 1]["pos"]  #
        features["prev_pos_bg"] = input_sent[
            idx - 2]["pos"] + "_" + input_sent[idx - 1]["pos"]
        features["prev_word"] = input_sent[idx - 1]["word"]  #no previous word

    features["suffix_bg"] = features["word"][-2:]  #get last two characters
    features["suffix_tg"] = features["word"][-3:]  #get last two characters
    features["mx_bigram"] = features["prev_pos"] + "_" + features["word"]
    features["mx_trigram"] = features["prev_pos_bg"] + "_" + features[
        "word"]  #make pos bigram + current suffix
    features["mx_suffix_bg_bigram"] = features["prev_pos"] + "_" + features[
        "suffix_bg"]
    features[
        "mx_suffix_bg_trigram"] = features["prev_pos_bg"] + "_" + features[
            "suffix_bg"]  #make pos bigram + current suffix
    features["mx_suffix_tg_bigram"] = features["prev_pos"] + "_" + features[
        "suffix_tg"]
    features[
        "mx_suffix_tg_trigram"] = features["prev_pos_bg"] + "_" + features[
            "suffix_tg"]  #make pos bigram + current suffix

    return (features)


test = [{
    'word': 'The',
    'pos': 'DT'
}, {
    'word': 'partners',
    'pos': 'NNS'
}, {
    'word': 'each',
    'pos': 'DT'
}, {
    'word': 'bring',
    'pos': 'VB'
}, {
    'word': 'to',
    'pos': 'TO'
}, {
    'word': 'it',
    'pos': 'PRP'
}, {
    'word': 'unselfish',
    'pos': 'NN'
}, {
    'word': 'love',
    'pos': 'NN'
}, {
    'word': ',',
    'pos': ','
}, {
    'word': 'and',
    'pos': 'CC'
}, {
    'word': 'each',
    'pos': 'DT'
}, {
    'word': 'takes',
    'pos': 'VBZ'
}, {
    'word': 'away',
    'pos': 'RB'
}, {
    'word': 'an',
    'pos': 'DT'
}, {
    'word': 'equal',
    'pos': 'JJ'
}, {
    'word': 'share',
    'pos': 'NN'
}, {
    'word': 'of',
    'pos': 'IN'
}, {
    'word': 'pleasure',
    'pos': 'NN'
}, {
    'word': 'and',
    'pos': 'CC'
}, {
    'word': 'joy',
    'pos': 'NN'
}, {
    'word': '.',
    'pos': '.'
}]

for idx, x in enumerate(test[:3]):  #add features to the first three items
    print(add_features(test, idx, x))


def mult_freq(training_data):  #compile frequency data for each predictor
    freq = {}  #output dictionary
    for sent in training_data:  #iterate through training data
        for idx, token in enumerate(sent):  # add features
            tok_features = add_features(sent, idx, token)
            for feature in tok_features:
                if feature not in freq:
                    freq[feature] = {
                    }  #add feature dictionary to freq dictionary (e.g., freq["prev_pos"] = {})
                if tok_features[feature] not in freq[feature]:
                    freq[feature][tok_features[feature]] = {
                    }  #add pos dictionary (e.g., freq["prev_pos"]["DT"] = {})
                freq_add(tok_features["pos"],
                         freq[feature][tok_features[feature]]
                         )  #add pos instance to that dictionary
    return (freq)


def sort_tags_multi(featured_freq):
    top_freq = {}
    for feature in featured_freq:
        top_freq[feature] = sort_tags(featured_freq[feature])

    return (top_freq)


#compile stats on training data for each predictor:
featured_freq = mult_freq(train_data)

#create dictionary with top tag for each predictor:
top_featured_freq = sort_tags_multi(featured_freq)
print(top_featured_freq["prev_pos_bg"]["DT_JJR"])
print(top_featured_freq["prev_pos"]["DT"])


def simple_model_4(sent_to_tag, unam_d, feature_d, unknown_tag):
    tagged = []
    for idx, x in enumerate(sent_to_tag):
        word = x["word"]
        token_d = add_features(tagged, idx, x)

        if word in unam_d:  #if the word is unambiguous, assign the tag
            tagged.append({"word": word, "pos": unam_d[word]})

        #rules for known words
        elif token_d["mx_trigram"] in feature_d[
                "mx_trigram"]:  #if the pos bigram + word in the dictionary:
            tagged.append({
                "word": word,
                "pos": feature_d["mx_trigram"][token_d["mx_trigram"]]
            })

        elif token_d["mx_bigram"] in feature_d[
                "mx_bigram"]:  #if the pos bigram + word in the dictionary:
            tagged.append({
                "word": word,
                "pos": feature_d["mx_bigram"][token_d["mx_bigram"]]
            })

        elif word in feature_d["word"]:
            tagged.append({
                "word": word,
                "pos": feature_d["word"][token_d["word"]]
            })

        #rules for unknown words

        elif token_d["mx_suffix_tg_trigram"] in feature_d[
                "mx_suffix_tg_trigram"]:  #if the the pos bigram + last three letters are in the dictionary:
            tagged.append({
                "word":
                word,
                "pos":
                feature_d["mx_suffix_tg_trigram"][
                    token_d["mx_suffix_tg_trigram"]]
            })

        elif token_d["mx_suffix_tg_bigram"] in feature_d[
                "mx_suffix_tg_bigram"]:  ##if the previous POS tag + last three letters are in the dictionary
            tagged.append({
                "word":
                word,
                "pos":
                feature_d["mx_suffix_tg_bigram"][
                    token_d["mx_suffix_tg_bigram"]]
            })

        elif token_d["suffix_tg"] in feature_d[
                "suffix_tg"]:  #if the last three letters are in the dictionary:
            tagged.append({
                "word": word,
                "pos": feature_d["suffix_tg"][token_d["suffix_tg"]]
            })

        elif token_d["suffix_bg"] in feature_d[
                "suffix_bg"]:  ##if the last two letters are in the dictionary:
            tagged.append({
                "word": word,
                "pos": feature_d["suffix_bg"][token_d["suffix_bg"]]
            })

        elif token_d["prev_pos_bg"] in feature_d[
                "prev_pos_bg"]:  #if the previous pos bigram in the dictionary:
            tagged.append({
                "word":
                word,
                "pos":
                feature_d["prev_pos_bg"][token_d["prev_pos_bg"]]
            })

        elif token_d["prev_pos"] in feature_d[
                "prev_pos"]:  #if the previous pos in the dictionary:
            tagged.append({
                "word": word,
                "pos": feature_d["prev_pos"][token_d["prev_pos"]]
            })

        else:  #if somehow we have a completely new word... then tag it as a "NN" - but we actually won't ever get here (because of our POS rules).
            tagged.append({"word": word, "pos": unknown_tag})

    return (tagged)


def simple_model_4_doc(doc_to_tag, unam_d, feature_d, unknown_tag):
    tagged = []
    for sent in doc_to_tag:
        tagged.append(simple_model_4(sent, unam_d, feature_d, unknown_tag))

    return (tagged)


test_simple_4_tagged = simple_model_4_doc(test_data, unambiguous,
                                          top_featured_freq, "NN")
tested_simple_4 = accuracy_doc(test_data, test_simple_4_tagged)
print(tested_simple_4)  #94.4%


def accuracy_cmplx_sent(gold, tested, acc_dict, feature_d):
    for idx, item in enumerate(gold):
        if item["pos"] == tested[idx]["pos"]:
            acc_dict["correct"] += 1
            if item["word"] in feature_d:
                acc_dict["known_correct"] += 1
            else:
                acc_dict["unknown_correct"] += 1

        else:
            acc_dict["incorrect"] += 1
            if item["word"] in feature_d:
                acc_dict["known_incorrect"] += 1
            else:
                acc_dict["unknown_incorrect"] += 1


def accuracy_cmplx_doc(gold, tested, feature_d):
    acc_dict = {
        "correct": 0,
        "incorrect": 0,
        "known_correct": 0,
        "known_incorrect": 0,
        "unknown_correct": 0,
        "unknown_incorrect": 0
    }

    for idx, item in enumerate(gold):
        accuracy_cmplx_sent(item, tested[idx], acc_dict, feature_d)

    acc_dict["total_acc"] = acc_dict["correct"] / (acc_dict["correct"] +
                                                   acc_dict["incorrect"])
    acc_dict["known_acc"] = acc_dict["known_correct"] / (
        acc_dict["known_correct"] + acc_dict["known_incorrect"])
    acc_dict["unknown_acc"] = acc_dict["unknown_correct"] / (
        acc_dict["unknown_correct"] + acc_dict["unknown_incorrect"])

    return (acc_dict)


#check our total accuracy and the accuracy for known words and unknown words, respectively
tested_simple_4_cmplx = accuracy_cmplx_doc(test_data, test_simple_4_tagged,
                                           top_featured_freq["word"])
print(tested_simple_4_cmplx)


#code for precision, recall, and F1 formulas
def prec_rec(accuracy_dict):
    accuracy_dict["TC"] = accuracy_dict["TP"] + accuracy_dict["FN"]
    if accuracy_dict["TP"] + accuracy_dict["FN"] == 0:
        accuracy_dict["recall"] = 0
    else:
        accuracy_dict["recall"] = accuracy_dict["TP"] / (accuracy_dict["TP"] +
                                                         accuracy_dict["FN"])

    if accuracy_dict["TP"] + accuracy_dict["FP"] == 0:
        accuracy_dict["precision"] = 0
    else:
        accuracy_dict["precision"] = accuracy_dict["TP"] / (
            accuracy_dict["TP"] + accuracy_dict["FP"])
    if accuracy_dict["precision"] == 0 and accuracy_dict["recall"] == 0:
        accuracy_dict["f1"] = 0
    else:
        accuracy_dict["f1"] = 2 * (
            (accuracy_dict["precision"] * accuracy_dict["recall"]) /
            (accuracy_dict["precision"] + accuracy_dict["recall"]))


def possible_tags(
    dataset
):  #create preliminary accuracy dictionary (used in tag_prec_rec_doc() below)
    acc_dict = {}
    for sent in dataset:
        for token in sent:
            if token["pos"] not in acc_dict:
                acc_dict[token["pos"]] = {"TP": 0, "FP": 0, "FN": 0}
    return (acc_dict)


#code for compilation of true positives, false positives, and false negatives for each tag
def tag_prec_rec_sent(gold, tested, tag_d):
    for idx, item in enumerate(gold):
        if item["pos"] == tested[idx]["pos"]:
            tag_d[item["pos"]]["TP"] += 1
        else:
            tag_d[item["pos"]]["FN"] += 1
            tag_d[tested[idx]["pos"]]["FP"] += 1


#code to apply the above function to a full dataset
def tag_prec_rec_doc(gold, tested, feature_d, full_data):
    tag_d = possible_tags(full_data)
    print(tag_d)
    for idx, item in enumerate(gold):
        tag_prec_rec_sent(item, tested[idx], tag_d)

    for x in tag_d:
        prec_rec(tag_d[x])

    return (tag_d)


#get detailed tag information for our model
tested_simple_4_pr = tag_prec_rec_doc(test_data, test_simple_4_tagged,
                                      top_featured_freq, full_data)

#sort the dictionary by tag frequency to make it easier to read:
from operator import *

simple_4_pr_sorted = sorted(tested_simple_4_pr.items(),
                            key=lambda x: getitem(x[1], 'TC'),
                            reverse=True)

#Check out precision and recall for the five most frequent tags
for x in simple_4_pr_sorted[:5]:
    print(x)
