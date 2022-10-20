# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:49:25 2022

@author: ustpython08
"""

from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
print(client)
db=client['pymongoDB']
collection=db['transactions']

#display count

allDocuments=collection.aggregate([{'$group':{'_id':'$category','count':{'$count':{}}}}])
for item in allDocuments:
    print(item)
    
#display average
allDocuments=collection.aggregate([{'$group':{'_id':'$category','average':{'$avg':'$amount'}}}])
for item in allDocuments:
    print(item)
#display category count in descending order
allDocuments=collection.aggregate([{'$group':{'_id':'$category','count':{'$count':{}}}},{'$sort':{'count':-1}}])
for item in allDocuments:
    print(item)

print("\n")
#display top 5 trending products
allDocuments=collection.aggregate([{'$group':{'_id':'$productname','count':{'$count':{}}}},{'$sort':{'count':-1}},{'$limit' : 5}])
for item in allDocuments:
    print(item)
print()    
#display top 5 trending bottom products
allDocuments=collection.aggregate([{'$group':{'_id':'$productname','count':{'$count':{}}}},{'$sort':{'count':1}},{'$limit' : 5}])
for item in allDocuments:
    print(item)