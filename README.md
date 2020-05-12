# CS525 Final Project




## docTvec.py & result.py
The docTvec.py is the training program of doc2vec model, and result.py is for prediction Gensim, Numpy, and Pandas are required to run the programs. <br />
pip install numpy <br />
pip install pandas <br />
pip install gensim <br />

File paperFrame2.csv need to be in the same folder with docTvec.py and result.py. <br />
PaperFrame2.csv can be downloaded at  <br />
https://drive.google.com/file/d/11gE-qSoao3sjkhXGevGEEWasgecaN0rG/view?usp=sharing <br />


## BERT
To run this, first download the dataset from cord-19 challenge from https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge <br />
Then unzip it. <br />
Change the path in dataprocessingBERT.py to where you downloaded the file in your system. <br />
Run dataprocessingBERT.py. <br />
It will write a csv file in the same location where you ran the previous code. <br />
Before the next step, install torch version 1.6, cdqa, pandas and ast. Note: install torch before cdqa as it is dependent on it. <br />
Finally, run BERTcdqa in the same location as the csv file. Output are the results required. <br />
Note: The results may slightly vary as the dataset is updated frequently. <br />
