from  elastic_tool import *
import time
import os
import json
import nltk
import fileinput
import sys



import asyncio
import aiohttp
sentence = sys.argv[1:]
start_time = time.time()


@asyncio.coroutine
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


    res = es_search_asy(query , 'linggle' ,'linggle')

    
    sentences = [hit['_source']['sentence'] for hit in res['hits']['hits']] 
    for sentence in sentences:
        print(sentence)
        
        
futures = [query_es(s) for s in sentence]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

print("--- %s seconds ---" % (time.time() - start_time))
