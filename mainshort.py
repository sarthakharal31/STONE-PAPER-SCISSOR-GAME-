"""
1 for stone 
-1 for paper 
0 for scissor
"""
import random
computer = random.choice([-1,0,1])
youstr = input("ENTER YOUR CHOICE (s,p,c) : ")
youdict = {
    "s" : 1,
    "p" : -1,
    "c" : 0,
}
reversedict = {
    1 : "stone",
   -1 : "paper",
    0 : "scissor",
}
you = youdict[youstr]

print(f"You chose {reversedict[you]} \ncomputer chose {reversedict[computer]}")

if(computer == you):
    print("OOPS! its a draw")
    print("better luck next time ")
else:
   
    if((computer - you)== -1 or (computer - you)== 2):
        print("you win")
    else :
        print("you lose")

#this  is shortened version of following 
# by analyzing that if computer - you is -1 or 2 then and then the user is wining
# so  i implemented this logic and here you can see the result 

""" if(computer== -1 and you == 1):   -2
        print("you lose")
    elif(computer== -1 and you == 0):    -1
        print("you win")
    elif(computer== 1 and you == -1):     2
        print("you win")
    elif(computer== 1 and you == 0):      1
        print("you lose")
    elif(computer== 0 and you== -1):      1
        print("you lose")
    elif(computer== 0 and you == 1):      -1
        print("you win")
    else :
        print("something went wrong")
        print("please try again")
"""



