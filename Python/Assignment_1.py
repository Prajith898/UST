#1. Write a function to take input from user in days and print it in years, month and days
#input - 397, output - 1 year , 1 month , 1 day

#code

def calculate(num):
    years = num//365
    s= num - years*365
    months = s//31
    days = num -((years*365)+(months*31))
    print(years, " year, ",months," months ,",days," days")
   
n = int(input("enter a number\n"))
calculate(n)

