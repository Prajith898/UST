#4. Write functions to calculate and display grosssalary and netsalary of an employee after getting input as basicsalary
#Write separate functions for allowances and deductions to calculate them respectively

"""
netsalary = grosssalary - deductions
grosssalary = basicsalary + allowances

allowances = hra(22% of basicsalary) + da(18% of basicsalary) +ta(10% of basicsalary)

deductions = proftax(if basicsalary > 8000 the 200 else 150) + pf(12% of basicsalary) + insurance(8% of basicsalary)

"""

#code

"""
def allowances(basic_salary):
    return ((0.22*basic_salary+0.18*basic_salary+0.10*basic_salary))
def deduction(basic_salary):
    if basic_salary > 8000:
        proftax = 200
    else :
        proftax = 150
    return ((proftax+0.12*basic_salary+0.08*basic_salary))
def salary(basic_salary):
    gross_salary= basic_salary+allowances(basic_salary)
    net_salary= gross_salary - deduction(basic_salary)
    print("\n Gross salary = ", gross_salary)
    print("\n Net salary =", net_salary)
basic_salary = float(input("Enter the Basic Salary\n"))
salary(basic_salary)


"""

#6. Ask user a input string and check if the entered string is palindrome. Ex: Input NitiN -> o/p palindrome

#code
"""

str1= input("\nEnter a string\n")
if (str1 == str1[::-1]):
    print("palindrome")
else :
    print(" Not palindrome")

"""

#7. Ask user to input email and check if the email is in valid form or not. Ex: it should contain single '@', '.', @or.shouldn't be in 1st position

#code


mail=input("Enter Your mail id \n")
count1=0
count2=0
if ((mail[0]!='@') and (mail[0]!=".")):
    for i in mail:
        if (i == '@'):
            count1+=1
            break
        elif(i == '.'):
            count2+=1
        elif(count1>=2)or(count2>=2):
                break
if (count1==1)and(count2==1):
    print("Valid mail id")
else:
    print("Invalid mail id ")



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
"""
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
print("Total pay: ",computepay(hour,rate))

"""
