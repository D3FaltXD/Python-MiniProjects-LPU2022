import os
def help(x):
    c= x.split(":")
    return int(c[-1])
list1=[]
stu_no=int(input("No. of Students: "))
for i in range(stu_no):
    n=input("Name: ")
    m=input("Marks: ")
    print()
    c=n+":"+m
    list1.append(c)
list1.sort(key=help,reverse=True)
print(list1)
print()
print()


############################     LOOP STARTS HERE       ########################

while True:
    c=0
    print("Menu :")
    print()
    print('''1.) Display the Student's Marks with Rank ''')
    print('''2.) Update and display the student Rank''')
    print('''3.) Display the specific student's Rank''')
    print('''4.) Clear the screen''')
    print('''5.) Exit''')
    print()
    a=input("Enter your choice: ")
    print()
    if a=="1":
        print()
        for i in list1:
            c=c+1
            print("Rank =",c)
            zz= i.split(":")
            
            print("        Name:",zz[0])
            print("        Marks:",zz[-1])
            print()


#######################     UPDATION IN MARKS       ########################

    elif a=="2":
        n=input("Name: ")
        m=input("Marks: ")
        print()
        ap=n+":"+m
        print("The updated list :")
        for j in list1:
            if n in j:
                del list1[c]
                list1.append(ap)
                list1.sort(key=help,reverse=True)
                break
            c=c+1
        print()
        print()
        rank=1
        for x in list1:
            print("Rank:",rank)
            zz=x.split(":")
            print("        Name:",zz[0])
            print("        Marks:",zz[-1])
            print()
            rank=rank+1

    elif a=="3":
        nm_rank=1
        n=input("Enter Name: ")
        print()
        for i in list1:
            if n in i:
                zz=i.split(":")

                print("Name:",zz[0])
                print("        Marks:",zz[-1])
                print("        Rank:",nm_rank)
            nm_rank=nm_rank+1
        print()
    elif a=="4":
        os.system('cls')
    elif a=="5":
        break