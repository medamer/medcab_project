"""
Preditive model for predicting best strains to match input variables
"""

# Imports:
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle
import en_core_web_sm
from spacy import load

df = pd.read_csv('data/cannabis_new.csv')

nlp = en_core_web_sm.load()

def tokenizer(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if ((token.is_stop == False) and
    (token.is_punct == False)) and (token.pos_ != 'PRON')]

# Build the model:
model = TfidfVectorizer(stop_words = 'english',
                        ngram_range = (1,2),
                        max_df = .95,
                        min_df = 3,
                        tokenizer = tokenizer)

# Fit the model:
dtm = model.fit_transform(df['Effects'])

# Get features:
dtm = pd.DataFrame(dtm.todense(), columns = model.get_feature_names())
nn = NearestNeighbors(n_neighbors = 5, algorithm = 'kd_tree')
nn.fit(dtm)

# Pickle trained model:
filename = 'model.pkl'
model_pkl = open(filename, 'wb') # Open the file to save as pkl file
pickle.dump(nn, model_pkl)
model_pkl.close() # Close the pickle instances

def my_prediction(user_input):
    model_pkl = open(filename, 'rb')
    nn2 = pickle.load(model_pkl)
    sample = [user_input]
    vec = model.transform(sample)
    dense = vec.todense()
    similar = nn2.kneighbors(dense, return_distance = False)
    similar.T

    output = []
    for i in range(5):
        elem = similar[0][i]
        output.append(elem)

    return output
