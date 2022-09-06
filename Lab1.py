#Notes from first lab
#Declare a string/str
name = "Kendrick"
#Declare an integer/int 
age = 23
#Example of another str 
age = "23" 
########
number1 = 34
number2 = 56543
print(number1)
#We can either +,-,*,or /.
print(number1 * number2) 
#Declare a float 
number3 = 23.4 
#Whenever you add an int and a float you're always going to get a float. 
print(number3 + number1) 
#########
name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
final_age = age * 35
print("Name:", name) 
print("Lastname:", last_name)
print("Final age:", final_age)
##########
#Lab: Part 1a
#Declare a variable for human age 
human_age = 2
#Declare a variable for dog year 
dog_year = 7
#Declare a variable that will calculate the human age in dog year.
human_in_dog_year = human_age * dog_year
#Now print out the value of the human age in dog year with a statement. 
print("An age", human_age, "human should be", human_in_dog_year, "in dog years.") 
#######
#Lab: Part 1b 
#Declare a variable for human age 
human_age1 = float(input("Enter your age:")) 
#Declare a variable for dog year
dog_year1 = 7 
#Declare a variable that will calculate the human age in dog year 
human_in_dog_year1 = human_age1 * dog_year1 
#Declare a variable that will get the rounded up value for the human age in dog year 
final_human_in_dog_year = int(human_age1 * dog_year1)
#To get the age in months we substract the rounded up value from the initial value
age_in_months = human_in_dog_year1 - int(human_in_dog_year1 ) 
#To get the final age in months we multiply the difference by 12 
final_age_in_months = 12 * age_in_months  
#The value of the final age must be a whole number so the int function will be added next to the final value.
final_age_in_months1 = int(12 * age_in_months)
#To get the value to calculate in days we must substract the two values of age in months. 
age_in_days = final_age_in_months - final_age_in_months1 
#To get the final value we must multiply the difference by 30 to get the value in days 
final_age_in_days = 30 * age_in_days 
#The final days must be a whole number so the int function will be added next to the final value. 
final_age_in_days1 = int(30 * age_in_days)
#Now we print the values of our calculation in text. 
print(f"An age", human_age1, "human should be", final_human_in_dog_year, "years", final_age_in_months1, "months and", final_age_in_days1, "days in dog age.")
#########
#Lab: Part 2a
#Declare a variable for the value of human years 
human_years = 18
#Declare a variable for the value of cat years 
cat_years = 9 
#Declare a variable that gets the value of cat in human years 
cat_in_human_years = human_years / cat_years 
#Print out the value of cat in human years in a statement 
print("An age", human_years, "human should be", cat_in_human_years, "in cat age.")
#######
#Lab: Part 2b
#Declare a variable for human years 
human_years1 = float(input("Enter your age:"))
#Declare a variable for cat years 
cat_years1 = 9 
#Declare a variable that will calculate the human years in cat years 
human_in_cat_years1 = human_years1 / cat_years1 
#Declare a variable that will get the rounded up value for the human in cat years 
final_human_in_cat_years = int(human_years1 / cat_years1)
#To get the age in months we subtract the rounded up value from the initial value. 
human_age_in_months = human_in_cat_years1 - final_human_in_cat_years 
#To get the final age in months we multiply the difference by 12
final_human_age_in_months = 12 * human_age_in_months 
#The value of the age in months must be a whole number so the int function must be added. 
final_human_age_in_months1 = int(12 * human_age_in_months)
#To get the value to calculate the age in days we must subtract the two values of the age in months 
human_age_in_days = final_human_age_in_months - final_human_age_in_months1 
#To get the final value of the age in days we must multiply the difference by 30 
final_human_age_in_days = 30 * human_age_in_days
#The value of the final age in days must be rounded up so we add the int function. 
final_human_age_in_days1 = int(30 * human_age_in_days) 
#Now we print out the final values of our calculation in text. 
print("An age", human_years1, "human should be", final_human_in_cat_years, "years", final_human_age_in_months1, "months and", final_human_age_in_days1, "days in cat age.")
#########
#Lab: Part 3a
#Declare a variable for the human age 
age_of_human = int(input("Enter value of the human age:"))  
#Declare a variable for the horse age that calculates the age of the horse when the human age is given.
horse_age = round(3 * ((((age_of_human**2)-47)/7)+12), 2)   
#Print the value of the horse's age in text. 
print(f"An age", age_of_human, "human should be about", horse_age, "in horse age.") 
########
#Lab: Part 3b 
#To get the value of the horse age in years 
horse_age_in_years = int(horse_age)
#To get the value of the horse age in months 
horse_age_in_months = horse_age - horse_age_in_years 
#To get the final value 
final_horse_age_in_months = 12 * horse_age_in_months 
#The final value must be a whole number 
final_horse_age_in_months1 = int(12 * horse_age_in_months) 
#To get the value of the horse age in days 
horse_age_in_days = final_horse_age_in_months - final_horse_age_in_months1 
#To get the final value 
final_horse_age_in_days = 30 * horse_age_in_days 
#The final value must be a whole number 
final_horse_age_in_days1 = int(30 * horse_age_in_days) 
#Print out the final values in text 
print("An age", age_of_human, "human should be about", horse_age_in_years, "years", final_horse_age_in_months1, "months and", final_horse_age_in_days1, "days in horse age." )
"""
12 months = 1 year 
x months = .7 years 
months = 8.4 

30 days = 1 months 
x days = .4 months 
days = 12 

"""
