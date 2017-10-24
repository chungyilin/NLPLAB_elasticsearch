import json
import requests
    
    
    
import asyncio
import aiohttp

def ListData(ESindice,EStype):
	query ={
			"from" : 0, 
			"size" : 1000,
            "query": {
                "match_all": {}
            }
        }
	query = json.dumps(query)

	r = requests.get('http://localhost:9200/'+ESindice+'/'+EStype+'/'+'_search?pretty',data = query)
	if 'hits' in r.json():
		sentences = [hit['_source'] for hit in r.json()['hits']['hits']] 
		for sentence in sentences:
		    print(sentence)

	return r.json()

def es_search(query , ESindice , EStype):
	query = json.dumps(query)

	r = requests.get('http://localhost:9200/'+ESindice+'/'+EStype+'/'+'_search?pretty',data = query)
	if 'hits' in r.json():
		if 'hits' in r.json()['hits']:
			sentences = [hit['_source'] for hit in r.json()['hits']['hits']] 
			for sentence in sentences:
			    print(sentence)
	return r.json()


def es_search_asy(query ,session, ESindice , EStype):
    query = json.dumps(query)
    r = await session.get('http://localhost:9200/'+ESindice+'/'+EStype+'/'+'_search?pretty',data = query)
    #if 'hits' in r.json():
    #    if 'hits' in r.json()['hits']:
    #       sentences = [hit['_source'] for hit in r.json()['hits']['hits']] 
    #       for sentence in sentences:
    #       	print(sentence)
    return r

def es_delete(query , ESindice, EStype):
	query = json.dumps(query)
	r = requests.delete('http://localhost:9200/'+ESindice+'/'+EStype,data = query)

	return r.text


def es_update(query , ESindice, EStype , index_id):
	query = json.dumps(query)
	r = requests.delete('http://localhost:9200/'+ESindice+'/'+EStype+'/'+index_id+'/_update',data = query)

	return r.text

def es_put(query , ESindice , EStype):
	query = json.dumps(query)

	r = requests.post('http://localhost:9200/'+ESindice+'/'+EStype,data = query)

	return r.json()








