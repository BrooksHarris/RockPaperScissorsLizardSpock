#pip install --user -U nltk

#set variable below to true to initiate setup mode
setup = False
if setup:
    import nltk
    nltk.download()
else:
    from nltk.corpus import wordnet as wn
    all_nouns = [word for synset in wn.all_synsets('n') for word in synset.lemma_names()]
    # all_nouns is a list of length 146,347