import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

def stem_sentences(text):
    ps = PorterStemmer()
    
    #list of each sentence in the text
    sentences = nltk.sent_tokenize(str(text))
    
    #makes a list of lists.  each entry has the the stems of all unique words in the sentence.
    sent_words = []
    for sent in sentences:
        unique_words = set(nltk.word_tokenize(sent))
        stems = []
        for word in unique_words:
            stems.append(ps.stem(word.lower()))
        sent_words.append(stems)
        
    return sent_words, sentences


def lemma_sentences(text):
    lemmatizer = WordNetLemmatizer()
    
    #list of each sentence in the text
    sentences = nltk.sent_tokenize(text)

    #makes a list of lists.  each entry has the the lemmas of all unique adjectives, nouns, verbs, and adverbs in the sentence.
    sent_words = []
    for sent in sentences:
        unique_words = set(nltk.pos_tag(nltk.word_tokenize(sent)))
        
        stems = []
        for (word, pos) in unique_words:
            if(pos[0] == 'J'):
                stems.append(lemmatizer.lemmatize(word.lower(), 'a'))
            elif(pos[0] == 'N'):
                stems.append(lemmatizer.lemmatize(word.lower(), 'n'))
            elif(pos[0] == 'V'):
                stems.append(lemmatizer.lemmatize(word.lower(), 'v'))
            elif(pos[0] == 'R'):
                stems.append(lemmatizer.lemmatize(word.lower(), 'r'))
            elif(pos == 'MD'):
                #WordNet doesn't have modals, but we want to know when they're in a sentence
                stems.append(word)
        sent_words.append(stems)

    return sent_words, sentences


#a list of common death words.  will attempt to do this more cleverly later.    
def murder_words(text):
    #die and dying both included because of v/a behavior of lemmatizer
    return ['murder','kill','die','dying','poison', 'murderer']

    
#might have issues if kill words in title, elsewise gutenburg extra at start and end should mean this is safe
#makes a list where each entry has the relevant murder word, the two sentences before it, the sentence with it, and the two sentences after it   
def murder_sents(sent_words, sentences, death_words):

    #a list of hypotheticals that mean we don't want the death words
    hypotheticals = ['might', 'will', 'could', 'can', 'may', 'would', 'shall', 'should', 'must']

    murdery_sentences = []
    i = 0
    while i < len(sent_words):
        for word in sent_words[i]:
            if (word in death_words) and (word not in hypotheticals):
                #this works because sent_words and sentences have the same sentence indexes
                murdery_sentences.append((word, sentences[i-2], sentences[i-1], sentences[i], sentences[i+1], sentences[i+2]))
                continue
        i += 1
        
    return murdery_sentences