#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:02:46 2018

@author: zy
"""

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet,stopwords
from copy import deepcopy
import numpy
import json
import readfile
#readfile.list_file

#print(readfile.list_file)


file_word_dict={}
#Traverse and read files
for index,f in enumerate(readfile.list_file):
    with open(f,'rb') as file:
        w_list=list(file.read())
    for ind_1,i in enumerate(w_list):
        if not chr(i).isprintable(): #can't be printed
            w_list[ind_1]=0x20
    lower_sentence=(''.join(chr(i) for i in w_list)).lower()  #lower sentence
    lower_word_list=word_tokenize(lower_sentence)
    
    english_lemmatizer=WordNetLemmatizer() #Part of speech reduction
    for ind_2,i in enumerate(lower_word_list):
        lower_word_list[ind_2]=english_lemmatizer.lemmatize(i)
    
    for w in lower_word_list[:]:
        if not wordnet.synsets(w):   #not danci
            lower_word_list.remove(w)    
    
    stwords=stopwords.words('english')
    for w in lower_word_list[:]:
        if(len(w)==i) or (w[0].isdigit()):
            if w in stwords:
                lower_word_list.remove(w)
                
    file_word_dict.setdefault(f,{})
    
    for word in lower_word_list:
        if word in file_word_dict[f]:
            file_word_dict[f][word]+=1
        else:
            file_word_dict[f].setdefault(word,1)

#print(file_word_dict)
word_numbers={}
for file in file_word_dict:
    for w in file_word_dict[file]:
        if w in word_numbers:
            word_numbers[w]+=1
        else:
            word_numbers.setdefault(w,1)
            
temps=[]  # not in 10 - 1000
for w in word_numbers:
    if not(10<word_numbers[w]<1000): 
        temps.append(w)
        for file in file_word_dict:
            if w in file_word_dict[file]:
                file_word_dict[file].pop(w)

for w in temps:
    word_numbers.pop(w)

#vsm tf-idf
vsm_word=deepcopy(file_word_dict)
idf_word={}

for w in word_numbers:
    w_f_num=0
    for file in file_word_dict:
        if w in file_word_dict[file]:
            w_f_num+=1
    idf=numpy.log(len(file_word_dict)/w_f_num)
    idf_word.setdefault(w,idf)
    
alf=0.1
cnt=0
for file in file_word_dict:
    cnt+=1
    max_word_cnt=1
    for w in file_word_dict[file]:
        if max_word_cnt<file_word_dict[file][w]:
            max_word_cnt=file_word_dict[file][w]
    for w in file_word_dict[file]:
        tf=alf+(1-alf)*(file_word_dict[file][w]/max_word_cnt)
        vsm_word[file][w]=tf*idf_word[w]
        
vsm_json=json.dumps(vsm_word)
vsm_file=open('vsm.json','w')
vsm_file.write(vsm_json)
vsm_file.close()
            
    