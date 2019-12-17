from nltk.corpus import verbnet

my_classids = verbnet.classids(lemma='take')
print(my_classids)
# my_lemmas = verbnet.lemmas(my_classids)
# my_longid = longid(my_shortid)
# my_shortid = shortid(my_longid)
for i in my_classids:
    my_vnclass = verbnet.vnclass(i)
    # my_wordnetids = verbnet.wordnetids(mi)
    # Human-friendly methods
    verbnet.pprint(my_vnclass)
    # vnframe = my_vnclass.findall('FRAMES/FRAME')
    # print(verbnet.pprint_description(vnframe))
    # print(verbnet.pprint_frames(vnframe))
    print(verbnet.pprint_members(my_vnclass))
    # print(verbnet.pprint_semantics(vnframe))
    print(verbnet.pprint_subclasses(my_vnclass))
    # print(verbnet.pprint_syntax(vnframe))
    # x = verbnet.pprint_themroles(my_vnclass)
    print(verbnet.pprint_themroles(my_vnclass))
    '''for j in x.split("]"):
        print(j)'''