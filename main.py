import os
import preprocessing
import nltk
import clues
import them_roles
import ner2
import alternate

if __name__ == '__main__':
    path = "./data/"
    files_all = os.listdir(path)
    count = 0
    reviews = []

    while count < len(files_all):
        full_path = path + files_all[count]
        file = open(full_path, 'r')
        text = file.read()
        file.close()

        print("TESTING " + file.name)

        # get list of text sentences and list of lists of lemmatized important words for sentences
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
        them_roles.murder_aggregate(cl, death_words, new_people)

        count += 1
        print()
        print()
