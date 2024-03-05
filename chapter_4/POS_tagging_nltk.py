# Importing the NLTK library
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download("average_perceptron_tagger")

# Sample text
text = "NLTK is a powerful library for natural language processing."

# Performing PoS tagging
pos_tags = pos_tag(text.split())

# Displaying the PoS tagged result in separate lines
print("Original Text:")
print(text)

print("\nPoS Tagging Result:")
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")
