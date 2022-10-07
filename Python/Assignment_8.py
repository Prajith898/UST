#8. Write a pay computation program with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
"""
8 hours * 5 days = 40 hours , 5 hours = 1.5 times

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Write functions to calculate your trip's costs:

Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night. So, the function hotel_cost should return 140 * nights.

Define a function called plane_ride_cost that takes a string, city, as input. The function should return a different price depending on the location, similar to the code example above. Below are the valid destinations and their corresponding round-trip prices.
"Charlotte": 183
"Tampa": 220
"Pittsburgh": 222
"Los Angeles": 475

define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days) if you rent the car for 7 or more days, you get $50 off your total(cost-=50). Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. You cannot get both of the above discounts. Return that cost.

Then, define a function called trip_cost that takes two arguments, city and days. Like the example above, have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.

Modify your trip_cost function definion. Add a third argument, spending_money. Modify what the trip_cost function does. Add the variable `spending_money to the sum that it returns

"""

#code

def computepay(hour,rate):
    pay=(hour-(hour%40))*rate+(hour%40)*1.5*rate
    return pay
def hotel_cost(nights):
    return((nights*140))
def  plane_ride_cost(city):
    charge ={"Charlotte": 183,"Tampa": 220,"Pittsburgh": 222,"Los Angeles": 475}
    return(charge[city])
def rental_car_cost(days):
    if days>=7:
        return ((40*days-50))
    elif days>=3:
        return ((40*days - 30))
    else:
        return ((40*days))
def trip_cost(days,city,spending_cost=None):
    cost=(hotel_cost(days)+rental_car_cost(days)+plane_ride_cost(city))
    if spending_cost!=None:
        cost=cost+spending_cost
    return (cost)
    
days=int(input("Enter the trip days\n"))
print("\nenter the city name you goig to visit\n")
city=input("Charlotte \n Tampa \n Pittsburgh \n Los Angeles\n")
print("\nExpenses :",trip_cost(days,city,spending_cost=None))
spend = int(input("Enter the spending cost\n"))
print("\nTotal tour expendeture: " ,trip_cost(days,city,spend))
trip_cost(days,city,spend)
print("\nEnter hour and rate to calculate compute pay\n")
hour=int(input("\nEnter hour\n"))
rate=int(input("\nEnter rate\n"))
print("pay: ",computepay(hour,rate))
