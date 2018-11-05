#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 15:47:34 2018

@author: zy
"""

import json
import numpy
import random
from copy import deepcopy

#get file_word_dict  {file-{word-number}}
with open('./file_word_dict.json') as fw:
    file_word_dict=json.load(fw)

#get all_word_number  {word-number}    
all_word_number={}
for file in file_word_dict:
    for word in file_word_dict[file]:
        if word in all_word_number:
            all_word_number[word]+=1
        else:
            all_word_number.setdefault(word,1)
            
too_low_high=[]   #not 10-5000
for w in all_word_number:
    if not(10<all_word_number[w]<5000):
        too_low_high.append(w)
        for file in file_word_dict:
            if w in file_word_dict[file]:
                file_word_dict[file].pop(w)
                
for w in too_low_high:
    all_word_number.pop(w)
    
    
#classfy by document
type_file={}
right_number={}

for path in file_word_dict:
    type_file.setdefault(path.split('/')[-2],[]).append(path)
    right_number.setdefault(path.split('/')[-2],0)


#10  test
def KNN(K):
    for i in range(5):
        print('the',i,'test')
        #80% train %20 test
        train_dict=deepcopy(file_word_dict)
        test_dict={}
        for doctype in type_file:
            test=random.sample(type_file[doctype],int(len(type_file[doctype])*0.2))
            for path in test:
                test_dict.setdefault(path,{})
                test_dict[path]=file_word_dict[path].copy()
                train_dict.pop(path)
                
        print('compute idf')
        word_idf={}
        for word in all_word_number:
            w_file_num=0
            for doc in train_dict:
                if word in train_dict[doc]:
                    w_file_num+=1
            if w_file_num!=0:
                idf=numpy.log(len(train_dict)/w_file_num)
            else:
                idf=0;
            word_idf.setdefault(word,idf)
            
        print('compute vsm')
        
        alf=0.1
        for doc in train_dict:
            max_word_num=1
            for w in train_dict[doc]:
                if max_word_num < train_dict[doc][w]:
                    max_word_num=train_dict[doc][w]
            for w in train_dict[doc]:
                tf=alf+(1-alf)*(train_dict[doc][w])
                train_dict[doc][w]=tf*word_idf[w]
                
        test_num=0
        success_num=0
        
        print('K=',K)
        for doc_test in test_dict:
            test_num+=1
            cos_dict={}
            for doc_train in train_dict:
                Vij=0.0
                Vii=0.0
                Vjj=0.0
                for word in test_dict[doc_test].keys():
                    vi=test_dict[doc_test].get(word,0)
                    vj=train_dict[doc_train].get(word,0)
                    Vij+=vi*vj
                    Vii+=vi*vi
                for word in train_dict[doc_train].keys():
                    vj=train_dict[doc_train].get(word,0)
                    Vjj+=vj*vj
                if (Vii*Vjj)==0:
                    value=0
                else:
                    value=Vij/((Vii**0.5)*(Vjj**0.5))
                cos_dict.setdefault(doc_train,value)
            sort_result=sorted(cos_dict.items(),key=lambda item:item[1],reverse=True)
            
            for key in right_number:
                right_number[key]=0
            for j in range(K):
                right_number[sort_result[j][0].split('/')[-2]]+=1
            
            sort_result=sorted(right_number.items(),key=lambda item:item[1],reverse=True)
            
            typer=''
            if sort_result[0][1]!=sort_result[1][1]:
                typer=sort_result[0][0]
            
            if typer==doc_test.split('/')[-2]:
                success_num+=1
            
    result_file=open('knn test.txt','a+')
    result_file.write(i,'test','success_num=',success_num,'test_num=',test_num,'percent=',success_num/test_num)
    result_file.close()


for i in range(3,9):        
    KNN(i)       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        