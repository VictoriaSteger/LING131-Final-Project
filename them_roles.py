import nltk
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
def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0]

def murder_aggregate(text, m_words, entities):
    print("-----------------------SPOILERS--------------------------")
    suspicious_events = list()
    for s in text:
        tmp =them_rip(s,m_words,entities)
        if tmp:
            suspicious_events += tmp

    murderers =[agent for agent, theme in suspicious_events]
    victims = [theme for agent, theme in suspicious_events]
    print("SUSPECTS:", murderers)
    print("POTENTIAL VICTIMS:", victims)
    mfm =most_frequent(murderers)
    mfv =most_frequent(victims)
    print("MOST LIKELY KILLER:", mfm)
    print("MOST LIKELY VICTIM:", mfv)
    return (mfm,mfv)

    
def them_rip(sent, murdery, entities):
    sls = nltk.pos_tag([w.lower() for w in nltk.word_tokenize(sent)])
    print(sls)
    bigrams = list(nltk.bigrams([w for w,t in sls]))
    #print("LIST: ",sls)
    tuples = list()
    #print("TEXT: ",sent) 
    vbls = [(w,t) for (w,t) in sls if "VB" in t and lemmatizer.lemmatize(w,'v') in murdery]
    #print("VERBS: ", vbls)
    for x in vbls:
        pre = sls[:sls.index(x)][::-1]
        post = sls[sls.index(x)+1:]
        if "not" != pre[0][0] and "n't" != pre[0][0]:  # in case of negation 
            agent = ''
            theme = ''
            def bool_check(w,t):
                return w in entities or "PR" in t # entity or pronoun
            try: #exception when there are no target agents or themes
                agent = [w for w,t in pre if bool_check(w,t)][0]
                theme = [w for w,t in post if bool_check(w,t)][0]
                if ("by", theme) in bigrams: # check for passive construction, then reverse tuple
                    tuples.append((theme, agent))
                else:
                    tuples.append((agent,theme))
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
#print(them_rip(s4,ex_verbs,ex_actors))
j = murder_aggregate(tex, ex_verbs,ex_actors)
print(j)
