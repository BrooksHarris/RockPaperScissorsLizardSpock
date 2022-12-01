#pip install --user -U nltk
#import nltk
#nltk.download()
from nltk.corpus import wordnet as wn
all_nouns = [word for synset in wn.all_synsets('n') for word in synset.lemma_names()]
# all_nouns is a list of length 146,347