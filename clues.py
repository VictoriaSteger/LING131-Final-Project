''' made some changes to ner so that I could return the list
I uploaded it as ner2
'''
import ner2

def clues(murdery_sents):
    
    people = list(set(ner2.listofPeople(murdery_sents)))
    
    new_people = []
    
    for i in people:
        if str(i) not in new_people:
            new_people.append(str(i))
    
    new_murder = []
    
    for i in new_people:
        for j in murdery_sents:
            k = j[1].split()
            if i in k:
                new_murder.append(j[1])
    return new_murder