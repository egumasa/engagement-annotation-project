import glob
from html import entities
from textwrap import indent
import spacy
import re
import json

from scripts.tsv2iob import conll2dict, sent2iob
from construction_analysis.scripts.preprocess_genia import parse_genia

nlp = spacy.load('en_core_web_trf')
eng_parser = spacy.load(
    '/Users/masakieguchi/Dropbox/0_Projects/0_basenlp/SFLAnalyzer/Engagement_span_finder/packages/en_engagement_RoBERTa-0.0.2/en_engagement_RoBERTa/en_engagement_RoBERTa-0.0.2'
)


def tsv2docs(filename: str):
    holder = []

    conll_file = conll2dict(open(filename, 'r').read())
    for sid, sent in conll_file.items():
        meta = sent['sentId']
        doc = nlp(sent['Text'])
        eng = eng_parser(sent['Text'])
        iobs = sent2iob(sent['lines'])
        holder.append((doc, eng, iobs, meta))
    return (holder)


# def span_extraction(doc, spans_key: str = 'sc'):
#     # first extract spans
#     # from displacy https://github.com/explosion/spaCy/blob/eaf66e74314cf5262cee0f41a42c36dc39fc0975/spacy/displacy/__init__.py#L220
#     spans = [
#         {
#             'span_text': span.text,
#             "span_root": span.root,
#             "start": span.start_char,
#             "end": span.end_char,
#             "start_token": span.start,
#             "end_token": span.end,
#             "label": span.label_,
#             # "kb_id": span.kb_id_ if span.kb_id_ else "",
#             # "kb_url": kb_url_template.format(span.kb_id_) if kb_url_template else "#",
#         } for span in doc.spans[spans_key]
#     ]
#     return (spans)


def docs2tokens(sentence: tuple, spans_key: str = 'sc'):
    spans = span_extraction(sentence[1], spans_key='sc')
    tok = []

    for t, engt, l in zip(sentence[0], sentence[1], sentence[2]):
        #print(t.text, engt.text, l)
        assert t.text == engt.text
        assert t.text == l.split("\t")[0]
        ###
        if t.ent_iob_ == "O":
            ner = t.ent_iob_
        else:
            ner = "{}-{}".format(t.ent_iob_, t.ent_type_)
        token_info = [
            t.text, t.lemma_, t.pos_, t.tag_, t.dep_, t.head.text,
            str(t.morph), ner
        ]

        # span extraction From displacy
        # https://github.com/explosion/spaCy/blob/eaf66e74314cf5262cee0f41a42c36dc39fc0975/spacy/displacy/render.py#L139
        engagement = []
        for span in spans:
            #ent = {}
            if span["start_token"] <= engt.i < span["end_token"]:
                if engt.i == span["start_token"]:
                    eng = "B-{}".format(span['label'])
                else:
                    eng = "I-{}".format(span['label'])
                engagement.append(eng)
        if len(engagement) == 0:
            engagement.append("-")
        tok.append(token_info + l.split("\t") + engagement)
        # print("\t".join(token_info), l, "\t".join(engagement))
    return tok


for file in filenames[0:1]:
    hold = tsv2docs(file)
    print(hold[2][2])

# def convert_iob2spans(doc_holder):

#     spans = {}

#     for sentence in doc_holder:
#         spacy_doc = sentence[0]

#         for l in sentence[2]:
#             hold = []
#             tag_list = l.split('\t')

#             for tag in tag_list:
#                 match = re.match(r"(B|I)\-(.+?)$", tag)

#                 if match:
#                     # print(match.group(2))
#                     if match.group(2) not in cx_dict:
#                         cx_dict[match.group(2)] = []


def extract_construction_info(token, span=None):

    if span == None:
        span_text = None
    else:
        span_text = span['span_text']
    norm = token.norm_
    lemma = token.lemma_,
    dep = token.dep_
    pos = token.pos_
    tag = token.tag_
    head = token.head.norm_
    head_dep = token.head.dep_
    head_tag = token.head.tag_
    child = ["{}_{}".format(c.norm_, c.dep_) for c in token.children]
    child_deps = [c.dep_ for c in token.children]
    child_seq = "-".join([c.dep_ for c in token.children])

    return {
        'norm': norm,
        'lemma': lemma,
        'span_text': span_text,
        "dep": dep,
        "word_dep_tag": "{}_{}_{}".format(norm, dep, tag),
        "pos": pos,
        "tag": tag,
        "child_deps": child_deps,
        "child_seq": child_seq,
        "head": head,
        "head_dep": head_dep,
        'head_dep_tag': "{}_{}_{}".format(head, head_dep, head_tag),
        "child": child,
    }


