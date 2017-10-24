from  elastic_tool import *
import time
import os
import json
import nltk
import fileinput
import sys



import gevent.monkey

gevent.monkey.patch_all()
sentence = sys.argv[1:]
start_time = time.time()

def query_es(s):
    query ={
                "from" : 0, 
                "size" : 3,
                "query": {
            "bool":{
                   "must":{"match_phrase": {'sentence' : s}},
                   "should":{"range":{"length":{"gte":10}}}
                }
                }

            }
    
    res = es_search(query , 'linggle' ,'linggle')


jobs = [gevent.spawn(query_es, s) for s in sentence]

gevent.wait(jobs)

print("--- %s seconds ---" % (time.time() - start_time))
