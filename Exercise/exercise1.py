# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:37:48 2022

@author: ustpython08
"""

import pymongo
if __name__=="__main__":
    print("Welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    all_DBS=client.list_database_names()
    print(all_DBS)
    collection=client['supermarket']
    print(collection.list_collection_names())