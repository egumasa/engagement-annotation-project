
import re
import os
import glob
from bs4 import BeautifulSoup as BS
import lxml

import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from spacy.util import compile_infix_regex

def custom_tokenizer(nlp):
    infixes = (
        LIST_ELLIPSES
        + LIST_ICONS
        + [
            r"(?<=[0-9])[+\-\*^](?=[0-9-])",
            r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
                al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
            ),
            r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
            #r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
            r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
        ]
    )

    infix_re = compile_infix_regex(infixes)

    return Tokenizer(nlp.vocab, prefix_search=nlp.tokenizer.prefix_search,
                                suffix_search=nlp.tokenizer.suffix_search,
                                infix_finditer=infix_re.finditer,
                                token_match=nlp.tokenizer.token_match,
                                rules=nlp.Defaults.tokenizer_exceptions)


nlp = spacy.load('en_core_web_sm')
nlp.tokenizer = custom_tokenizer(nlp)
print([(t.text, t.pos_) for t in nlp("It's 1.50, up-scaled haven't")])



def doc2conll(doc):
	
	engagement = None

	holder = []
	for t in doc:
		match = re.match(r'class="(.*)', t.text)
		if t.text in ['/engmt']:
			engagement = None
		elif match:
			engagement = match.group(1)
		elif t.text in ["<", ">", 'engmt']:
			continue
		elif t.text == '"':
			try:
				next_token = t.nbor().text
				if next_token == ">":
					continue
			except IndexError:
				pass
		else:
			holder.append( (t, engagement) )
	return(holder)

def soup2sentlist(soup):
	sents = []
	for s in soup.find_all('s'):
		id_ = s['id']
		tunit = s['tunit']
		raw_text = s.text.strip()
		
		## strip annotation
		annotation = str(s)
		p1 = r'\<s engmt_main.*?\>'
		p2 = r'\</s\>'
		annotation = re.sub(p1, "", annotation)
		annotation = re.sub(p2, "", annotation)
		
		#print(anno_list)
		#print('\n')
		doc = nlp(annotation.strip())
		res = doc2conll(doc)
		sents.append( (id_, raw_text, res) )
	return(sents)
 

def output(sentences: list, dir_, outname):
	with open('{}/{}.tsv'.format(dir_, outname), 'w') as f:
		
		for id_, raw_text, conll in sentences:
			f.write("#Text={}\n".format(raw_text))
			f.write("#id={}\n".format(id_))
			
			for token, tag in conll:
				if tag == None: tag = "_"
				f.write("{}\t{}\n".format(token, tag))
			f.write('\n')


sample = open("data/xml/ICNALE_1.xml").read()
sample = sample.replace("<engmt", '<engmt class')
sample = sample.replace("\">", "\"> ")
sample = sample.replace("</eng", " </eng")

soup = BS(sample)


output(sents, 'data/conllu', 'test')

filenames = glob.glob("data/xml/*.xml")
for filename in filenames:
	txt = open(filename).read()
	txt = txt.replace("<engmt", '<engmt class')
	txt = txt.replace("\">", "\"> ")
	txt = txt.replace("</eng", " </eng")
	txt = txt.replace("disclaim:", "")
	txt = txt.replace("proclaim:", "")
	
	soup = BS(txt)
	sents = soup2sentlist(soup)
	output(sents, 'data/conllu', os.path.split(filename)[-1])

