# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 00:19:28 2022

@author: ustpython08
"""

from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

def insert_collection():
    data=pd.read_csv("E:/Assignment/Flights_Delay.csv")
    data1=json.loads(data.to_json(orient='records'))
    collection.insert_many(data1)

if __name__=='__main__':
    
    # a) Create collections “flights” inside database “airline_delayDB”
    client=MongoClient('mongodb://localhost:27017')
    db=client['airline_delayDB']
    collection=db['flights']
    #insert_collection()
    
    # b) average arrival delay caused by airlines
    all_docs=collection.aggregate([{'$group':{'_id':{},'average':{'$avg':'$ARRIVAL_DELAY'}}},{'$project':{'_id':0}}])
    for i in all_docs:
        print(i)
        
        
        
    # c) Days of months with respect to average of arrival delays.
    #   [Create a suitable plot using matplotlib/seaborn]
    
    avg_arrival_delay=collection.aggregate([{'$group': {'_id':'$DAY','Average':
                                    {'$avg':'$ARRIVAL_DELAY'}}}])
    
    avg_arrival_delay1=pd.DataFrame(avg_arrival_delay)
    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(10,7))
    sns.barplot(x=avg_arrival_delay1['_id'],y=avg_arrival_delay1['Average'])
    plt.title('Days of month VS average arrival delay')
    plt.xlabel('Days')
    plt.show()
    
    # d) Arrange weekdays with respect to the average arrival delays caused. 
    # [Create a suitable plot using matplotlib/seaborn]
    
    avg_arrival_delay=collection.aggregate([{'$group': {'_id':'$DAY_OF_WEEK','Average':
                                    {'$avg':'$ARRIVAL_DELAY'}}}])
    avg_arrival_delay1=pd.DataFrame(avg_arrival_delay)
    sns.barplot(x=avg_arrival_delay1['_id'],y=avg_arrival_delay1['Average'])
    plt.title('Weekdays VS average arrival delay')
    plt.xlabel('Weekdays')
    plt.show()
    
    # e) Arrange Days of month as per cancellations done in descending order.  
    #Create a suitable plot using matplotlib/seaborn]
    
    cancellation=collection.aggregate([{'$match':{'CANCELLED':1}},
                {'$group':{'_id':'$DAY','Count1':{'$count':{}}}},
                {'$sort':{'Count1': -1}}])
    
    cancellation1=pd.DataFrame(cancellation)
    sns.barplot(x=cancellation1['_id'],y=cancellation1['Count1'])
    plt.title('Days of Month VS Cancellation')
    plt.xlabel('Days')
    plt.ylabel('Cancellation count')
    plt.show()
    
    #f) Find the busiest airports with respect to day of week. 
    #Create a suitable plot using matplotlib/seaborn.
    
    airport=collection.aggregate([{'$group':{'_id':'$DAY_OF_WEEK'}}])
    busy_airport=pd.DataFrame(airport)
    print(busy_airport)
    
    
    #g Find top 10 Airlines of US. Create a suitable plot using matplotlib/seaborn.
    
    
    top=collection.aggregate([{ '$match':{'AIRLINE':"US"}},
            {'$group' :{'_id' : '$FLIGHT_NUMBER', 'Count1':{'$count' : {}}}},
            {'$sort':{'Count1':-1}},{'$limit':10}])											
											
    
    top_10=pd.DataFrame(top)
    sns.barplot(x=top_10['_id'],y=top_10['Count1'])
    plt.title('Top 10 Airlines of US')
    plt.xlabel('Flight Number')
    plt.ylabel('count')
    plt.show()
    
    
    
    #h) Finding airlines that make the maximum, minimum number of cancellations.
    
    
    min_cancellation = collection.aggregate([{'$match' : {'CANCELLED':1}},
                    {'$group':{'_id':'$AIRLINE','min':{'$count':{}}}},
                    {'$sort':{'min': 1}}, {'$limit':1}])
    for i in min_cancellation:
        print(i)
    
    
    max_cancellation = collection.aggregate([{'$match' : {'CANCELLED':1}},
                    {'$group':{'_id':'$AIRLINE','max':{'$count':{}}}},
                    {'$sort':{'max': -1}}, {'$limit':1}])
                                        
    for i in max_cancellation:
        print(i)
    
    
    # i) Find and show airlines names in descending that make the most number of diversions made.
    #[Create a suitable plot using matplotlib/seaborn]
    
    diversion = collection.aggregate([{'$match' : {'DIVERTED':1}},
                {'$group':{'_id':'$AIRLINE','Count':{'$count':{}}}},
                {'$sort':{'Count': -1}}])
    
    diversion1=pd.DataFrame(diversion)
    sns.barplot(x=diversion1['_id'],y=diversion1['Count'])
    plt.title('Airline Vs No.of diversions')
    plt.xlabel('Airline')
    plt.show()
    
    # j) Finding days of month that see the most number of diversion
    
    diversion = collection.aggregate([{'$match' : {'DIVERTED':1}},
                {'$group':{'_id':'$DAY','Count1':{'$count':{}}}},
                {'$sort':{'Count1': -1}},{'$limit':1}])
    
    print()
    for i in diversion:
        print(i)
    print()
    # k) Calculating mean and standard deviation of departure delay for all flights 
    #   in minutes
    
    departure_delay = collection.find({},{'DEPARTURE_DELAY':1,'_id':0})
    
    departure_delay1=pd.DataFrame(departure_delay)
    print("mean :",departure_delay1.mean())
    print("Standard deviation :",departure_delay1.std())  
    
    
    # l)Calculating mean and standard deviation of arrival delay for all flights 
    #   in minutes
    
    arrival_delay = collection.find({},{'ARRIVAL_DELAY':1,'_id':0})
    
    arrival_delay1=pd.DataFrame(arrival_delay)
    print("mean :",arrival_delay1.mean())
    print("Standard deviation :",arrival_delay1.std())   

    #m) Create a partitioning table “flights_partition” using partitioned by schema “CANCELLED”


    #n) Finding all diverted Route from a source to destination Airport & which route is the most diverted route.
    
    diverted_route=collection.aggregate([{'$match':{'DIVERTED':1}},
             {'$group':{'_id':{'ORIGIN_AIRPORT':'$ORIGIN_AIRPORT',"DESTINATION_AIRPORT":'$DESTINATION_AIRPORT'},
            'count':{'$sum':1}}}])
    
    diverted_route1=pd.DataFrame(diverted_route)
    print('Diverted route\n')
    print(diverted_route1['_id'])
    max=diverted_route1['count'].max()
    print('Maximum diverted route\n')
    print(diverted_route1[diverted_route1['count']==max])
                               
     
    
    #o) When is the best time of day/day of week/time of year to fly with minimum delay
    

    
    
        
    