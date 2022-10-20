# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:53:00 2022

@author: ustpython08
"""

import pymongo
if __name__=="__main__":
    print("Welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db=client['pymongoDB']
    myCollection=db['myFirstCollection']
    document = [{'_id': 4, 'name':'Lenovo Ideapad', 'price':128000,                   'color': ["Gray","Gold","Black"], 'ram':[4096,8196],'storage':[1024, 2048, 4096]},                 {'_id': 5, 'name':'Macbook', 'price':8000,                   'color': ["Black","Silver"], 'ram':[4096], 'storage': [1024, 2048]}]
    #myCollection.insert_many(document)
    print(myCollection.distinct('name'))
    # Update the existing document
    myCollection.update_one({'_id':5},{'$set':{'price':88000}})
    print(myCollection.find_one({'_id':5}))
    #rename existing column name
    myCollection.update_many({},{'$rename':{'name':'Laptop name'}})
    allDocuments = myCollection.find()
    for item in allDocuments:
        print(item)