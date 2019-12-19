''' made some changes to ner so that I could return the list
I uploaded it as ner2
'''
import ner2
from nltk.tokenize import RegexpTokenizer


def clues(murdery_sents):

    people = list(set(ner2.listofPeople(murdery_sents)))

    new_people = []

    for i in people:
        if str(i) not in new_people:
            new_people.append(str(i))

    new_murder = []

    tokenizer = RegexpTokenizer(r'\w+')

    for i in new_people:
        for j in murdery_sents:
            for l in j:
                k = tokenizer.tokenize(l)
                if i in l:
                    new_murder.append(j)
                elif "Mr." in k or "Mrs." in k:
                    new_murder.append(j)

    return list(new_murder)
