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
            outf.write("\t".join([
                token['token1'], token['token2'], token['tag1'], token['tag2']
            ]))
            outf.write("\n")
        outf.write("\n\n")


def filter_agreements_v2(anno: list):

    disagreed = []
    agreed = []

    for sent in anno:

        disagree = False

        for t in sent['lines']:
            if t['token1'] == t['token2']:
                if t['tag1'] != t['tag2']:
                    print(t['tag1'], t['tag2'])
                    disagree = True
        if disagree:
            disagreed.append(sent)
        else:
            agreed.append(sent)
    return (disagreed, agreed)


def writebysent_v2(sent: dict, outfile: str, outdir: str):

    with open(outdir + outfile + ".txt", 'a') as outf:
        #outf.write("#New sent below\n")
        outf.write("#Sentence.id={}\n".format(sent['sentid']))
        outf.write("#Text={}\n".format(sent['text']))
        outf.write('Tokenid\tToken1\tToken2\tTag1\tTag2\n')

        for token in sent['lines']:
            outf.write("\t".join([
                token['tid'], token['token1'], token['token2'], token['tag1'],
                token['tag2']
            ]))
            outf.write("\n")
        outf.write("\n\n")


files = glob.glob('data/input_for_reliabiliy/Aaron_completed_As/*.json')

files = glob.glob('data/input_for_reliabiliy/Training_Ryan/*.json')

for file in files:
    print(file)
    text = json.load(open(file, 'r'))

    dagr, agr = filter_agreements_v2(text)
    #dagr, agr = filter_agreements(text)
    for sent in dagr:
        label_pair = []
        print(sent['chunkid'])
        for t in sent['lines']:
            print(t['tid'])
            if t['token1'] == t['token2']:
                if t['tag1'] != t['tag2']:
                    label_pair.append("{}-{}".format(t['tag1'], t['tag2']))

        if len(label_pair) > 0:
            for pair in label_pair:
                writebysent_v2(sent, pair,
                               'data/disagreed_sentences/Ryan/Training14-25/')
