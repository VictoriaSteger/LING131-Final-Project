import spacy
import preprocessing

nlp = spacy.load('en_core_web_sm')

with open("./Strong Poison - Dorothy L. Sayers.txt", encoding="utf8") as file:
    text = str(file.read())

sent_words, sentences = preprocessing.lemma_sentences(text)

death_words = preprocessing.murder_words(text)

murdery_sents = preprocessing.murder_sents(sent_words, sentences, death_words)

relevant = []
for tup in murdery_sents:
    for i in range(1,6):
        relevant.append(tup[i])

doc = nlp(' '.join(relevant))

for ent in doc.ents:
    if ent.label_ == "PERSON":
        print(ent)
