import spacy

nlp = spacy.load('en_core_web_sm')

def listofPeople(murdery_sents):
    relevant = []
    for tup in murdery_sents:
        for i in range(1,6):
            relevant.append(tup[i])
    
    doc = nlp(' '.join(relevant))
    
    people = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            people.append(ent)
    
    return people