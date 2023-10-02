# Conditional statments in Python
# We are checking if a number is posative, negative or zero
# Taking number from user ans storing it in a variable
num = int(input("Enter a number: "))

if num < 0:   # Checking if number is smaller than zero
  print("Negative number")
elif num > 0:    # We are chcking if number is greater than zero, it wont be checked if the first condition will be true
  print("Posative number")
else:     # If both of above conditions are false
  print("Its Zero!!!")
