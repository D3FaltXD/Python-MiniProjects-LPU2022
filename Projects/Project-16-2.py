# Python3 program two find number of
# days between two given dates

# To store number of days in all months from January to Dec.
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# This function counts number of leap years before the given date
def countLeapYears(d):

	years = d[2]
	# Check if the current year needs to be considered for the count of leap years or not
	if (d[1] <= 2):
		years -= 1

	# An year is a leap year if it is a multiple of 4, multiple of 400 and not a multiple of 100.
	ans = int(years / 4)
	ans -= int(years / 100)
	ans += int(years / 400)
	return ans

# This function returns number of days between two given dates
def getDifference(birth_date, current_date):

	# COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'birth_date'
	# initialize count using years and day
	n1 = birth_date[2] * 365 + birth_date[0]

	# Add days for months in given date
	for i in range(0, birth_date[1]-1):
		n1 += monthDays[i]

	# Since every leap year is of 366 days,
	# Add a day for every leap year
	n1 += countLeapYears(birth_date)

	# SIMILARLY, COUNT TOTAL NUMBER
	# OF DAYS BEFORE 'current_date'
	n2 = current_date[2] * 365 + current_date[0]
	for i in range(0, current_date[1]-1):
		n2 += monthDays[i]
	n2 += countLeapYears(current_date)

	# return difference between two counts
	return (n2 - n1)


# Driver Code
a = "y"
while a.lower() == "y":
	try:
		dob=input("Enter your Date of Birth as DD/MM/YYYYY : ")
		dob=[int(i) for i in dob.split("/")]
		PD=input("Enter Present Day as DD/MM/YYYYY : ")
		PD=[int(i) for i in PD.split("/")]
		if(dob[1] == 13 or PD[1] == 13):
			print("Please enter a valid date")
		elif sum(dob) < sum(PD):
			print("\nThe number of days the person is alive:", getDifference(dob, PD))
		else:
			print("Date of birth is more than present date")
	except ValueError:
		print("Enter date only in the given format")
	except IndexError:
		print("Please enter a valid date")
	a = input("\nDo You Want to Continue? (Y/N) : ")
print("\nEXIT")


