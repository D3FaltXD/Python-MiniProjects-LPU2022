#This is a guess the number game.
import random

print("Hello!")

myName=input("Enter Your name: ")
print("\nWelcome, " + myName)
choice="yes"
score=0
while(True):
    if(choice=="no"):
        break
    upper=int(input("Enter lower range: "))
    lower=int(input("Enter upper range: "))
    guessesTaken = 0
    number = random.randint(upper,lower)
    while guessesTaken < 3:
        print("\nTake a guess.") #There are four spaces in front of print.
        guess = input()
        guess = int(guess)

        guessesTaken = guessesTaken + 1

        if guess < number:
            print("\nHave one more try, Your guess is too low.") # There are eight space in front of print.
        elif guess > number:
            print("\nHave one more try, Your guess is too high.")
        else:
            break

    if guess == number:
        number = str(number)
        print("\nCongrat's")
        score+=5

    else: 
        number = str(number)
        print("\nBetter Luck next time")        
    print("Score is %d"%score)
    choice=input("Do you want to play again? yes-no :")
