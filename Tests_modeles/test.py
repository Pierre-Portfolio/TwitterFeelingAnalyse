import os
from nltk.tag import UnigramTagger
from nltk.corpus import treebank
from nltk.tokenize import word_tokenize
from nltk.corpus import sentiwordnet as swn

train_sents = treebank.tagged_sents()[:3000]
tagger = UnigramTagger(train_sents)
#print(treebank.sents()[0])
#print(tagger.tag(treebank.sents()[0]))

#ouverture articles

path_neg=r'D:\OneDrive - De Vinci\ESILV\A5\Machine_learning_NLP\wp2\txt_sentoken\neg'
path_pos=r'D:\OneDrive - De Vinci\ESILV\A5\Machine_learning_NLP\wp2\txt_sentoken\pos'

path=r'twitter_data_161122.csv'

pos_reviews =os.listdir(path_pos)
neg_reviews =os.listdir(path_neg)


L=set()
for a in neg_reviews:
    #tagger.tag()
    x=path_neg
    x+='\\' + a
    texte=word_tokenize(open(x, "r",encoding='utf-8').read())
    tag=tagger.tag(texte)

    for t in tag:
        if t[1] in ('RB','RBR','RBS'):
            L.add(t[0])

    break

def Predire(nom_texte,type):
    if type=='adverbe':
        Ltag=['RB','RBR','RBS','RBW']
        senti='r'
    elif type=='verbe':
        Ltag=['VB','VBD','VBG','VBN','VBP','VBZ']
        senti='v'


    texte=word_tokenize(open(nom_texte, "r",encoding='utf-8').read())
    L=set()
    tag=tagger.tag(texte)

    for t in tag:
        if t[1] in Ltag:
            L.add(t[0])

    pos_score=0
    neg_score=0


    for adv in L:
        adv_senti = list(swn.senti_synsets(adv, senti))
        if len(adv_senti)!=0:
            pos_score+=adv_senti[0].pos_score()
            neg_score+=adv_senti[0].neg_score()


    res=''
    if pos_score > neg_score:
        res='pos'
    elif pos_score < neg_score:
        res='neg'

    return res,pos_score,neg_scores


def Prediction_dataset(type):
    vrai_pos=0
    vrai_neg=0
    faux_pos=0
    faux_neg=0


    for a in neg_reviews:
        x=path_neg
        x+='\\' + a

        S=Predire(x,type)
        if S[0]=='pos':
            faux_pos+=1
        elif S[0]=='neg':
            vrai_neg+=1

    for a in pos_reviews:
        x=path_pos
        x+='\\' + a

        S=Predire(x,type)
        if S[0]=='pos':
            vrai_pos+=1
        elif S[0]=='neg':
            faux_neg+=1

    return vrai_pos,vrai_neg,faux_pos,faux_neg






