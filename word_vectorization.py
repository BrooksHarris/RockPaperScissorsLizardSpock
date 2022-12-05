import gensim

# WARNING: THE LINE OF CODE BELOW WILL DOWNLOAD 3.5GB OF DATA
# Load Google's pre-trained Word2Vec model.
model = gensim.models.KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)

#fill below with words to create associations
input_array = []
input_array = [x.lower() for x in input_array]
input_vectors = [model[x] for x in input_array]
greatest_distance = [max([model.similartity(x,a) for x in input_array]) for a in input_array]

print(greatest_distance)

b=[]
w=[]

