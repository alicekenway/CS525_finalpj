import numpy as np 
import pandas as pd 

import gensim
from gensim.utils import lemmatize
from gensim.parsing.preprocessing import STOPWORDS
from gensim.parsing.porter import PorterStemmer

df = pd.read_csv('paperFrame2.csv')


body_text = df.body_text
index = df.index

p = PorterStemmer()


stopset = set([
    'doi', 'preprint', 'copyright', 'org', 'https', 'et', 'al', 'author', 'figure', 'table',
    'rights', 'reserved', 'permission', 'use', 'used', 'using', 'biorxiv', 'medrxiv', 'license', 'fig', 'fig.', 'al.', 'Elsevier', 'PMC', 'CZI',
    '-PRON-', 'usually',
    r'\usepackage{amsbsy', r'\usepackage{amsfonts', r'\usepackage{mathrsfs', r'\usepackage{amssymb', r'\usepackage{wasysym',
    r'\setlength{\oddsidemargin}{-69pt',  r'\usepackage{upgreek', r'\documentclass[12pt]{minimal'
    ])
cStopwords = STOPWORDS.union(stopset)




def processing(body_text):
    

    for i, text in enumerate(body_text):
        tokens = []
        for item in gensim.parsing.preprocess_string(text):
            if item.lower() not in cStopwords:
                p.stem(item)
                tokens.append(item)
        yield gensim.models.doc2vec.TaggedDocument(tokens, [i])

documents = list(processing(body_text))
model = gensim.models.doc2vec.Doc2Vec(documents,dm=1, vector_size=50, min_count=10, dm_mean=1, epochs=50, seed=10, workers=6)
model.save("test_doc2vec.model")
