import re
import csv
import json
import os
from scripts.utils.aligner import needle, water

# file1 = "data/Annotated_files_ALM/Aaron_Afiles_220517/batch1_A1_pos_ALM.tsv"
# file2 = "data/Annotated_files_ME/batch1_A1_pos_ME.tsv"

# conll1 = open(file1, 'r').read()
# conll2 = open(file2, 'r').read()


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
        if len(temp) > 0:  #skip line with no sentences
            holder.append(temp)
    return holder


def conll2dict(conllfile):
    holder = {}
    for chunkid, chunk in enumerate(conllfile.split('\n\n')):
        temp = []
        sent_id = "NA"
        for line in chunk.split("\n"):
            if len(line) < 1:
                continue
            elif "#Sentence.id" in line:
                sent_id = re.match(r'#Sentence\.id=(.+)', line).group(1)
                print(sent_id)
            elif "#Text=" in line:
                text = re.match(r'#Text=(.+)', line).group(1)
            elif "#" in line[0]:
                #print(line)
                pass
            else:
                temp.append(line)
        if len(temp) > 0:  #skip line with no sentences
            holder[chunkid] = {'sentId': sent_id, 'Text': text, 'lines': temp}
    return holder


# list1 = conll2dict(conll1)
# list2 = conll2list(conll2)


def clean_tag(label: str):
    '''This function cleans the token labels.
    '''
    labels = label.split("|")  #when multiple tags

    newlabels = []
    for lbl in labels:
        print(lbl)
        pat = r"(.*)\[(\d+)\]"
        match = re.match(pat, lbl)
        if match:
            #print(label)
            newlabel = match.group(1)
            l_id = match.group(2)
            newlabels.append((newlabel, l_id))
            #print(newlabel)
        else:
            newlabels.append((lbl, "NA"))
    return newlabels


def strip_identifier(labels: list):
    newlabels = []
    label_ids = {"_": ""}
    for lbl in labels:
        # print(lbl)
        pat = r"(.*)\[(\d+)\]"
        match = re.match(pat, lbl)
        if match:
            #print(label)
            newlabel = match.group(1)
            l_id = match.group(2)
            newlabels.append(newlabel)
            label_ids[newlabel] = l_id
            #print(newlabel)
        else:
            newlabels.append(lbl)
            label_ids[lbl] = ""
    return newlabels, label_ids


def align_tag(label1: str, label2: str, sep: str = "|"):
    '''This function takes a pair of annotation labels.
    Each annotation can have two or more labels (due to Webanno.tsv format)
    The function does the following:
        1. split annotations by the separator; "|" by default
        2. 
    '''
    labels1 = label1.split(sep)  #when multiple tags
    labels2 = label2.split(sep)  #when multiple tags

    #This separates TAG and ID e.g., TAG[ID]
    new1, id1 = strip_identifier(labels1)
    new2, id2 = strip_identifier(labels2)

    ndl = needle(new1, new2)  #align the two

    aligned1, aligned2 = ndl[2], ndl[3]

    annotations = []

    for a, b in zip(aligned1, aligned2):
        #print(a, b)
        annotations.append((a, id1[a], b, id2[b]))

    return annotations


def list2alignedtokens(list1, list2):
    sent = []
    for sent1, sent2 in zip(list1, list2):
        tokens = []
        if len(sent1) == len(sent2):
            # iterating the two sentences
            # Accuracy for clause, ENGAGEMENT and modal verb

            for t1, t2 in zip(sent1, sent2):
                tid1, charid, token1, xpos1, upos1, cl1, eng1, md1 = t1.strip(
                ).split("\t")
                tid2, charid, token2, xpos2, upos2, cl2, eng2, md2 = t2.strip(
                ).split("\t")

                aligned_anno = align_tag(eng1, eng2)
                #eng1 = clean_tag(eng1)
                #eng2 = clean_tag(eng2)

                for lbl1, id1, lbl2, id2 in aligned_anno:
                    line = {
                        'tid': tid1,
                        'token1': token1,
                        'token2': token2,
                        'tag1': lbl1,
                        'tag2': lbl2,
                        'id1': id1,
                        'id2': id2
                    }

                    tokens.append(line)
        else:
            for t1, t2 in zip(sent1, sent2):
                print(t1, t2)
        sent.append(tokens)
    return sent


