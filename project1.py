print("Welcome to the Interactive Personal Data Collector!", end="\n")

print(" ")

name = str(input("Please enter your name: "))
age = int(input("Pleas enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))

print(" ")

print("Thank you! Here is the information we collected:")

print(" ")

print("Name: ", name, " (Type: ", type(name), ", Memory Address: ", id(name),")", sep="")
print("Age: ", age, " (Type: ", type(age), ", Memory Address: ", id(age), ")", sep="")
print("Height: ", height, " (Type: ", type(height), ", Memory Address: ", id(height), ")", sep="")
print("Favourite Number: ", favourite_number, " (Type: ", type(favourite_number), ", Memory Address: ", id(favourite_number), ")", sep="")

current_year = 2025

dob = current_year - age

print(" ")

print("Your birth year is approximately: ", dob, " (based on your age of ", age, ")", sep="")

print(" ")

print("Thank you for using the Personal Data Collector. Goodbye!")
