import json
import glob
import re
import csv
from typing import Dict

filenames = glob.glob(
    'construction_analysis/results/construction_freq_FRAGMENT.json')


def tag_collector(input: dict, key: str) -> dict:
    return input[key]


def reformatter(target: dict, freq_dict: dict, label: str):

    for tag, freq in freq_dict.items():
        if tag not in target:
            target[tag] = {}

        target[tag][label] = freq


def process_file_by_tag(filenames: list,
                        feature_key: str) -> tuple[dict, dict]:
    labels = {}
    holder = {}
    for file in filenames:

        match = re.match(r'.*construction_freq_(.*)\.json', file)
        label = match.group(1)
        if label not in labels:
            labels[label] = None

        with open(file, 'r') as f:
            cx_freq = json.load(f)

        tag_dict = tag_collector(cx_freq, feature_key)
        reformatter(holder, tag_dict, label)
    return ((labels, holder))


def write_csv(tag_dict: dict,
              labels: dict,
              outputname='construction_analysis/results/feature_test.csv'):

    with open(outputname, 'w') as outf:
        csv_writer = csv.writer(outf, delimiter=",")

        labels = list(labels.keys())
        labels.sort()

        csv_writer.writerow(['TAG'] + labels)

        for tag, freq_dict in tag_dict.items():
            freq_holder = [tag]
            for label in labels:
                if label in freq_dict:
                    freq_holder.append(str(freq_dict[label]))
                else:
                    freq_holder.append("0")
            csv_writer.writerow(freq_holder)


feature_list = "dep\tpos\ttag\tchild_deps\tchild_seq\thead_dep".split('\t')

for x in feature_list:

    labels, dict = process_file_by_tag(filenames, x)
    write_csv(
        dict,
        labels,
        outputname='construction_analysis/results/feature_{}.csv'.format(x))
