#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:42:17 2018

@author: zy
"""

import os 
dir_name=os.getcwd()
data_dir=dir_name+'/../20news-18828'
data_dir_list=os.listdir(data_dir)#20dir name
#print(len(data_dir_list))
list_file=[]
for dfile in data_dir_list:
#    print(os.listdir(data_dir+'/'+dfile)) 
    list_file.append([data_dir+'/'+dfile+'/'+i for i in os.listdir(data_dir+'/'+dfile)])
    

#print(list_file[19])
    
    