import random
import preprocessing
import clues
import them_roles
import ner2

def testing():
    tested = 0
    kill_acc = 0
    vic_acc = 0

    rand_kill_acc = 0
    rand_vic_acc = 0

    with open("answers-story,killer,victim.txt") as file:
        for line in file:
            tested += 1

            f, s, t = line.split(",")
            # To discard newline character
            t = t[:-1]

            with open("data/" + f + ".txt") as story:
                text = story.read()

                sent_words, sentences = preprocessing.lemma_sentences(text)

                # get a list of words from the text related to death/murder
                death_words = preprocessing.improved_murder_words(text)

            # get a list of sentences and context for death/murder words
            murdery_sents = preprocessing.murder_sents(sent_words, sentences, death_words)

            # filter murdery_sents to only keep entries with a character name in one of the sentences
            cl = clues.clues(murdery_sents)

            # get a list of people in the story
            people = ner2.listofPeople(murdery_sents)

            # change the list from objects to strings
            new_people = []
            for i in people:
                if str(i) not in new_people:
                    new_people.append(str(i).lower())

            # attempt to predict the murderer and victim
            kill, vic = them_roles.murder_aggregate(cl, death_words, new_people)
            rkill, rvic = random.sample(new_people, 2)

            print("Story:", f)
            print("\tReal killer:", s)
            print("\tPredicted killer:", kill)
            print("\tReal victim:", t)
            print("\tPredicted victim:", vic)

            if s in kill or kill in s:
                kill_acc += 1
            if t in vic or vic in t:
                vic_acc += 1

            if rkill in kill or kill in rkill:
                rand_kill_acc += 1
            if rvic in vic or vic in rvic:
                rand_vic_acc += 1

    print()
    print("Killer prediction accuracy:", kill_acc/tested)
    print("\tRandom chance accuracy:", rand_kill_acc/tested)
    print("Victim prediction accuracy:", vic_acc / tested)
    print("\tRandom chance accuracy:", rand_vic_acc / tested)

if __name__ == "__main__":
    testing()