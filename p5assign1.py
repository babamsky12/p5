#Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
#Ask for the grade
#Compute grade for the equivalent mark and description
#Print the mark and description

import math

grade = float(input("Enter your grade? "))

Grade=math.ceil(grade)

if grade <= 65:
    print("You got Inc., W, D mark.")
    print("Withdrawn")
    print("Study Harder!")

elif grade >= 65 and grade <= 74:
    print("You got 5.0 mark.")
    print("Failure")
    print("Study Harder!")

elif grade <= 75:
    print("You got 3.0 mark.")
    print("Passing")
    print("Study Harder!")
    
elif grade >= 76 and grade <= 78:
    print("You got 2.75 mark.")
    print("Satisfactory")

elif grade >= 79 and grade <= 81:
    print("You got 2.5 mark.")
    print("Satisfactory") 

elif grade >= 82 and grade <= 84:
    print("You got 2.25 mark.")
    print("Good")

elif grade >= 85 and grade <= 87:
    print("You got 2.0 mark.")
    print("Good")

elif grade >= 88 and grade <= 90:
    print("You got 1.75 mark.")
    print("Very Good")
    
elif grade >= 91 and grade <= 93:
    print("You got 1.5 mark.")
    print("Very Good")

elif grade >= 94 and grade <= 96:
    print("You got 1.25 mark.")
    print("Excellent")

elif grade >= 97 and grade <= 99:
    print("You got 1.0 mark.")
    print("Excellent")

else: 
    print("Success")

