"""
Your Name: Regina Mayiie Kamara
Date: 9/9/2022

Description of what this program does:
The calculator calculates the tax owed based on the individual's earned income and marital status. 
"""
import sys


taxOwed = 0.0

earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")


#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")




# Your code goes here
if earnedIncome <= 9950 and maritalStatus == "s":
	taxOwed = earnedIncome * 0.1
	print("This year you owe", taxOwed, "in taxes") 
elif earnedIncome <= 19900 and maritalStatus == "m":
	taxOwed = earnedIncome * 0.1
	print("This year you owe", taxOwed, "In taxes" )
elif earnedIncome >=9951 and earnedIncome <= 40525 and maritalStatus == "s": 
	taxOwed = 0.12 * (earnedIncome - 9950) + (0.1 * 9950)
	print("This year you owe", taxOwed, "in taxes") 
elif earnedIncome >=19901 and earnedIncome <= 81050 and maritalStatus == "m":
	taxOwed = 0.12 * (earnedIncome - 19900) + (0.1 * 19900)
	print("This year you owe", taxOwed, "in taxes")
elif earnedIncome >=40526 and earnedIncome <= 86375 and maritalStatus == "s":
	taxOwed = 0.22 * (earnedIncome - 40525) + (0.12 * 30574) + (0.1 * 9950)
	print("This year you owe", taxOwed, "in taxes")
elif earnedIncome >= 81051 and earnedIncome <= 172750 and maritalStatus == "m":
	taxOwed = 0.22 * (earnedIncome - 81050) + (0.12 * 61150) + (0.1 * 19900)
	print("This year you owe", taxOwed, "in taxes") 
else:
	print("You made too much for the calculator this year. Hooray!") 



	







