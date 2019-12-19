''' made some changes to ner so that I could return the list
I uploaded it as ner2
'''
import ner2
from nltk.tokenize import RegexpTokenizer


def clues(murdery_sents):

    # calls ner2, gives it the sentences with murdery words in it
    # and gets back a list of people
    people = list(set(ner2.listofPeople(murdery_sents)))

    # initializes list of strings
    new_people = []

    # goes through and changes the objects into strings
    for i in people:
        if str(i) not in new_people:
            new_people.append(str(i))

    # initializes new list of sentences
    new_murder = []

    # this was used earlier development cycle - leaving it in in case we need
    # it later
    # tokenizer = RegexpTokenizer(r'\w+')

    # loops through the sentences and checks if the sentences contain a name
    for i in new_people:
        for j in murdery_sents:
            for l in j:
                # k = tokenizer.tokenize(l)
                if i in l:
                    new_murder.append(j)
                # there were some problems originally getting Mr and Mrs to
                # register - there shouldn't be any problems, but this is
                # rather safe than sorry
                elif "Mr." in l or "Mrs." in l:
                    new_murder.append(j)

    return list(new_murder)
