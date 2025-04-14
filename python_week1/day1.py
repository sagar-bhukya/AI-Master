# num =10

# if num>0:
#     print("positive")
# elif num==0:
#     print("number is zero")
# else:
#     print("number is zero")


# nested condition

# age =32
# if age>18:
#     if age<30:
#         print("young adult")
#     else:
#         print("adult")
    


#loops--------------
#syntax
#for --- iterartes over a sequence
# for item in sequence:
    #code block

# fruits=["apple","banana","mongo"]
# for fruit in fruits:
#     print("fruit:::\n",fruit)


#loop with range
# for i in range(10):# 1 -9
#     print(i)



#while loop---Executes as long as a condition True
#syntax----
# while condition:
#     #code Block

#count down from 6
# a=6
# c=0
# while a>c:
#     c+=1
#     print(f"count::{c}")

# break and continue for control flow
#break terminates the loop permanently when a condition is met
#continue its skip the matched one 
# for i in range(10):
#     print("iii",i)
#     if i==5:
#         # continue
#         break

# for i in range(10):
#     if i%2==0:
#         continue #guves odd numbers
#     print(i)


#handson ---------
#check if a number is prime

# num=int(input("enter a number"))
# if num>1:
#     for i in range(2, int(num**0.5)+1):
#         print("iiiiii::",i)
#         if num %i==0:
#             print(f"{num}is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# else:
#     print(f"{num} is prime number")



#create a Menu-Driver calculator
# def add(a,b):
#     return a+b
# def substract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divede(a,b):
#     if b!=0:
#         return a/b
#     else:
#         return "Division by zero is not allowed"
# while True:
#     print("\nMenu:")
#     print("1.Addition")
#     print("2.Substraction")
#     print("3.multiply")
#     print("4.Division")
#     print("5.Exit")
#     choice=input("Enter your choice based on the menu::")
#     if choice == "5":
#         print("Exiting Program")
#         break
#     num1=float(input("enter first number: "))
#     num2=float(input("enter second number; "))
#     if choice=="1":
#         print("Result add: ",add(num1,num2))
#     elif choice =="2":
#         print("Result: ",substract(num1,num2))
#     elif choice =="3":
#         print("Result: ",multiply(num1,num2))
#     elif choice =="4":
#         print(":Result: ",divede(num1,num2))
#     else:
#         print("you Enter wrong number!. please enter from the display number")


#finding a factorial of a number using while loop-----
# fact=int(input("enter what number you to find factorial"))
# re=1
# while fact>0:
#     re*=fact
#     fact-=1
# print("re::\n",re)

#finding a largest number from a list---------
# list=[5,7,2,87,9]
# max=0
# for i in list:
#     if i>max:
#         max=i
# print(max)


#============================================================================================================


#functions-----------

# def function_name(parameters):
#     #code block
#     return result


#function with parameters and return value
# def add_numbers(a,b):
#     return a+b

# result=add_numbers(2,3)
# print(result)

#scope and lifetime of variables

#scope
#---local scope
# def greet():
#     message="Hello papa"
#     # print(message)
#     return message
# a=greet()
# print(a)


#global scope------------
# greeting="Hi papa"
# def say_hello():
#     print(f"outside thi function variable{greeting}")
# say_hello()
# print(f"global variables {greeting}")



# #modules------------------
# from math import sqrt as sr
# print(sr(10))

#create a function to calculate Factorials

# def factorials(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n* factorials(n-1)

# def prin_factorial(n):
#     result=factorials(n)
#     print(f"the factorial of {n} is {result}")
# prin_factorial(4)



#Data types------------------
#list =============================================================
numbers =[1,2,3,4,5,6,7]
fruits=["apples","banana","cherry"]
mixed =[1,"hi",True]
#accessing the elem-------
# print(numbers[2])
# print(fruits[-1])
# print(mixed[0])

# fruits.append("orange")#adding at last
# fruits.insert(1,"grapes")#adding at specific index
# print(fruits)

# fruits.remove("banana")#remove for spcific data
# print(fruits)

# del fruits[0]#delete for particular index or
# print(fruits)
# del fruits["cherry"]
# print(fruits)

# fruits.pop(1)#remove last or specific
# print(fruits)



# #tuples----------------------
# colors=("red","green","blue")
# print(colors[0])


#dictonary-----------------------

#student={"name":"sagar","age":25,"grade":"A"}

# student["subject"]="math"
# student["age"]=24
# del student["subject"]

# student.pop("age")
# print(student)

#iterate------
# for key,val in student.items():
#     print(key,":",val)

#sets----------------
# numbers={1,2,3,4}
# empty_set={}
# print(numbers)
# numbers.add(5)
# print(numbers)
# numbers.add(4)
# print(numbers)
# numbers.remove(3)# 3 ele remove
# print(numbers)

# #union of 2 sets
# set1={1,2,3}
# set2={3,4,5}
# print(set1 | set2) # union remove duplicates

# print(set1 & set2)# intersection only gives common in both 

# print(set1 -set2)#


#------handson-----
# person ={"name":"sagar","age":25,"grade":"A"}

# #add new key-value pair
# person["address"]="regadithanda"

# #update age
# person["age"]=30
# #remove grade
# if "grade" in person:
#     del person["grade"]
# print(person)


#count frequency
# sentence= input("enter a sentence")
sentence= "sagar"
#split the sentence into words
words =sentence.split('')
#initialize dictionary
word_count={}
for word in words:
    word= word.lower()
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)