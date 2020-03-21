

import nltk,re
from nltk.tokenize import sent_tokenize
from nltk import load

def loadLexicon(fname):
    newLex = set()
    lexConn = open(fname)
   
    for line in lexConn:
        newLex.add(line.strip())
    lexConn.close()
    
    return newLex

def run(path1):
    decisions=[] 
    reviews=[]
    #load the positive and negative lexicons
    posLex=loadLexicon('positive-words.txt')
    negLex=loadLexicon('negative-words.txt')
    return posLex,negLex
    
    

def processSentence(sentence,posLex,negLex,tagger):
    lst = []
    terms = nltk.word_tokenize(sentence)   #tokenize the sentence
    tagged_terms=tagger.tag(terms)
    #print(tagged_terms)
    for i in range(len(tagged_terms)-3):# for every tagged term
            term1=tagged_terms[i] #current term
            term2=tagged_terms[i+1] # following term
            term3=tagged_terms[i+2]
            term4=tagged_terms[i+3]      
            if re.match('NN',term4[1]) and term1[0] == 'not' and (term3[0] in posLex or term3[0] in negLex): # current term is an adverb, next one is an adjective
                lst.append((term1[0],term2[0],term3[0],term4[0]))# add the adverb-adj pair to the list
    print(lst)   
    return lst


if __name__=='__main__':
    pos,neg = run('C:/Users/manik/Documents/all/Stevens/660/week6')
    sen ='''My name is not John'''
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)
    lst = processSentence(sen,pos,neg,tagger)
    