def span_extraction(doc, spans_key: str = 'sc'):
    # first extract spans
    # from displacy https://github.com/explosion/spaCy/blob/eaf66e74314cf5262cee0f41a42c36dc39fc0975/spacy/displacy/__init__.py#L220
    try:
        spans = [
            {
                'span_text': span.text,
                "span_root": span.root,
                "span_root_idx": span.root.i,
                "start": span.start_char,
                "end": span.end_char,
                "start_token": span.start,
                "end_token": span.end,
                "label": span.label_,
                # "kb_id": span.kb_id_ if span.kb_id_ else "",
                # "kb_url": kb_url_template.format(span.kb_id_) if kb_url_template else "#",
            } for span in doc.spans[spans_key]
        ]
    except KeyError:
        spans = [
            {
                'span_text': span.text,
                "span_root": span.root,
                "span_root_idx": span.root.i,
                "start": span.start_char,
                "end": span.end_char,
                "start_token": span.start,
                "end_token": span.end,
                "label": None,
                # "kb_id": span.kb_id_ if span.kb_id_ else "",
                # "kb_url": kb_url_template.format(span.kb_id_) if kb_url_template else "#",
            } for span in doc.spans[spans_key]
        ]
    return (spans)


# def span_extraction(doc, spans_key: str = 'sc'):
#     # first extract spans
#     # from displacy https://github.com/explosion/spaCy/blob/eaf66e74314cf5262cee0f41a42c36dc39fc0975/spacy/displacy/__init__.py#L220

#     spans = [
#         {
#             'span_text': span.text,
#             "span_root": span.root,
#             "start": span.start_char,
#             "end": span.end_char,
#             "start_token": span.start,
#             "end_token": span.end,
#             "label": span.label_,
#             # "kb_id": span.kb_id_ if span.kb_id_ else "",
#             # "kb_url": kb_url_template.format(span.kb_id_) if kb_url_template else "#",
#         } for span in doc.spans[spans_key]
#     ]
#     return (spans)

# iob_holder = "\n\n".join(["\n".join(s[2]) for s in doc_holder])
# span_doc = parse_genia(iob_holder, span_key='sc', num_levels=3)

# for doc in span_doc:
#     spans = span_extraction(doc)

#     for span in spans:
#         print(span)


def cx_analysis(doc_holder, cx_dict: dict, process_in_batch: bool = True):

    if process_in_batch:
        iob_holder = "\n\n".join(["\n".join(s[2]) for s in doc_holder])
        span_doc = parse_genia(iob_holder, span_key='sc', num_levels=3)

        for doc in span_doc:
            spans = span_extraction(doc)
            for span in spans:
                span_root = span['span_root']
                span_text = span['span_text']
                span_root_idx = span['span_root_idx']
                label = span['label']
                #print(span_text, span_root)

                if label not in cx_dict:
                    cx_dict[label] = []

                cx_dict[label].append(
                    extract_construction_info(
                        doc[span_root_idx:span_root_idx + 1], span))

    else:
        for sentence in doc_holder:
            print(sentence[-1])
            print("\n".join(sentence[2]))

            doc = sentence[0]
            # extract spans from l
            span_doc = parse_genia("\n".join(sentence[2]),
                                   span_key='sc',
                                   num_levels=3)

            print(len(span_doc))
            spans = span_extraction(span_doc[0])

            for span in spans:
                print(span)
                '''
                {
                    'span_text': span.text,
                    "span_root": span.root,
                    "start": span.start_char,
                    "end": span.end_char,
                    "start_token": span.start,
                    "end_token": span.end,
                    "label": span.label_,
                    # "kb_id": span.kb_id_ if span.kb_id_ else "",
                    # "kb_url": kb_url_template.format(span.kb_id_) if kb_url_template else "#",
                } for span in doc.spans[spans_key]
                '''
                span_root = span['span_root']
                span_text = span['span_text']
                span_root_idx = span['span_root_idx']
                label = span['label']
                #print(span_text, span_root)

                if label not in cx_dict:
                    cx_dict[label] = []

                cx_dict[label].append(
                    extract_construction_info(
                        doc[span_root_idx:span_root_idx + 1].root, span))

        # parse_genia covers this part
        # for t, engt, l in zip(sentence[0], sentence[1], sentence[2]):
        #     tag_list = l.split('\t')

        #     for tag in tag_list:
        #         match = re.match(r"(B|I)\-(.+?)$", tag)
        #         if match:
        #             # print(match.group(2))
        #             if match.group(2) not in cx_dict:
        #                 cx_dict[match.group(2)] = []

        #             cx_dict[match.group(2)].append(
        #                 extract_construction_info(t))


