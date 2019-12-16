import os
import time                           #only using this for testing purposes, can remove when submitting
import preprocessing
import nltk
import clues

#DOES SOMEONE HAVE A BETTER WAY TO READ THIS FILE?  ONE WITHOUT ALL THE SLASHES?

#killer: Mr. Alfred Inglethorp
#dead person: Mrs. Inglethorp

if __name__ == '__main__':
    #input = input("What file should I use?")
    input = "./The Mysterious Affair at Styles - Agatha Christie.txt"
    #input = "./test.txt"

    # open supplied file and get contents
    if os.path.isfile(input):
        file = open(input, 'r')
        text = file.read()
        file.close()
    else:
        print("Invalid file.")
        quit()
            
    
    #two options, get 122 sentences with stemming, 113 with lemmatizing
    # sent_words, sentences = preprocessing.stem_sentences(text)
    sent_words, sentences = preprocessing.lemma_sentences(text)

    #get a list of words from the text related to death/murder
    death_words = preprocessing.murder_words(text)
    
    #get a list of sentences and context for death/murder words
    murdery_sents = preprocessing.murder_sents(sent_words, sentences, death_words)
    
    '''for i in murdery_sents:
        if "murderer" in i:
            print(i)'''
    
    #print(len(murdery_sents))
    x = clues.clues(murdery_sents)
    for i in x:
        print(i)