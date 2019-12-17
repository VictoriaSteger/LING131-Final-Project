import spacy
import preprocessing
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

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
                to_append = ent.text
                if ent.start_char > 3 and tup[i][(ent.start_char-4):(ent.start_char)] == "Mr. ":
                    to_append = "Mr. " + to_append
                elif ent.start_char > 4 and tup[i][(ent.start_char-5):(ent.start_char)] == "Mrs. ":
                    to_append = "Mrs. " + to_append

                ents.append(to_append)

counts = FreqDist(ents)
print(counts.most_common())