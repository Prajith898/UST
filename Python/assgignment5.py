#5. For the given string
"""

""Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Found
ation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code""


calculate the number of vowels individually i.e number of a, e, i , o and u , calculate total number of consonants without considering any punctuation character
"""

#code


string = """Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python
Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code"""
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
count=0
str1=string.lower()
for i in str1:
    if (i.isalpha()):
        if i in vowels.keys():
            vowels[i]+=1
        else :
            count +=1
print("\nCount of constants : ",count)
for i in vowels:
    print("count of ",i, " : ", vowels[i])
    
