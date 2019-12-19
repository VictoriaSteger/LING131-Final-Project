import random
import preprocessing
import clues
import them_roles
import ner2

def testing():
    with open("answers-story,killer,victim.txt") as file:
        for line in file:
            f, s, t = line.split(",")

            print("doing", f)

            name = f + ".txt"

            sent_words, sentences = preprocessing.lemma_sentences(name)

            # get a list of words from the text related to death/murder
            death_words = preprocessing.improved_murder_words(name)

            # get a list of sentences and context for death/murder words
            murdery_sents = preprocessing.murder_sents(sent_words, sentences, death_words)

            # not currently used by Mike's method
            cl = clues.clues(murdery_sents)
            people = ner2.listofPeople(murdery_sents)

            new_people = []
            for i in people:
                if str(i) not in new_people:
                    new_people.append(str(i).lower())

            kill, vic = them_roles.murder_aggregate(cl, death_words, new_people)

            print("Story:", f)
            print("\tReal killer:", s)
            print("\tPredicted killer:", kill)
            print("\tReal victim:", t)
            print("\tPredicted victim:", vic)

def bad_detective(people):
    rand = random.randint(0,(len(people)))
    definitely_the_killer = people[rand]
    return definitely_the_killer

def red_herring_sucess_rate(killer, people):
    truth = 0
    for i in range(100):
        definitely_the_killer = bad_detective(people)
        if definitely_the_killer == killer:
            truth += 1
    result = truth/100
    return result

def actual_success_rate(outcomes, num_tested):
    return outcomes/num_tested


def formula():
    pass

if __name__ == "__main__":
    testing()