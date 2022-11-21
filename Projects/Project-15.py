print("\nWelcome :)\n")
x=int(input("x: "))
y=int(input("y: "))
s=0
g=0
if x<y:
    for i in range(x,y+1):
    
        a=i
        c=0
        for j in range(2,a):
            if a%j==0:
                c=1
                s+=1
                print(f"{a} is composite")
                break
        if c==0:
            print(f"{a} is Prime")
            g+=1
    print(f"There are total {g} prime numbers, and {s} composite numbers in the given Range.")
else:
    print(f"INVALID RANGE!")
   
