import pandas as pd
import random 


######## From Abhishek Jana https://github.com/abhishek-jana/Disaster-Response-Pipelines
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download(['omw-1.4','punkt', 'wordnet', 'averaged_perceptron_tagger','stopwords'])
from sqlalchemy import create_engine
from sklearn.base import BaseEstimator, TransformerMixin
import joblib

# model tokenizer, verb and noun extractors
def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens
class StartingVerbExtractor(BaseEstimator, TransformerMixin):

    # Custom transformer to extract starting verb
    def starting_verb(self, text):
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            pos_tags = nltk.pos_tag(tokenize(sentence))
            first_word, first_tag = pos_tags[0]
            if first_tag in ['VB', 'VBP'] or first_word == 'RT':
                return True
        return False

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.starting_verb)
        return pd.DataFrame(X_tagged)

class StartingNounExtractor(BaseEstimator, TransformerMixin):

    # Custom transformer to extract starting Noun
    def starting_noun(self, text):
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            pos_tags = nltk.pos_tag(tokenize(sentence))
            first_word, first_tag = pos_tags[0]
            if first_tag in ['NN', 'NNS', 'NNP', 'NNPS'] or first_word == 'RT':
                return True
        return False

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.starting_noun)
        return pd.DataFrame(X_tagged)

########

class Classifier():
    def __init__(self) -> None:
        engine = create_engine('sqlite:///classifier_model/data/DisasterResponse.db')
        self.datadf = pd.read_sql_table('DisasterResponseTable', engine)
        self.categories = self.datadf.columns[4:]
        self.rowcount = len(self.datadf.index)
        self.model = joblib.load("classifier_model/model/classifier.pkl")

    def classifyraw(self,query:str):
        return self.model.predict([query])[0]

    def classify(self,query:str):
        return pd.Series(self.classifyraw(query),index=self.categories)

    def random_message(self):
        randomint=random.randint(0,self.rowcount)
        return self.datadf["message"][randomint]
    