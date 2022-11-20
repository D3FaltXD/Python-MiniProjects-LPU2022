# Rock Paper Scissor

import time
from random import *
from os import system
print("\n \n Welcome To The Game Of Rock Paper And Scissor \n First to Score 3 Points wins!")
c=h=0
options=["Scissors","Paper","Rock"]
while(c!=3 and h!=3):
    print("\n \n Press: \n 0 for Scissor \n 1 for Rock \n 2 for Rock \n")
    g=int(input())
    gc=randint(0,2)
    if(g>2):
        system('cls')
        print("\n \n Invalid Input try again!")
        print("\n \nScore Board: \n ---------------- \n| Human Score:",h,"|"," \n ---------------- \n| Comp  Score:",c,"|\n ---------------- \n")
        continue
    system('cls')
    match options[g]:
        case "Scissors":
            if(gc==0):
                print("\n \n Draw try again!")
            elif(gc==1):
                print("\n \n Human : Scissor Cuts Through Paper!")
                print("\n User +1 Point")
                h+=1
            else:
                print("\n \n CPU : Rock Smashes Scissor!")
                print("\n Comp +1 Point")
                c+=1
        case "Paper":
            if(gc==0):
                print("\n \n CPU : Scissor Cuts Through Paper!")
                print("\n Comp +1 Point")
                c+=1
            elif(gc==1):
                print("\n \n Draw try again!")
                
            else:
                print("\n \n Human : Paper Covers Rock!")
                print("\n User +1 Point")
                h+=1
        case "Rock":
            if(gc==0):
                print("\n \n Human : Rock Smashes Scissor!")
                print("\n User +1 Point")
                h+=1
            elif(gc==1):
                print("\n \n CPU : Scissor Cuts Through Paper!")
                print("\n Comp +1 Point")
                c+=1
            else:
                print("\n \n Draw try again!")
    print("\n \nScore Board: \n ---------------- \n| Human Score:",h,"|"," \n ---------------- \n| Comp  Score:",c,"|\n ---------------- \n")
    time.sleep(1)
if(h==3):
    print("Human Wins! \n \n")
else:
    print("Computer Wins! \n \n ")                
            