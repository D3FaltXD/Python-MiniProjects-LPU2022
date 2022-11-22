#DESCRIPTION:
#Email-Slicer: A program that extracts the username and domain from an email.

#DETAILS:
#The user will be asked to enter his/her email address.
#The program will format the input (to prevent some errors).
#The program returns the username and domain.

#CODE:
print('\t \t''\t''\t'"EMAIL SLICER")
def mail(n):
    for i in range(n):
        email = input("Enter your Email: ").strip()
        if '@' and '.com' not in email:
            print("Enter valid Mail ID")
            if n==1:
                mail(n)
            else:
                mail(n-(n-1))               
        else:
            l.append(email)
            n-=1
def checking():
    x=input("How many mails would you like to Slice:")
    if x.isnumeric():
        n=int(x)
        if n<=0:
            print("Enter a positive number")
            checking()
        else:
            mail(n)
    else:
        print("Enter an Integer")
        checking()
l=[]
checking()
if l!=[]:
    for i in l:
        username = i[:i.index('@')]
        domain = i[i.index('@')+1:]
        domain=domain.upper()
        print(f"your username is {username} & domain is {domain}")
        

