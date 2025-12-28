#"""---------- Assignment 3 ---------''''
#task1
def rec_fun(n):
    if n==1: return 1
    else: return n*rec_fun(n-1)
n=int(input("enter a number"))
print(f"factorial of {n} is {rec_fun(5)}")

#task2
import math
n1=int(input("enter a number"))
print(f"square root of {n1} is {math.sqrt(n1)}")
print(f"natural logarithm of {n1} is {math.log(n1)}")
print(f"sine of {n1} is {math.sin(n1)}")




# #''''---------  Assignment 2 ---------'''#
# #Task1 - Check if a number is odd or even
# rec_int=int(input("enter a number"))
# if rec_int % 2 == 0: print(f"{rec_int} is a even number")
# else: print(f"{rec_int} is a odd number")
#
# #Task2 - Sum of integers from 1 to 50 using a loop
# total=0
# for i in range(1,51,1):
#     total=total+i
# print(f"the sum of numbers from 1 to 50 is: {total}")


#Assignment 1
# #Task 1
# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# add=num1+num2
# sub=num1-num2
# mul=num1*num2
# div=num1/num2
# print("addition is", add)
# print("subtraction is", sub)
# print("multiplication is", mul)
# print("division is", div)
#
# #Task 2
# first_name=input("enter your first name")
# last_name=input("enter your last name")
# concatenation=first_name+" "+last_name
# print("Hello",concatenation,"hope you have great exp learning python")