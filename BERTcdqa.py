
import pandas as pd
from ast import literal_eval

from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model, download_bnpp_data

download_bnpp_data(dir='./data/bnpp_newsroom_v1.1/')
download_model(model='bert-squad_1.1', dir='./models')

df = pd.read_csv('final.csv', converters={'paragraphs': literal_eval})
print(df.head())
df2 = filter_paragraphs(df)
print(df2.head())

cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib')
cdqa_pipeline.fit_retriever(df=df2)


queries = [
    'What is known about transmission, incubation, and environmental stability?',
    'What do we know about COVID-19 risk factors?',
    'What do we know about virus genetics, origin, and evolution?',
    'What do we know about vaccines and therapeutics?',
    'What do we know about non-pharmaceutical interventions?',
    'What has been published about medical care?',
    'What do we know about diagnostics and surveillance?'
    'What has been published about information sharing and inter-sectoral collaboration?',
    'What has been published about ethical and social science considerations?'
]
for query in queries:
    prediction = cdqa_pipeline.predict(query, n_predictions=20, retriever_score_weight=0.6)
    print('Query: {}'.format(query))
    # for x,y,z in zip(prediction[0][:-1],prediction[1][:-1],prediction[2][:-1]):
    print('Answer: ', str(prediction[0][-2]))
    print('Title: ', str(prediction[1][-2]))
    print('Paragraph: ', str(prediction[2][-2]))
    if query != queries[-1]:
        print('---------------Next Query---------------------')
