import nltk
import math
from nltk.stem import WordNetLemmatizer
from collections import Counter
lemmatizer = WordNetLemmatizer()

deniery = {"n't", "not", "would", "should", "could"}
main_char = ''


def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


def murder_aggregate(text, m_words, entities):
    global main_char
    print("-----------------------SPOILERS--------------------------")
    suspicious_events = list()
    murderers = list()
    victims = list()
    half = math.floor(len(text) / (3/4))
    # main_char = most_frequent(entities)
    print(main_char)
    for wd, pre1, pre2, s, post1, post2 in text:
        targets = set()
        context = (pre1+" "+pre2+" "+s+" "+post1+" "+post2).lower()
        context2 = (pre2+" "+s+" "+post1).lower()
        targets = {e for e in entities if e in context}
        tmp = them_rip(context, wd, targets)
        if tmp[0] != '' or '' != tmp[1]:
            murderers.append(tmp[0])
            victims.append(tmp[1])

    print("SUSPECTS:", murderers)
    print("POTENTIAL VICTIMS:", victims)
    mfm = most_frequent(murderers)
    mfv = most_frequent(victims)
    print("MOST LIKELY KILLER:", mfm)
    print("MOST LIKELY VICTIM:", mfv)
    return (mfm, mfv)


def processing():
    pass


def them_rip(sent, m, entities):
    global main_char
    targets = set()
    sls = nltk.pos_tag([w.lower() for w in nltk.word_tokenize(sent)])
    bigrams = list(nltk.bigrams([w for w, t in sls]))
    tuples = ('', '')
    PROa = False
    PROt = False

    def minifunc(w):
        a = lemmatizer.lemmatize(w, 'v') == m
        b = lemmatizer.lemmatize(w, 'n') == m
        c = lemmatizer.lemmatize(w, 'a') == m
        return a or b or c
    m0 = [(w, t) for (w, t) in sls if minifunc(w)][0]  # hopefully only 1

    pre = sls[:sls.index(m0)][::-1]
    post = sls[sls.index(m0)+1:]
    if len(pre) == 0 or len(post) == 0:
        return tuples
    if pre[0][0] not in deniery:
        agent = ''
        theme = ''

        def bool_check(w, t, b):
            interstitials = {(w, "said"), ("said", w)}
            for i in interstitials:
                if i in bigrams:
                    return False
            return (w in " ".join(entities)) and len(w) > 2 and w != main_char
        try:  # exception when there are no target agents or themes
            agent = [w for w, t in pre if bool_check(w, t, True)][0]
            theme = [w for w, t in post if bool_check(w, t, True)][0]
            if ("by", theme) in bigrams:  # check for passive construction, then reverse tuple
                tuples = (theme, agent)
            else:
                tuples = (agent, theme)
        except:
            pass
    return tuples


ex_actors = ['john', 'thomas', 'larry', 'moe', 'curly', 'sam', 'jill',
             'jamal', 'jackson', 'janet', 'latoya']
ex_verbs = ['kill', 'poison', 'stab', 'break', 'murder', 'destroy']
s1 = "When larry killed Moe i didn't know what I would do until CurLY was stabbed by larry too"
s2 = "jackson hated,,,, to hurt Latoya like this"
s3 = "Thomas poisoned Curly with Jamal's ...pills"
s4 = "John broke Thomas' heart"
s5 = "Who killed Moe?"
s6 = "Jerry distract distract distract repeated destroyed by Chen"
s7 = "Jill was destroyed by Sam's bomb"
s8 = "I stabbed him"
s9 = "There's no way Thomas would kill Janet, he broke her heart, but Thomas would not kill Janet"
s10 = "Thomas didn't kill Larry, Moe killed larry"
tex = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
'''
j = murder_aggregate(tex, ex_verbs,ex_actors)
print(j)'''
