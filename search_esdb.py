from  elastic_tool import *
import time
import os
import json
import nltk
import fileinput
import sys

sentence = sys.argv[1]
start_time = time.time()


query ={
			"from" : 0, 
			"size" : 10,
            "query": {
		"bool":{
               "must":{"match_phrase": {'sentence' : sentence}},
			   "should":{"range":{"length":{"gte":10}}}	
			}
            }

        }


res = es_search(query , 'linggle' ,'linggle')

print("--- %s seconds ---" % (time.time() - start_time))
sentences = [hit['_source']['sentence'] for hit in res['hits']['hits']] 
for sentence in sentences:
    print(sentence)
