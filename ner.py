import spacy
import preprocessing
from nltk.probability import FreqDist

nlp = spacy.load('en_core_web_sm')

with open("./The Secret Adversary - Agatha Christie.txt", encoding="utf8") \
        as file:
    text = str(file.read())

sent_words, sentences = preprocessing.lemma_sentences(text)

death_words = preprocessing.murder_words(text)

murdery_sents = preprocessing.murder_sents(sent_words, sentences, death_words)

ents = []
titles = ['Master ', 'Mr. ', 'Miss ', 'Ms. ', 'Mrs. ', 'Sir ', 'Madam ',
          'Dame ', 'Lord ', 'Lady ', 'Doctor ', 'Dr. ', 'Professor ', 'Fr. ',
          'Pr. ', 'Br. ', 'Sr. ', 'Father ', 'Pastor ', 'Brother ', "Sister "]

for tup in murdery_sents:
    for i in range(1, len(tup)):
        doc = nlp(tup[i])
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                to_append = ent.text
                for t in titles:
                    if ent.start_char >= len(t) and tup[i][
                                (ent.start_char-len(t)):ent.start_char] == t:
                        to_append = t + to_append
                        break
                ents.append(to_append)

counts = FreqDist(ents)
print(counts.most_common())
