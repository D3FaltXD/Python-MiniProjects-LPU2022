# A python code to design an ATM machine
# Default Password is: 1234

# start by defining some functions to make our code stress free
def substract(a, b):
    return a - b


def add(a, b):
    return a + b


def withdraw(accBalance, amount):
    newBalance = substract(accBalance, amount)
    return newBalance


def deposit(accBalance, amount):
    newBalance = add(accBalance, amount)
    return newBalance


def thanks():
    print("\nThank you for banking with us.")
    print("_____________________________________ \n")

# welcoming the user and assigning values to some variables


def main():
    print("________________________________ \n")
    name = print("WELCOME TO ATM Machine")
    print("________________________________ \n")

    balance = int(1000000)
    count=0


# inputs your pin and checks if its correctso as to display your available balance
    while True:
        if count>=3:
        	print("Your card has been blocked! Please visit your nearest branch to unblock your card.")
        	break
        elif count==0:
        	pin = int(input("Enter your pin: "))
        	password = 1234
        else:
        	pin = int(input("Enter your pin again: "))
        	password = 1234
        if password != pin:
            print("Pin Incorrect!")
            count+=1
            print(f"You have {3-count} attempts remaining. \n")
            continue
        else:
            print("\n"+f"Your existing balance is: ₹{balance}")
            

    # if balance is displayed, it prompts the user to select between 1,2 or 3 for the next line of action that would be performed
    # if the user selects "1", it askes "how much" and then shows available balance by deducting the amount withdrawn from the initial balance
            #money = input("1: withdraw or 2: deposit or 3: exit: ")
            while True:
                money = input("\n1: withdraw \n2: deposit\n3: exit \n \nEnter your choice: ")
                if money == "1":
                    user_withdraw = int(input("Enter the amount you wish to withdraw: ₹"))
                    if user_withdraw > balance:
                        print("\nYou don't have sufficient funds.")
                        thanks()
                    else:
                        print('\n'+f"You have withdrawn ₹{user_withdraw} from your Account.")
                        balance = withdraw(balance, user_withdraw)
                        print(f"Your balance after withdrawal is: ₹{balance}")
                        thanks()

        # else if the user selects "2", it shows "how much" and then shows the total balance
                elif money == "2":
                    user_deposit = int(input("Enter the amount you wish to deposit: ₹"))
                    print(f"\nYou have deposited ₹{user_deposit} to your Account.")
                    if user_deposit > balance:
                        balance=deposit(balance, user_deposit)
                        print("Plenty money to spend!")
                        print(f"Your balance after deposit is: ₹{balance}")
                        thanks()
                    else:
                        balance=deposit(balance, user_deposit)
                        print(f"Your balance after deposit is: ₹{balance}")
                        thanks()

        # if user selects "3", thank you for banking with us!
                elif money == "3":
                    thanks()
                    break

                else:
                    print("Please Call The Security")
                    continue
        break

main()
