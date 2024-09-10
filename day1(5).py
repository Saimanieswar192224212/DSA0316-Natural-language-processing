'''import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
porter = PorterStemmer()
words = ["running", "jumps", "easily", "fairly", "studies", "studying"]
stemmed_words = [porter.stem(word) for word in words]
for word, stemmed in zip(words, stemmed_words):
    print(f"Original: {word}, Stemmed: {stemmed}")'''
    
import nltk
nltk.download('treebank')
train_data = nltk.corpus.treebank.tagged_sents()[:100]
tagger = nltk.DefaultTagger('NN')
tokens = nltk.word_tokenize("The quick fox.")
print(tagger.tag(tokens))