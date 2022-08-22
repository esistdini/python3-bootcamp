
#!/usr/bin/python3
#Object oriented programming practise 
#Coding practise using class
#Coded by dini( AKA d4t4 or data )
#Instagram : @d.4.t.4
#Youtube : https://www.youtube.com/channel/UCNmEATZC26W2CaUHfxhjefQ

import os
import random

class Game:

    def clear():
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def start():
        min = int(input("Enter the minimum number : "))
        max = int(input("Enter the maximum number : "))
        if min > max:
            print("Swapping minumum and maximum number")
            a , b = min , max
            min = b 
            max = a
            print("Starting the game")
            Game.game(min , max)

        else:
            print("Starting the game")
            Game.game(min , max)

    def game(x , y):
        usr_input = int(input("Enter a number :  "))
        if usr_input < x or usr_input > y:
            print("The number exceeded the limit")
            exit()
        else:
            m = random.randint(x , y)
            if usr_input == m:
                print("Congratulation! , you got the correct number")
                print("Your choice : " , str(usr_input))
                print("Generated number : " , str(m))
                Game.restart()
            else:
                print("Better luck next time!")
                print("Your choice : " , str(usr_input))
                print("Generated number : " , str(m))
                Game.restart()


    def restart():
        final_out = input("Do you want to play it again ? (Y/N) : ")
        if final_out == "y" or final_out == "Y":
            Game.intro()
        else:
            exit()

    def intro():
        Game.clear()
        Game.start()



Game.intro()