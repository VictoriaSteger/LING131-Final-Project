import os
import preprocessing
import nltk
import clues
import them_roles
import ner2
import alternate 

#killer: Culverton Smith
#dead person: Victor Savage

if __name__ == '__main__':
    #input = input("What file should I use?")
    input = "./The Mysterious Affair at Styles - Agatha Christie.txt"

    # open supplied file and get contents
    if os.path.isfile(input):
        file = open(input, 'r')
        text = file.read()
        file.close()
    else:
        print("Invalid file.")
        quit()

    # get list of sentences in text and list of lists of lemmatized important words for sentences
    sent_words, sentences = preprocessing.lemma_sentences(text)

    # get a list of words from the text related to death/murder
    death_words = preprocessing.improved_murder_words(text)

    # get a list of sentences and context for death/murder words
    murdery_sents = preprocessing.murder_sents(sent_words, sentences, death_words)

    #not currently used by Mike's method
    cl = clues.clues(murdery_sents)
    #for i in x:
    #    print(i)
    
    people = ner2.listofPeople(murdery_sents)
    
    new_people = []
    for i in people:
        if str(i) not in new_people:
            new_people.append(str(i).lower())

    print(cl)
    them_roles.murder_aggregate(cl, death_words, new_people)
