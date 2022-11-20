#Acronym program
# Taking in put from user
user_input = str(input("Enter a Sentence: "))
# making list of words
text = user_input.split()
# Creating empty string
a = " "
# Acessing each word one by one using for loop
for i in text:
# Taking first letter of word and converting to uppercase
    a = a+str(i[0]).upper()
#printing acronym
print(a)