#1. Write a function to take input from user in days and print it in years, month and days
#input - 397, output - 1 year , 1 month , 1 day

#code
"""
def calculate(num):
    years = num//365
    s= num - years*365
    months = s//31
    days = num -((years*365)+(months*31))
    print(years, " year, ",months," months ,",days," days")
   
n = int(input("enter a number\n"))
calculate(n)

"""

#2 Generate fibnoacci series for 1 to 20

#code
"""
print("\n*** Fibinocci series***\n")
a=0
b=1
c=1
while c<=20:
    print(c)
    a=b
    b=c
    c=a+b

"""

#3. Create a program to play RPS Game
"""
Inputs:
1. Enter Player name 1
2. Enter Player name 2
3. Enter Player 1 Choice
4. Enter Player 2 Choice


Choices are "Rock", "Scissor", "Paper"

result: who wins?


display result: Player name with choice Rock wins
Player name with choice Scissor Lose


how to manipulate result:
If P1 enter Rock and P2 enters Scissor then P1 Wins
if P1 enter Rock and P2 enters Paper then P2 Wins
if P1 enter Scissor and P2 enters Paper then P1 wins
if both player enters the same choice it should say "Tie"

"""
#code

player1=input("\nenter player1 name\n")
player2=input("\nenter player2 name\n")
print("""Enter any of the following choices
          1) Rock
          2) Scissor
          3) Paper
          \n""")
choice1=input("\nEnter player 1 choice\n")
choice2=input("\nEnter player 2 choice\n")
c1=choice1.upper()
c2=choice2.upper()
if ( c1== "ROCK" and c2 == "SCISSOR")or (c1=="SCISSOR" and c2 == "PAPER")or (c1=="PAPER" and c2 =="ROCK"):
    print(player1, "  wins")
elif ( c2== "ROCK" and c1 == "SCISSOR")or (c2=="SCISSOR" and c1 == "PAPER")or (c2=="PAPER" and c1 =="ROCK"):
    print(player2, "  wins")
elif ( c1==c2):
    print("it's a tie ")
else :
    print("Invalid choice")




    
    

    
