import os
import preprocessing
import nltk
import clues
import alternate

#killer: Culverton Smith
#dead person: Victor Savage

if __name__ == '__main__':
    #input = input("What file should I use?")
    input = "./The Adventure of the Dying Detective.txt"

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

    '''x = clues.clues(murdery_sents)
    for i in x:
        print(i)
        
    z = alternate.accusations(murdery_sents, text)
    print(z)
    y = alternate.known_victim(murdery_sents, text, "Victor Savage")
    print(y)'''
    
    a = alternate.murder_she_wrote(murdery_sents, text)
    print(a)
    
'''look for accusations, and give more weight to ones done by the detective?
create test files to check if we recieve the correct killer
See if we can get better than random chance
Write-up: what we looked at, the differences between the two, the accuracy rate
for each author, show the results of the tests
Write about the heuristics
Clean up readme

To Do:
    Write up bullshit methods
    ? - one that filters if the detective said something
    ? - one that only contains "murder" or "murderer" in it
    
    Edit the google doc
    
    Write the google doc for CompSemantics
'''