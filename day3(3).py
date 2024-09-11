import nltk
from nltk import CFG
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> 'John' | 'Mary' | 'Bob'
    VP -> V NP
    V -> 'likes' | 'hates'
    NP -> 'pizza' | 'apple' | 'orange'
""")
# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)
# Get a sentence from the user
sentence = input("Enter a sentence: ")
tokens = sentence.split()
# Parse the sentence and print the parse tree(s)
for tree in parser.parse(tokens):
    tree.pretty_print()