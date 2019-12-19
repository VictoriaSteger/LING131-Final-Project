import spacy

nlp = spacy.load('en_core_web_sm')


def listofPeople(murdery_sents):
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
                            to_append = t[:-1] + '_' + to_append
                            break
                    ents.append(to_append)
    return ents
