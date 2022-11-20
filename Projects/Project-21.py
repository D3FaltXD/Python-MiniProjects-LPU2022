# Cake Question


cakeangle=eval(input("Enter the Angle of the Cake: "))
N=eval(input("Enter N: "))
if(cakeangle%N==0):
    print("YES the cake will cut in equal pieces of size %d"%N)
else:
    print("NO the cake will not cut in equal pieces of size %d"%N)
if(N>cakeangle): #Only when N is greater tha cake angle cake can't be cut into pieces
    print("NO the cake will not cut in any piece of size %d"%N)
else:
    print("YES the cake will cut in any piece of size %d"%N)
n=1 # start subratcrting the cake
for i in range(N):
    cakeangle-=n
    n+=1
    if(cakeangle<0):
        print("NO the cake will not cut into %d pieces such that no two of them are equal"%N)
        break
else:
        print("YES the cake will cut into %d pieces such that no two of them are equal"%N)
    