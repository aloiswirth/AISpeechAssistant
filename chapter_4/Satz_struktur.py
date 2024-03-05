# POS Tagging und Visaualisierung der Wortbeziehungen eines Satzes

import spacy
from spacy import displacy

nlp = spacy.load("de_core_news_sm")
doc = nlp("Die schnelle braune Füchsin springt über den faulen Hund.")
displacy.serve(doc, style="dep", auto_select_port=True)
doc = nlp("Goldfische sind pflegeleicht.")
displacy.serve(doc, style="dep", auto_select_port=True)

# print(spacy.explain('sb'))
