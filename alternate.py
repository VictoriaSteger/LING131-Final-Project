import clues
import ner2

# This entire file is to check alternate ways of getting a result, and see
# how they compare to our main project. There's some redundancy in this code,
# but there are also just enough differences that I don't want to mess with it.

# I named this "detective", but what it really is is "reoccuring characters
# that we know aren't the killer"
detective = ["Holmes", "Poirot", "Watson", "Lestrade", "Japs", "Hudson",
             "Hastings"]


# this method only looks at sentences with the word "murder" in them
def murder_she_wrote(murdery_sents, text):
    people = ner2.listofPeople(murdery_sents)
    x = clues.clues(murdery_sents)
    test = []
    # filters the sentences with the word "murder"
    for i in x:
        i = list(i)
        if "murder" in i:
            test.append(i)

    # list of people that aren't detectives
    suspects = little_grey_cells(people)
    # get the person mentioned the most
    most_wanted = fbi_most_wanted(suspects, text)
    return most_wanted


def accusations(murdery_sents, text):
    people = ner2.listofPeople(murdery_sents)
    accuse = []
    for line in murdery_sents:
        for i in detective:
            for j in line:
                if i in j:
                    accuse.append(line)
    # list of people that aren't detectives
    suspects = little_grey_cells(people)
    # get the person mentioned the most
    most_wanted = fbi_most_wanted(suspects, text)
    return most_wanted


def known_victim(murdery_sents, text, victim):
    accuse = []
    for line in murdery_sents:
        for i in detective:
            for j in line:
                if i in j:
                    accuse.append(line)
    # list of people
    people = ner2.listofPeople(murdery_sents)
    # list of people that aren't detectives
    suspects = little_grey_cells(people)
    # modification of the fbi_most_wanted
    most_wanted = ""
    wanted = 0
    for i in suspects:
        if text.count(i) > wanted and i != victim:
            wanted = text.count(i)
            most_wanted = i
    return most_wanted


# filters the people list to rule out the detectives
def little_grey_cells(people):
    suspects = []
    for i in people:
        if i not in detective:
            suspects.append(i)
    # removes dupilcate names from the list
    for i in suspects:
        for j in suspects:
            if i in j and i != j:
                suspects.remove(i)


# decides which character is mentioned the most
def fbi_most_wanted(suspects, text):
    most_wanted = ""
    wanted = 0
    for i in suspects:
        if text.count(i) > wanted:
            wanted = text.count(i)
            most_wanted = i
    return most_wanted
