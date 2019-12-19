import nltk
import math
from nltk.stem import WordNetLemmatizer
from collections import Counter 
lemmatizer = WordNetLemmatizer()

'''
from nltk.corpus import verbnet as vn
from nltk.corpus import propbank as pb

x = vn.classids(lemma='poison')
print(x)
z = vn.vnclass(x[0])
print(z)
y=list()
for l in x:
    print(vn.pprint_themroles(l))
        #print(vn._get_semantics_within_frame(p))
print(vn.classids(lemma='dog'))
#print(vn.pprint_members(z))


import nlpnet
from nlpnet import srl

tagger = nlpnet.SRLTagger()
sent = "I think jane killed terry"
tagger.tag(sent)


import pntl.tools as tool
import pntl.cli as cli

cli.download_files()

x = "Jane killed Tom"
annotator = tool.Annotator()
annotator.get_senna_tag(x)



tagger = nlpnet.SRLTagger()
sent = "I think jane killed terry"
tagger.tag(sent)

from nltk.corpus import treebank

def agent_rip(sent):
    pass
def theme_rip(sent):
    pass

x = pb.instances()
print(x)
y = x[5000]
print(y)
tree = y.tree
print(y.predicate.select(tree))
for (argloc, argid) in y.arguments:
    print('%-10s %s' % (argid, argloc.select(tree).pformat(500)[:50]))
'''
deniery = {"n't","not","would","should","could"} 
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
    half = math.floor(len(text) /(3/4))
    #main_char = most_frequent(entities)
    print(main_char)
    for wd, pre1,pre2, s, post1, post2 in text:
        targets = set()
        context = (pre1+" "+pre2+" "+s+" "+post1+" "+post2).lower()
        context2 = (pre2+" "+s+" "+post1).lower()
        targets = {e for e in entities if e in context}
        tmp = them_rip(context,wd,targets)
        if tmp[0] != '' or '' != tmp[1] :
            murderers.append(tmp[0])
            victims.append(tmp[1])

    print("SUSPECTS:", murderers)
    print("POTENTIAL VICTIMS:", victims)
    mfm =most_frequent(murderers)
    mfv =most_frequent(victims)
    print("MOST LIKELY KILLER:", mfm)
    print("MOST LIKELY VICTIM:", mfv)
    return (mfm,mfv)

def processing():
    pass

def them_rip(sent, m, entities):
    global main_char
    targets = set()
    sls = nltk.pos_tag([w.lower() for w in nltk.word_tokenize(sent)])
    bigrams = list(nltk.bigrams([w for w,t in sls]))
    tuples = ('','')
    PROa = False
    PROt = False
    def minifunc(w):
        a = lemmatizer.lemmatize(w, 'v') == m
        b = lemmatizer.lemmatize(w, 'n') == m
        c = lemmatizer.lemmatize(w, 'a') == m
        return a or b or c
    m0 = [(w,t) for (w,t) in sls if minifunc(w)][0] #hopefully only 1
    
    pre = sls[:sls.index(m0)][::-1]
    post = sls[sls.index(m0)+1:]
    if len(pre) ==0 or len(post) == 0:
        return tuples
    if pre[0][0] not in deniery:
        agent = ''
        theme = ''
        def bool_check(w,t, b):
            interstitials = {(w, "said"),("said", w)}
            '''
            if "PR" not in t and "PR" not in tmp[1][1]:
                for t in targets:
                    if tmp[0][0] in t:
                        tmp = ((t,tmp[0][1]),tmp[1])
                    if tmp[1][0] in t:
                        tmp =(tmp[0], (t,tmp[1][1]))
            else:
               
            if b:
                return (w in " ".join(entities) and "NN" in t) 
            else:'''
            for i in interstitials:
                if i in bigrams:
                    return False
            return (w in " ".join(entities)) and len(w) > 2 and w != main_char
        try: #exception when there are no target agents or themes
            agent = [w for w,t in pre if bool_check(w,t, True)][0]
            theme = [w for w,t in post if bool_check(w,t, True)][0]
            '''
            if "PR" in agent[1] or "i" == agent[0]:
                prepre = pre[:pre.index(agent)]
                for x in range (0,len(prepre)):
                    if bool_check(prepre[x][0],prepre[x][1], False):
                        agent = (prepre[x][0],prepre[x][1])
                        if agent[0] not in entities: #non full name
                            ag = prepre[x+1][0]+" "+prepre[x][0]
                            agent = (ag,prepre[x][1])
                        break
                        
            if "PR" in theme[1] or "i" == theme[0]:
                theme = [(w,t) for w,t in pre if bool_check(w,t,False) and (w,t) != agent][0]
'''
            if ("by", theme) in bigrams: # check for passive construction, then reverse tuple
                tuples = (theme, agent)
            else:
                tuples = (agent, theme)
        except:
                pass    
    return tuples

ex_actors = ['john','thomas','larry','moe','curly', 'sam', 'jill','jamal','jackson','janet','latoya']
ex_verbs = ['kill','poison','stab','break','murder', 'destroy']
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
tex = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
'''
j = murder_aggregate(tex, ex_verbs,ex_actors)
print(j)'''
