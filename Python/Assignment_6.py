#6. Ask user a input string and check if the entered string is palindrome. Ex: Input NitiN -> o/p palindrome

#code

str1= input("\nEnter a string\n")
if (str1 == str1[::-1]):
    print("palindrome")
else :
    print(" Not palindrome")


