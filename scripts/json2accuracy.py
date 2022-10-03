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

import csv
import itertools


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
    '''This function cleans the token labels.'''

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


# with open(
#         "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/input_for_reliabiliy/batch1_A0_test.json",
#         'r') as f:
#     temp = json.load(f)

# for l in temp:
#     print(l)


def reduce_entry(anno: list, layer: str = "eng"):
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
        for l in sent[layer]:  #sent is a dictionary
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


def dict2csv(rec_prec_f1: dict, save_dir: str):
    fields = ['Eng', 'recall', 'precision', 'f1', 'TC', "TP", 'FP', 'FN']
    with open(save_dir, "w") as f:
        w = csv.DictWriter(f, fields)
        w.writeheader()
        for k in rec_prec_f1:
            w.writerow(
                {field: rec_prec_f1[k].get(field) or k
                 for field in fields})


# result = calc_recall_prec_f1(temp_dict)
# dict2csv(calc_recall_prec_f1(temp_dict), 'data/pres_recall_f1_RyanA0-9.csv')


def json2dict(json_list: list,
              anno_name1: str,
              anno_name2: str,
              batch_letter: str,
              regex_fileno: str = "*",
              output_dir: str = 'benchmark_scores',
              csv_out: bool = True,
              input_root: str = 'data/input_for_reliability'):

    # holder = []
    clauses = []
    engmts = []
    splmts = []

    for file in json_list:
        with open(file, 'r') as f:
            jsonf = json.load(f)
            cl_lst = reduce_entry(jsonf, layer="cl")
            eng_lst = reduce_entry(jsonf, layer='eng')
            spl_lst = reduce_entry(jsonf, layer='spl')

            clauses.extend(cl_lst)
            engmts.extend(eng_lst)
            splmts.extend(spl_lst)

    cl_dict = list2dict(clauses)
    cl_result = calc_recall_prec_f1(cl_dict)
    eng_dict = list2dict(engmts)
    eng_result = calc_recall_prec_f1(eng_dict)
    spl_dict = list2dict(splmts)
    spl_result = calc_recall_prec_f1(spl_dict)

    if csv_out:
        dict2csv(
            cl_result, 'data/{}/cl_agreement_{}-{}_{}{}.csv'.format(
                output_dir, anno_name1, anno_name2, batch_letter,
                regex_fileno))
        dict2csv(
            eng_result, 'data/{}/eng_agreement_{}-{}_{}{}.csv'.format(
                output_dir, anno_name1, anno_name2, batch_letter,
                regex_fileno))
        dict2csv(
            spl_result, 'data/{}/spl_agreement_{}-{}_{}{}.csv'.format(
                output_dir, anno_name1, anno_name2, batch_letter,
                regex_fileno))

    return cl_result, eng_result, spl_result


#json2dict("ME", "RW", "A")

if __name__ == "__main__":

    inputfiles = glob.glob(
        "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/input_for_reliabiliy/Ryan_As_20220620/A_batch_Ryan[0-9]_20220620_.json"
    )
    len(inputfiles)

    holder = []
    for file in inputfiles:
        with open(file, 'r') as f:
            lst = reduce_entry(json.load(f))

            holder.extend(lst)

    temp_dict = list2dict(holder)
    simple_acc(temp_dict)
    pp.pprint(calc_recall_prec_f1(temp_dict))

    ## aaron

    inputfiles = glob.glob(
        "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/input_for_reliabiliy/Aaron_completed_As/A_batch_Aaron*_20220620_.json"
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

    ## Aaron and Ryan agreement

    inputfiles = glob.glob(
        "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/input_for_reliabiliy/Aaron-Ryan/A_batch_AaronRyan*_20220620_.json"
    )
    holder = []
    for file in inputfiles:

        with open(file, 'r') as f:
            lst = reduce_entry(json.load(f))

            holder.extend(lst)

    temp_dict = list2dict(holder)
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
