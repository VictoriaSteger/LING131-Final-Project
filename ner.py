import spacy
import preprocessing
from nltk.probability import FreqDist

nlp = spacy.load('en_core_web_sm')

with open("./The Mysterious Affair at Styles - Agatha Christie.txt", encoding="utf8") as file:
    text = str(file.read())

sent_words, sentences = preprocessing.lemma_sentences(text)

death_words = preprocessing.murder_words(text)

murdery_sents = preprocessing.murder_sents(sent_words, sentences, death_words)

ents = []

for tup in murdery_sents:
    for i in range(1,6):
        doc = nlp(tup[i])
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                ents.append(ent.text)

counts = FreqDist(ents)
print(counts.most_common())