def run_cx_analysis(
        filenames: list,
        output: bool = True,
        output_name: str = 'construction_analysis/results/test.json'):

    cx = {}
    for file in filenames:
        hold = tsv2docs(file)

        cx_analysis(
            hold, cx,
            process_in_batch=False)  # to allow only head, think about this.
    if output:
        with open(output_name, 'w') as f:
            json.dump(cx, f, indent=2)
    return cx


def output_conll(filenames: list):
    with open("construction_analysis/data/conll.tsv", 'w') as f:
        for file in filenames:
            hold = tsv2docs(file)
            for sent in hold:
                f.write("#Text={}\n".format(sent[-1]))

                token_list = docs2tokens(sent)
                for l in token_list:
                    # print(l)

                    f.write("\t".join(l))
                    f.write('\n')
                f.write('\n')
                # align(sent)


def dicter(item: str, target_dict: dict):
    if item not in target_dict:
        target_dict[item] = 1
    else:
        target_dict[item] += 1


def count_tag_per_move(
        cx_dict: dict,
        engagement: str,
        output: bool = True,
        outputname: str = 'construction_analysis/results/construction_freq'):
    cx_freq = {}
    keys = []
    for cx in cx_dict[engagement]:
        if keys == []:
            keys.extend(list(cx.keys()))
        for key in keys:
            if key not in cx_freq:
                cx_freq[key] = {}

            if type(cx[key]) == str:
                dicter(cx[key], cx_freq[key])
            elif type(cx[key]) == list:
                for item in cx[key]:
                    dicter(item, cx_freq[key])

    ## output
    if output:
        with open("{}_{}.json".format(outputname, engagement), 'w') as f:
            json.dump(cx_freq, f, indent=2)

    return cx_freq


# filenames = glob.glob('construction_analysis/data/tsv/*.tsv')
# cx_dict = run_cx_analysis(filenames, output=False)

if __name__ == "__main__":
    # load the tsv file
    filenames = glob.glob('construction_analysis/data/tsv/*.tsv')
    cx_dict = run_cx_analysis(
        filenames, output_name='construction_analysis/results/span_info.json')
    count_tag_per_move(cx_dict, "DENY")
    count_tag_per_move(cx_dict, "COUNTER")
    count_tag_per_move(cx_dict, "CONCUR")
    count_tag_per_move(cx_dict, "ENDORSE")
    count_tag_per_move(cx_dict, "PRONOUNCE")
    count_tag_per_move(cx_dict, "ATTRIBUTE")
    count_tag_per_move(cx_dict, "ENTERTAIN")
    count_tag_per_move(cx_dict, "MONOGLOSS")
    count_tag_per_move(cx_dict, "JUSTIFY")

    # processing both doc and iob sequence
filenames = glob.glob('construction_analysis/data/tsv/*.tsv')
cx_dict = run_cx_analysis(
    filenames, output_name='construction_analysis/results/span_info.json')
count_tag_per_move(cx_dict, "DENY")
count_tag_per_move(cx_dict, "COUNTER")
count_tag_per_move(cx_dict, "CONCUR")
count_tag_per_move(cx_dict, "ENDORSE")
count_tag_per_move(cx_dict, "PRONOUNCE")
count_tag_per_move(cx_dict, "ATTRIBUTE")
count_tag_per_move(cx_dict, "ENTERTAIN")
count_tag_per_move(cx_dict, "MONOGLOSS")
count_tag_per_move(cx_dict, "JUSTIFY")
