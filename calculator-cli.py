

#!/usr/bin/python3
#Coding practise using functions
#Coded by dini( AKA d4t4 or data )
#Instagram : @d.4.t.4
#Youtube : https://www.youtube.com/channel/UCNmEATZC26W2CaUHfxhjefQ

from __future__ import division
from distutils.command.clean import clean
import math
import os

ops = os.name #Retrieves operating system detail

def intro():

    options()


def restart():
    final_out = input("Do you want to use it again ? (Y/N) : ")
    if final_out == "y" or final_out == "Y":
        intro()
    else:
        exit()

def options():
    print("***Basic CLI Calculator***")
    print()
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Find Square Root")
    print("6 - Find Square of")
    print("7 - Find Power Of Two Numbers")


    usr_choice()

def addition():
    
    n1 = int(input("Enter the first number : "))
    n2 = int(input("Enter the second number : "))
    val = n1 + n2
    print()
    print("Addition : " , str(val))
    print()

    restart()

def subtraction():
    
    n1 = int(input("Enter the first number : "))
    n2 = int(input("Enter the second number : "))
    val = n1 - n2
    print()
    print("Subtraction : " , str(val))
    print()

    restart()

def multiplication():
    
    n1 = int(input("Enter the first number : "))
    n2 = int(input("Enter the second number : "))
    val = n1 * n2 
    print()
    print("Multiplication : " , str(val))
    print()

    restart()

def caldivision():
    
    n1 = int(input("Enter the first number : "))
    n2 = int(input("Enter the second number : "))
    val = n1 // n2 
    print()
    print("Division : " , str(val))
    print()

    restart()

def squareroot():
    num = int(input("Enter the number : "))
    print()
    print("Square root : " ,  str(math.sqrt(num)))
    print()

    restart()

def squareof():
    num = int(input("Enter the number : "))
    print()
    val = num ** 2
    print("Square of : " , str(val))
    print()

    restart()

def powerof():
    n1 = int(input("Enter the base number : "))
    n2 = int(input("Enter the power number : "))
    val = math.pow(n1 , n2)
    print()
    print("Power of : " , str(val))
    print()


    restart()

def usr_choice():
    print()
    usr_input = int(input("Enter your option : "))
    if usr_input == 1:
        addition()

    elif usr_input == 2:
        subtraction()

    elif usr_input == 3:
        multiplication()

    elif usr_input == 4:
        caldivision()

    elif usr_input == 5:
        squareroot()

    elif usr_input == 6:
        squareof()

    elif usr_input == 7:
        powerof()

    else:
        print("Check the available options and try again next time!")
        exit()

intro()
