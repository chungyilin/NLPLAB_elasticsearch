from  elastic_tool import *
import time
import os
import json
import nltk
import fileinput

count = 0
for line in fileinput.input():
        ## Logging
        count +=1
        if count%10000 == 0:
                print('Sentence Count : ',count)

        ## Put Data
        token = nltk.word_tokenize(line.lower())
        if len(token) > 3 :
                line  = " ".join(token)
                query = {
                                        'length'   : len(token),
                                        'sentence' : line
                                }
                PutData(query,'linggle' ,'linggle')