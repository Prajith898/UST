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

