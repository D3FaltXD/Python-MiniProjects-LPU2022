#Program to check a random number

import random
def prime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

a=int(input("Enter Upper limit: "))
b=int(input("Enter lower limit: "))
x=random.randint(a,b)
print("\n")
print("Range is (%d,%d) and randomly picked number is %d"%(a,b,x))
if(x%2==0):
    print("%d is an even number"%x)
else:
    print("%d is an odd number"%x)
if(x==1):
    print("1 is netiher a prime number nor composite number")
elif(prime(x)):
    print("%d is a prime number"%x)
else:
    print("%d is a composite number"%x)