#leap year Program
year = int(input("enter the starting year: "))       # taking input from user for starting year
year2 = int(input("enter the ending year: "))        # taking input from user for ending year
s = []                                             # creating empty list
b = []                                             # creating empty list
for i in range(year,(year2)+1):                    # loop for starting year to ending year
    if i % 4 == 0:                                 # conditions for checking leap year or not
        if i % 100 != 0:
            s.append(i)                            # using append function to store value
                                                   # in the list
        elif i % 100 == 0:
            if i % 400 == 0:
                s.append(i)

            else:
                b.append(i)
    else:
        b.append(i)

print("leap year: ", s)                                            # printing leap year
print("Non leap year: " , b)                                        # printing non- leap years
