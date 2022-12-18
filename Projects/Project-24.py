date1 = input("Enter your starting year in (dd/mm/yy): ")                     # taking input from user for starting year
date2 = input("Enter your ending year in (dd/mm/yy): ")                       # taking input from user for ending year
d1 = date1.split("/")
d2 = date2.split("/")
y1 = int(d1[2])
y2 = int(d2[2])
leap = []                                                                 # creating empty list
non_leap = []                                                             # creating empty list
for i in range(y1, y2+1):                                             # loop for starting year to ending year
    if i % 4 == 0:                                                  # conditions for checking leap year or not
        if i % 100 != 0:
            leap.append(i)
        else:
            if i % 400 == 0:
                leap.append(i)                                      # using append function to store value in the list
            else:
                non_leap.append(i)
    else:
        non_leap.append(i)
print("Leap years are:",leap)                                         # printing leap year
print("Non-Leap years are:",non_leap)                                 # printing non- leap years


        
