#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:42:17 2018

@author: zy
"""

import os 
import random
dir_name=os.getcwd()
data_dir=dir_name+'/../20news-18828'
data_dir_list=os.listdir(data_dir)#20dir name
#print(len(data_dir_list))
list_file=[]
for dfile in data_dir_list:
#    print(os.listdir(data_dir+'/'+dfile)) 
    list_file.extend([data_dir+'/'+dfile+'/'+i for i in os.listdir(data_dir+'/'+dfile)])
    

#print(len(list_file))

list_file_train=random.sample(list_file,int(len(list_file)*0.8))
print(list_file_train)

#list_file_test=list_file-list_file_train

list_file_test=[i for i in list_file if i not in list_file_train]

print(list_file_test)