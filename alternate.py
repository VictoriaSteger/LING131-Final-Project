import clues

detective = ["Holmes", "Poirot", "Watson", "Lestrade", "Japs", "Hudson", "Hastings"]

def murder_she_wrote(murdery_sents, text):
    x, people = clues.clues(murdery_sents)
    test = []
    for i in x:
        i = list(i)
        if "murder" in i:
            test.append(i)

    suspects = []
    for i in people:
        if i not in detective:
            suspects.append(i)
    for i in suspects:
        for j in suspects:
            if i in j and i != j:
                suspects.remove(i)
    most_wanted = ""
    wanted = 0
    for i in suspects:
        if text.count(i) > wanted:
            wanted = text.count(i)
            most_wanted = i
    return most_wanted

def accusations(murdery_sents, text):
    accuse = []
    for line in murdery_sents:
        for i in detective:
            for j in line:
                if i in j:
                    accuse.append(line)
    sents, people = clues.clues(accuse)
    suspects = []
    for i in people:
        if i not in detective:
            suspects.append(i)
    for i in suspects:
        for j in suspects:
            if i in j and i != j:
                suspects.remove(i)
    most_wanted = ""
    wanted = 0
    for i in suspects:
        if text.count(i) > wanted:
            wanted = text.count(i)
            most_wanted = i
    return most_wanted
    
def known_victim(murdery_sents, text, victim):
    accuse = []
    for line in murdery_sents:
        for i in detective:
            for j in line:
                if i in j:
                    accuse.append(line)
    sents, people = clues.clues(accuse)
    suspects = []
    for i in people:
        if i not in detective:
            suspects.append(i)
    for i in suspects:
        for j in suspects:
            if i in j and i != j:
                suspects.remove(i)
    most_wanted = ""
    wanted = 0
    for i in suspects:
        if text.count(i) > wanted and i != victim:
            wanted = text.count(i)
            most_wanted = i
    return most_wanted