def dict2alignedtokens(dict1, dict2):
    sent = []
    for chunkid, content1 in dict1.items():
        content2 = dict2[chunkid]

        tokens = []
        cid = chunkid

        if content1['sentId'] == content2['sentId']:  #Check alignment
            # iterating the two sentences
            # Accuracy for clause, ENGAGEMENT and modal verb
            sentid = content1['sentId']
            text = content1['Text']

            for t1, t2 in zip(content1['lines'], content2['lines']):
                if len(t2.strip().split("\t")) > 7:
                    tid1, charid, token1, xpos1, upos1, cl1, eng1, md1 = t1.strip(
                    ).split("\t")
                    tid2, charid, token2, xpos2, upos2, cl2, eng2, md2 = t2.strip(
                    ).split("\t")
                elif len(t2.strip().split("\t")) == 7:
                    tid1, charid, token1, xpos1, upos1, cl1, eng1, md1 = t1.strip(
                    ).split("\t")
                    tid2, charid, token2, xpos2, upos2, cl2, eng2 = t2.strip(
                    ).split("\t")
                elif len(t1.strip().split("\t")) > 3:
                    tid1, charid, token1, cl1, eng1 = t1.strip().split("\t")
                    tid2, charid, token2, cl2, eng2 = t2.strip().split("\t")

                aligned_anno = align_tag(eng1, eng2)
                #eng1 = clean_tag(eng1)
                #eng2 = clean_tag(eng2)

                for lbl1, id1, lbl2, id2 in aligned_anno:
                    line = {
                        'tid': tid1,
                        'token1': token1,
                        'token2': token2,
                        'tag1': lbl1,
                        'tag2': lbl2,
                        'id1': id1,
                        'id2': id2
                    }

                    tokens.append(line)

            sent.append({
                "chunkid": cid,
                "sentid": sentid,
                "text": text,
                "lines": tokens
            })
        else:
            for t1, t2 in zip(sent1, sent2):
                print(t1, t2)

    return sent


def tsv2json(start,
             end,
             batch_letter: str,
             anno_name1: str,
             anno_name2: str,
             tsv_root: str = 'data/annotated_tsv/',
             json_dir: str = 'input_for_reliability'):

    for fileno in range(start, end):

        file1 = "data/annotated_tsv/{}/{}-batch/batch1_{}{}_pos_{}.tsv".format(
            anno_name1, batch_letter, batch_letter, fileno, anno_name1)
        file2 = "data/annotated_tsv/{}/{}-batch/batch1_{}{}_pos_{}.tsv".format(
            anno_name2, batch_letter, batch_letter, fileno, anno_name2)
        # file1 = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/Annotated_files_ME/batch1_A{}_pos_ME.tsv".format(
        #     fileno)
        # file2 = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/Annotated_files_ALM/2A_completed/batch1_A{}_pos_ALM.tsv".format(
        #     fileno)
        conll1 = open(file1, 'r').read()
        conll2 = open(file2, 'r').read()
        #list1 = conll2list(conll1)
        #list2 = conll2list(conll2)
        dict1 = conll2dict(conll1)
        dict2 = conll2dict(conll2)

        #aln_list = list2alignedtokens(list1, list2)
        aln_list = dict2alignedtokens(dict1, dict2)

        ## Creating directory if not exist
        path = 'data/{}/{}-{}'.format(json_dir, anno_name1, anno_name2)

        isExist = os.path.exists(path)

        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)
            print("The new directory is created!")

        with open(
                "data/{}/{}-{}/{}{}_{}-{}.json".format(
                    json_dir,
                    anno_name1,
                    anno_name2,
                    batch_letter,
                    fileno,
                    anno_name1,
                    anno_name2,
                ), 'w') as f:
            json.dump(aln_list, f, indent=2)


# tsv2json(0, 10, "A", "ME", "RW")

# list2alignedtokens(list1, list2)

if __name__ == "__main__":
    for fileno in range(0, 10):
        file1 = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/Annotated_files_ME/A-batch/batch1_A{}_pos_ME.tsv".format(
            fileno)
        file2 = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/Annotated_files_Ryan/A_files_1st-round/batch1_A{}_pos_RW.tsv".format(
            fileno)
        # file1 = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/Annotated_files_ME/batch1_A{}_pos_ME.tsv".format(
        #     fileno)
        # file2 = "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/Annotated_files_ALM/2A_completed/batch1_A{}_pos_ALM.tsv".format(
        #     fileno)
        conll1 = open(file1, 'r').read()
        conll2 = open(file2, 'r').read()
        #list1 = conll2list(conll1)
        #list2 = conll2list(conll2)
        dict1 = conll2dict(conll1)
        dict2 = conll2dict(conll2)

        #aln_list = list2alignedtokens(list1, list2)
        aln_list = dict2alignedtokens(dict1, dict2)

        with open(
                "/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/input_for_reliabiliy/Ryan_As_20220620/A_batch_Ryan{}_20220620_.json"
                .format(fileno), 'w') as f:
            json.dump(aln_list, f, indent=2)

# for line in conll2.split('\n'):
#     if len(line) < 1:
#         continue
#     elif "#" in line[0]:
#         #print(line)
#         pass
#     else:
#         print(line)
