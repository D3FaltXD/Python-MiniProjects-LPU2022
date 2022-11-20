#Full project at : https://github.com/D3FaltXD/Password-Generator-Project
# Project to make a Random Password generator

from random import *
import array
 
def gen(max): #Password generator func
#All valid inputs
    d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
    uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
    s = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~',
           '*', '(', ')']
 
    COMBINED_LIST = d + uc + lc + s
 

    rand_digit = choice(d)
    rand_upper = choice(uc)
    rand_lower = choice(lc)
    rand_symbol = choice(s)
 
# make sure to include all necessary char
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 
 

    for x in range(max - 4):
        temp_pass = temp_pass + choice(COMBINED_LIST)
 
#Shuffle list last time in order to avoid anomalies
        temp_pass_list = array.array('u', temp_pass)
        shuffle(temp_pass_list)
 
# traverse the temporary password array and append the chars
# to form the password
    password = ""
    for x in temp_pass_list:
            password = password + x
    return password


print(""" 
░█▀▀█ █▀▀█ █▀▀ █▀▀ █───█ █▀▀█ █▀▀█ █▀▀▄ 　 ░█▀▀█ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ 
░█▄▄█ █▄▄█ ▀▀█ ▀▀█ █▄█▄█ █──█ █▄▄▀ █──█ 　 ░█─▄▄ █▀▀ █──█ █▀▀ █▄▄▀ █▄▄█ ──█── █──█ █▄▄▀ 
░█─── ▀──▀ ▀▀▀ ▀▀▀ ─▀─▀─ ▀▀▀▀ ▀─▀▀ ▀▀▀─ 　 ░█▄▄█ ▀▀▀ ▀──▀ ▀▀▀ ▀─▀▀ ▀──▀ ──▀── ▀▀▀▀ ▀─▀▀ """)

while(True):
    response=int(input("""\n\nWelcome To Password Generator ! 
    \n\rPress 0 to Exit
    \n\rPress 1 to generate Password: """))
    if(response==1):
        len=int(input("Please enter the password length: "))
        if(len>=12):
            print("\n\nThe random password is: %s"%(gen(len)))
        elif(len<12):
            print("Please enter a length more than or equal to 12")
        else:
            print("Error Please enter a correct value")
    elif(response==0):
        break
    else:
        print("Invalid Input")