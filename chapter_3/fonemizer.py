import phonemizer as pm


texts = [
    "Das ist ein kurzer deutscher Text",
    "Das ist ein langer deutscher Text",
    "Das ist ein sehr langer deutscher Text",
]

for text in texts:
    phonemes = pm.phonemize(text, language="de")
    print(phonemes)
