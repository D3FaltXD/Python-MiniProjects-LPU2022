import random
count1 = 0
count2 = 0
count3 = 0
round = 1
print("Rock, Paper or Scissors?")
n = int(input("How many rounds you want to play? "))
while(round <= n):
    print("Round:",round)
    player1 = input("User: ").title()
    a=["Rock","Paper","Scissors"]
    while player1 not in a:
            player1 = input("Insert valid: ").title()
    player2 = random.choice(["Rock", "Paper", "Scissors"]).title()
    print("CPU: ", player2)
    round += 1
    if player1 == player2:
        count3 += 1
        print("It's a Tie")     
    elif player1 == "Rock":
        if player2 == "Scissors":
            count2 += 1
            print("Rock smashes scissors! You win!")
        else:
            count1 += 1
            print("Paper covers rock! You lose.")
    elif player1 == "Paper":
        if player2 == "Rock":
            count2 += 1
            print("Paper covers rock! You win!")
        else:
            count1 += 1
            print("Scissors cuts paper! You lose.")
    elif player1 == "Scissors":
        if player2 == "Paper":
            count2 += 1
            print("Scissors cuts paper! You win!")
        else:
            count1 += 1
            print("Rock smashes scissors! You lose.")
print("End the game")
print("*****FINAL SCORES*****")
print("User Score:",count2)
print("CPU Score:",count1)
print("Ties:",count3)
if count2>count1:
    print("*********************You won*******************")
elif count2<count1:
    print("*******************You lost,AI won*******************")
else:
    print("*******************It's a tie*******************")
