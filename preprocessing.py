import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import operator

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
            elif(pos == 'MD'):
                #WordNet doesn't have modals, but we want to know when they're in a sentence
                stems.append(word)
        sent_words.append(stems)

    return sent_words, sentences


#a list of common death words.  will attempt to do this more cleverly later.    
def murder_words(text):
    #die and dying both included because of v/a behavior of lemmatizer
    return ['murder','kill','die','dying','poison', 'murderer']


#still probably want to lemma or stem these
#attempting to do murder_words more cleverly
def improved_murder_words(text):
    noun = wordnet.synsets('murder','n')[0]
    verb = wordnet.synsets('murder','v')[0]
    adj = wordnet.synsets('dying','a')[0]
    
    tagged_unique_words = set(nltk.pos_tag(nltk.word_tokenize(text)))
    words = []
    for (word, pos) in tagged_unique_words:
        min_num = 100
        if(pos[0] == 'J'):
            synset = wordnet.synsets(word,'a')
            for meaning in synset:
                num = adj.shortest_path_distance(meaning)
                if(num != None):
                    min_num = min(min_num, num)
        elif((pos == 'NN') or (pos == 'NNS')):
            synset = wordnet.synsets(word,'n')
            for meaning in synset:
                num = noun.shortest_path_distance(meaning)
                if(num != None):
                    min_num = min(min_num, num)
        elif(pos[0] == 'V'):
            synset = wordnet.synsets(word,'v')
            for meaning in synset:
                num = verb.shortest_path_distance(meaning)
                if(num != None):
                    min_num = min(min_num, num)
        words.append((word.lower(), min_num))
    
    words = sorted(words, key = operator.itemgetter(1))
    
    #keeps any words with a distance of 3 or less from the targets
    murder_words = []
    for (word, num) in words:
        if num < 4:
            murder_words.append(word)
    
    return murder_words

    
#wraps around end of file if finds murder word at start or end
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