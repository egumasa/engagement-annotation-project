import re
import csv
import json
import os

import glob
import random


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


def line2dict(line: str, cols):
    l = {}
    items = line.strip().split("\t")

    for c, label in zip(cols, items):
        l[c] = label
    return l


col_def = ['tid', 'chid', 'token', 'tag', 'pos', 'clause', 'engmt', 'modal']

line2dict("1-1\t0-2\tIt\tPRP\tPRON\tMAIN[1]\t_\t_\t", col_def)


def conll2dict(conllfile: str):
    '''Takes conll file as string
    outputs 
    holder[chunkid] =  {'sentId': sent_id, 'Text': text, 'lines': temp}
    '''
    features = []
    cols = [
        'tid',
        'chid',
        'word',
    ]
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

            elif "#T_SP=" in line:  #for webanno tsv format
                if 'POS' in line:
                    features.append('POS')
                    cols.extend(['tag', 'pos'])
                elif 'Clause' in line:
                    features.append('Clause')
                    cols.extend(['clause'])
                elif 'Engagement' in line:
                    features.append('Engagement')
                    cols.extend(['engmt'])
                elif 'ModalSense' in line:
                    features.append('Modal')
                    cols.extend(['modal'])
            elif "#" in line[0]:
                pass
            else:
                temp.append(line2dict(line, cols))
        if len(temp) > 0:  #skip line with no sentences
            holder[chunkid] = {'sentId': sent_id, 'Text': text, 'lines': temp}
    return holder


def sent2iob(sent_lines: list, col_size: int = 5, feature: str = 'engmt'):
    holder = []
    seen_tags = {}

    for l in sent_lines:
        tags = l[feature].split("|")
        if len(tags) > 1:
            print(tags)

        iob_tags = []

        for tag in tags:
            pat = r"(.*)\[(\d+)\]"
            match = re.match(pat, tag)

            if match:  ## multiword tags
                if tag not in seen_tags:
                    seen_tags[tag] = None
                    ## strip number here
                    iob_tags.append("B-{}".format(match.group(1)))
                else:
                    ## strip number here
                    iob_tags.append("I-{}".format(match.group(1)))

            else:
                if tag not in ["_", "*"]:
                    iob_tags.append("B-{}".format(tag))
                else:
                    iob_tags.append("O")

        #Then store as string
        n_tags = len(iob_tags)
        for i in range(0, col_size - n_tags):
            iob_tags.append("O")

        holder.append("\t".join([l['word']] + iob_tags))
    return holder


# pat = r"(.*)\[(\d+)\]"
# match = re.match(pat, 'DENY[1]')

# if match:
#     print("yes")

# file1 = "data/Annotated_files_ALM/completed_archive/download-20220616/1C-Batch/2C_completed/batch1_C6_pos_ALM.tsv"


def tsv2sentlist(filename: str):

    holder = []

    conll_file = conll2dict(open(filename, 'r').read())
    for sid, sent in conll_file.items():
        holder.append(sent2iob(sent['lines']))

    return (holder)


def write_file(output_name: str, data: list):
    with open(output_name, 'w') as f:

        for sent in data:
            for line in sent:
                f.write(line)
                f.write('\n')
            f.write('\n')


# The output would be
def Run():
    filenames = glob.glob(
        '/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/engagement-annotation-project/data/data_to_convert/20220719_data_to_train/*.tsv'
    )

    holder = []
    for file in filenames:
        holder.extend(tsv2sentlist(file))

    random.seed(1993)
    random.shuffle(holder)

    size = len(holder)

    train, dev = holder[0:int(size * 0.9)], holder[int(size * 0.9):]

    write_file('data/iob_data/train.iob', train)
    write_file('data/iob_data/dev.iob', dev)


if __name__ == "__main__":
    Run()