import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
text = "Hello, Students Welcome to SSE."
tokens = word_tokenize(text)
print("Word Tokens:")
print(tokens)