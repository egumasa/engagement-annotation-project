from scripts.matching_webannotsv import tsv2json
from scripts.json2accuracy import json2dict
from scripts.sorting_for_error_analysis import write_disagreed_conll

annotator1 = "ME"
annotator2 = "ALM"
# annotator2 = "RW"

batch_letter = "E"
regex_fileno = "*"  #e.g. [5-9]

tsv2json(start=0,
         end=10,
         batch_letter=batch_letter,
         anno_name1=annotator1,
         anno_name2=annotator2)

json2dict(annotator1, annotator2, batch_letter, regex_fileno=regex_fileno)

write_disagreed_conll(annotator1, annotator2, batch_letter, regex_fileno)

# batch

batch_letter = "E"
regex_fileno = "*"  #e.g. [5-9]

batches = ["A", "B", "C", "D", "E"]

for batch_letter in batches:
    tsv2json(start=0,
             end=10,
             batch_letter=batch_letter,
             anno_name1=annotator1,
             anno_name2=annotator2)

    json2dict(annotator1, annotator2, batch_letter, regex_fileno=regex_fileno)

    write_disagreed_conll(annotator1,
                          annotator2,
                          batch_letter,
                          output_letter='combined',
                          regex_fileno=regex_fileno)


