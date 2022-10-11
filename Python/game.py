#!/usr/bin/env python
# coding: utf-8

# #### Snake Water Gun using python program

# In[11]:


import random
player=input('Enter Player name:')
num=int(input("enter number of rounds:"))
choice=['snake','water','gun']
count1=0
count2=0
count3=0
for i in range(1,num+1):
    print("""\nEnter any of these choice for round {}
            1) Snake
            2) Water
            3) Gun\n""".format(i))
    choice2=random.choice(choice)
    choice1=(input("Enter player choice :").lower())
    print("computer choice : ",choice2)
    if ((choice1=='snake' and choice2=='water')or(choice1=='water'and choice2=='gun')or(choice1=='gun'and choice2=='snake')):
        print("***{} wins round {}***".format(player,i))
        count1+=1
    elif ((choice2=='snake' and choice1=='water')or(choice2=='water'and choice1=='gun')or(choice2=='gun'and choice1=='snake')):
        print("***Computer wins rounds {}***".format(i))
        count2+=1
    elif (choice1==choice2):
        print("round {} is  a tie".format(i))
        count3+=1
    else:
        print("\nWrong choice")
print("{} wins {} times".format(player1,count1))
print("Computer wins {} times".format(count2))
print("Tie :",count3)


# In[ ]:




