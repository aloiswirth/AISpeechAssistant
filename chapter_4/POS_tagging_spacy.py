import spacy
from spacy import displacy

nlp = spacy.load("de_core_news_sm")
# doc = nlp("Goldfische sind pflegeleicht.")
doc = nlp("NLTK ist eine Bibliothek für die Sprachverarbeitung. Sie ist sehr mächtig.")
displacy.serve(doc, style="dep", port=5001)