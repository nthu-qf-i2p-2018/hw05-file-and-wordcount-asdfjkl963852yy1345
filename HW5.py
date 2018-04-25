# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:31:05 2018

@author: acer
"""

import csv
import json
from collections import Counter
import string

def main(filename):
    txtfile=open(filename)
    lines=txtfile.readlines()
    
    all_words=[]
    
    for line in lines:
        words=line.split()
        
        for word in words:
            word=word.strip(string.punctuation)
            
            if word!=None and word!="":
                all_words.append(word)
                
    count=Counter(all_words)
    d=dict()
    for a,b in count.most_common():
        add_dict={a:b}
        d.update(add_dict)
        
    with open("wordcount.csv" , "w") as csv_file:
        print("word","count",file=csv_file,sep=",")
        for word,count in count.most_common():
            print(word,count,file=csv_file,sep=",")
    
    
    f=open("wordcount.json", "w") 
    json.dump(d , f)
    
        
        
            
        
    
    

                      
    
                    
    
            