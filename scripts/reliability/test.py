import glob
import os, re
import json
import pprint as pp
from scripts.matching_webannotsv import conll2dict  #dict2alignedtokens
from scripts.utils.aligner import needle, water
from scripts.json2accuracy import json2dict

# pp.pprint(conll2dict(open(files1[0]).read()), sort_dicts=False)


def _print_connll_lines(dicted_conll: dict,
                        print_line: bool = False,
                        print_lineno=False):

    for id, sent in dicted_conll.items():
        for token in sent['lines']:
            if print_lineno == True:
                print("Line no.: {}".format(len(token.split('\t'))))
            if print_line:
                print(token)
            line = len(token.split('\t'))
    return line


# for i in range(0, 49):
#     _print_connll_lines(conll2dict(open(files1[i]).read()))

# _print_connll_lines(conll2dict(open(files1[7]).read()), True)


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


def dict2alignedtokens(dict1, dict2):
    sent = []
    for chunkid, content1 in dict1.items():
        content2 = dict2[chunkid]

        tokens = []
        cl_anno = []
        eng_anno = []
        spl_anno = []

        cid = chunkid

        _sameSent = (content1['sentId']
                     == content2['sentId']) or (content1['Text']
                                                == content2['Text'])

        if _sameSent:  #Check alignment
            # iterating the two sentences
            # Accuracy for clause, ENGAGEMENT and modal verb
            sentid = content1['sentId']
            if sentid == "NA":
                sentid = content2['sentId']
            text = content1['Text']

            for t1, t2 in zip(content1['lines'], content2['lines']):
                if len(t1.strip().split("\t")) == 10:
                    tid1, charid, token1, xpos1, upos1, cl1, eng1, hierarchy1, supplement1, _ = t1.strip(
                    ).split("\t")
                elif len(t1.strip().split("\t")) == 9:
                    tid1, charid, token1, xpos1, upos1, cl1, eng1, hierarchy1, supplement1 = t1.strip(
                    ).split("\t")
                elif len(t1.strip().split("\t")) > 10:
                    tid1, charid, token1, xpos1, upos1, cl1, eng1, hierarchy1, _, _, supplement1 = t1.strip(
                    ).split("\t")
                else:  #len(t1.strip().split("\t")) == 8:
                    print(len(t1.strip().split("\t")))
                    tid1, charid, token1, xpos1, upos1, cl1, eng1, hierarchy1 = t1.strip(
                    ).split("\t")
                    supplement1 = "_"

                if len(t2.strip().split("\t")) == 10:
                    tid2, charid, token2, xpos2, upos2, cl2, eng2, hierarchy2, supplement2, _ = t2.strip(
                    ).split("\t")
                elif len(t2.strip().split("\t")) == 9:
                    tid2, charid, token2, xpos2, upos2, cl2, eng2, hierarchy2, supplement2 = t2.strip(
                    ).split("\t")
                elif len(t2.strip().split("\t")) > 10:
                    tid2, charid, token2, xpos2, upos2, cl2, eng2, hierarchy2, _, _, supplement2 = t2.strip(
                    ).split("\t")
                else:  #len(t2.strip().split("\t")) == 8:
                    print(len(t2.strip().split("\t")))
                    tid2, charid, token2, xpos2, upos2, cl2, eng2, hierarchy2 = t2.strip(
                    ).split("\t")
                    supplement2 = "_"

                aligned_cl = align_tag(cl1, cl2)
                aligned_eng = align_tag(eng1, eng2)
                aligned_spl = align_tag(supplement1, supplement2)
                #print(aligned_spl)
                #eng1 = clean_tag(eng1)
                #eng2 = clean_tag(eng2)

                for lbl1, id1, lbl2, id2 in aligned_cl:
                    cl_line = {
                        'tid': tid1,
                        'token1': token1,
                        'token2': token2,
                        'tag1': lbl1,
                        'tag2': lbl2,
                        'id1': id1,
                        'id2': id2
                    }
                    cl_anno.append(cl_line)

                for lbl1, id1, lbl2, id2 in aligned_eng:
                    eng_line = {
                        'tid': tid1,
                        'token1': token1,
                        'token2': token2,
                        'tag1': lbl1,
                        'tag2': lbl2,
                        'id1': id1,
                        'id2': id2
                    }
                    eng_anno.append(eng_line)

                for lbl1, id1, lbl2, id2 in aligned_spl:
                    spl_line = {
                        'tid': tid1,
                        'token1': token1,
                        'token2': token2,
                        'tag1': lbl1,
                        'tag2': lbl2,
                        'id1': id1,
                        'id2': id2
                    }
                    #tokens.append(line)
                    spl_anno.append(spl_line)

            sent.append({
                "chunkid": cid,
                "sentid": sentid,
                "text": text,
                "lines": tokens,
                "cl": cl_anno,
                "eng": eng_anno,
                "spl": spl_anno
            })

        else:
            for t1, t2 in zip(content1['lines'], content2['lines']):
                print(t1, t2)

    return sent


annotator1 = "RW"
annotator2 = "ME"
json_dir = 'input_for_reliability'
batch_letter = 'Batch2'
fno = '0000-0049'

files1 = glob.glob('data/annotated_for_reliability/Batch2/{}/{}/*.tsv'.format(
    annotator1, fno))
files1.sort()

files2 = glob.glob('data/annotated_for_reliability/Batch2/{}/{}/*.tsv'.format(
    annotator2, fno))
files2.sort()


def run():

    holder = []
    for file1, file2 in zip(files1, files2):

        conll1 = open(file1, 'r').read()
        conll2 = open(file2, 'r').read()

        dict1 = conll2dict(conll1)
        dict2 = conll2dict(conll2)

        aln_list = dict2alignedtokens(dict1, dict2)

        holder.extend(aln_list)
        ## Creating directory if not exist
    path = 'data/{}/{}-{}'.format(json_dir, annotator1, annotator2)
    print(path)
    isExist = os.path.exists(path)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print("The new directory is created!")

    with open(
            "data/{}/{}-{}/{}{}_{}-{}.json".format(
                json_dir,
                annotator1,
                annotator2,
                batch_letter,
                fno,
                annotator1,
                annotator2,
            ), 'w') as f:
        json.dump(holder, f, indent=2)


run()

inputdata = ['data/input_for_reliability/RW-ME/Batch20000-0049_RW-ME.json']
json2dict(inputdata, "RW", "ME", "2")