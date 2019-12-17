import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import operator


# deprecated, we're now using the lemma one
def stem_sentences(text):
    ps = PorterStemmer()

    # list of each sentence in the text
    sentences = nltk.sent_tokenize(str(text))

    # makes a list of lists.  each entry has the the stems of all unique words in the sentence.
    sent_words = []
    for sent in sentences:
        unique_words = set(nltk.word_tokenize(sent))
        stems = []
        for word in unique_words:
            stems.append(ps.stem(word.lower()))
        sent_words.append(stems)

    return sent_words, sentences


# lemmatizes important words in the text
def lemma_sentences(text):
    lemmatizer = WordNetLemmatizer()

    # list of each sentence in the text
    sentences = nltk.sent_tokenize(text)

    # list of lists with lemmas of each sentence's unique adjectives, nouns, verbs, and adverbs
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
                # WordNet doesn't have modals, but we want to know when they're in a sentence
                stems.append(word)
        sent_words.append(stems)

    return sent_words, sentences


# deprecated, we're now using improved_murder_words.
def murder_words(text):
    # die and dying both included because of v/a behavior of lemmatizer
    return ['murder', 'kill', 'die', 'dying', 'poison', 'murderer']


# returns a lemmatized list of words within 3 WordNet steps of 'murder' or 'dying'
def improved_murder_words(text):
    noun = wordnet.synsets('murder', 'n')[0]
    verb = wordnet.synsets('murder', 'v')[0]
    adj = wordnet.synsets('dying', 'a')[0]

    lemmatizer = WordNetLemmatizer()

    tagged_unique_words = set(nltk.pos_tag(nltk.word_tokenize(text)))
    words = []
    for (word, pos) in tagged_unique_words:
        min_num = 100
        word_lemmatized = ''
        if(pos[0] == 'J'):
            synset = wordnet.synsets(word, 'a')
            word_lemmatized = lemmatizer.lemmatize(word.lower(), 'a')
            for meaning in synset:
                num = adj.shortest_path_distance(meaning)
                if(num is not None):
                    min_num = min(min_num, num)
        elif((pos == 'NN') or (pos == 'NNS')):
            synset = wordnet.synsets(word, 'n')
            word_lemmatized = lemmatizer.lemmatize(word.lower(), 'n')
            for meaning in synset:
                num = noun.shortest_path_distance(meaning)
                if(num is not None):
                    min_num = min(min_num, num)
        elif(pos[0] == 'V'):
            synset = wordnet.synsets(word, 'v')
            word_lemmatized = lemmatizer.lemmatize(word.lower(), 'v')
            for meaning in synset:
                num = verb.shortest_path_distance(meaning)
                if(num is not None):
                    min_num = min(min_num, num)

        words.append((word_lemmatized, min_num))

    words = sorted(words, key=operator.itemgetter(1))

    # keeps any words with a distance of 3 or less from the targets
    murder_words = []
    for (word, num) in words:
        if num < 4:
            murder_words.append(word)

    return murder_words


# makes list of the relevant murder word, the sentence with it, and two sentences before and after
# wraps around end of file if finds murder word at start or end
def murder_sents(sent_words, sentences, death_words):
    murdery_sentences = []
    i = 0
    while i < len(sent_words):
        for word in sent_words[i]:
            if (word in death_words):
                # this works because sent_words and sentences have the same sentence indexes
                murdery_sentences.append((word, sentences[i-2], sentences[i-1],
                                          sentences[i], sentences[i+1], sentences[i+2]))
                continue
        i += 1

    return murdery_sentences
