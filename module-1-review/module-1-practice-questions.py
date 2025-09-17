"""
MODULE 1 PRACTICE QUESTIONS
===========================

This file contains practice questions for students to reinforce the concepts
learned in Module 1: Variables, Arithmetic Operations, and String Concatenation.

Instructions:
- Read each question carefully
- Write your code below each question
- Test your solutions by running the file
- Check your answers against the expected output when provided
"""

print("=" * 50)
print("MODULE 1 PRACTICE QUESTIONS")
print("=" * 50)

# =============================================================================
# SECTION 1: VARIABLE ASSIGNMENT
# =============================================================================

print("\n--- SECTION 1: Variable Assignment ---\n")

# Question 1.1
print("Question 1.1:")
print("Create a variable called 'age' and assign it the value 25.")
print("Then create a variable called 'city' and assign it the string 'Boston'.")
print("Print both variables.")
print("Expected output: 25, Boston")
print()

# Write your code here:
age = 25
city = 'Boston'
print(age, city, sep=', ')


print("=" * 30)

# Question 1.2
print("Question 1.2:")
print("Create three variables: 'first_name', 'last_name', and 'student_id'.")
print("Assign them appropriate values and print each one on a separate line.")
print()

# Write your code here:

first_name = "Amy"
last_name = "Apple"
student_id = 1234567
print(first_name)
print(last_name)
print(student_id)



print("=" * 30)

# Question 1.3
print("Question 1.3:")
print("Create a variable 'temperature' with the value 72.")
print("Then reassign it to 68 and print the new value.")
print("Expected output: 68")
print()

# Write your code here:
temperature = 72
temperature = 68
print(temperature)


# =============================================================================
# SECTION 2: ARITHMETIC OPERATIONS
# =============================================================================

print("\n--- SECTION 2: Arithmetic Operations ---\n")

# Question 2.1
print("Question 2.1:")
print("Given two numbers 15 and 4, calculate and print:")
print("- Their sum")
print("- Their difference (15 - 4)")
print("- Their product")
print("- Their quotient (15 / 4)")
print("- The remainder when 15 is divided by 4")
print("Expected output: 19, 11, 60, 3.75, 3")
print()

# Write your code here:
num1 = 15
num2 = 4
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
quot_result = num1 / num2
rem_result = num1 % num2
print(sum_result, diff_result, prod_result, quot_result, rem_result, sep=", ")


print("=" * 30)

# Question 2.2
print("Question 2.2:")
print("Calculate the area of a rectangle with length 12 and width 8.")
print("Store the result in a variable called 'area' and print it.")
print("Expected output: 96")
print()

# Write your code here:
length = 12
width = 8
area = length * width
print(area)



print("=" * 30)

# Question 2.3
print("Question 2.3:")
print("You have $50. You buy 3 items that cost $12.99 each.")
print("Calculate how much money you have left.")
print("Expected output: 11.03")
print()

# Write your code here:

initial_amount = 50
item_cost = 12.99
total_cost = 3 * item_cost
remaining_amount = initial_amount - total_cost
print(remaining_amount)


print("=" * 30)

# Question 2.4
print("Question 2.4:")
print("Calculate the average of these five test scores: 85, 92, 78, 96, 89")
print("Store the result in a variable called 'average' and print it.")
print("Expected output: 88.0")
print()

# Write your code here:
total = 85 + 92 + 78 + 96 + 89
average = total / 5
print(average)



# =============================================================================
# SECTION 3: STRING CONCATENATION
# =============================================================================

print("\n--- SECTION 3: String Concatenation ---\n")

# Question 3.1
print("Question 3.1:")
print("Create variables for your first name, middle initial, and last name.")
print("Concatenate them to create your full name and print it.")
print("Example output: John Q. Smith")
print()

# Write your code here:
first_name = "John"
middle_initial = "Q"
last_name = "Smith"
print(first_name + " " + middle_initial + ". " +last_name)



print("=" * 30)

# Question 3.2
print("Question 3.2:")
print("Create a greeting message that includes the user's name and age.")
print("Use variables: name = 'Sarah' and age = 20")
print("Expected output: Hello Sarah, you are 20 years old!")
print()

# Write your code here:
user_name = "Sarah"
user_age = 20
print(f"Hello {user_name}, you are {user_age} years old!")



print("=" * 30)

# Question 3.3
print("Question 3.3:")
print("Create variables for a book title and author.")
print("Print a message in the format: 'The book [title] was written by [author].'")
print("Example: 'The book To Kill a Mockingbird was written by Harper Lee.'")
print()

# Write your code here:
title = "game of Thrones"
author = "George R.R. Martin"
print(f"The book {title} was written by {author}.")


# =============================================================================
# SECTION 4: COMBINING CONCEPTS
# =============================================================================

print("\n--- SECTION 4: Combining All Concepts ---\n")

# Question 4.1
print("Question 4.1:")
print("Create a simple calculator program:")
print("- Create two number variables: num1 = 24, num2 = 6")
print("- Calculate all four basic operations")
print("- Print each result with a descriptive message")
print("Example: '24 + 6 = 30'")
print()

# Write your code here:

num1 = 24
num2 = 6
add = num1 +num2
minus = num1 - num2
multiply = num1 * num2
divide = num1 / num2

print(f"num1 + num2 is {add}")
print(f"num1 - num2 is {minus}")
print(f"num1 * num2 is {multiply}")
print(f"num1 / num2 is {divide}")


print("=" * 30)

# Question 4.2
print("Question 4.2:")
print("Create a program that calculates the tip for a restaurant bill:")
print("- Bill amount: $45.50")
print("- Tip percentage: 18%")
print("- Calculate the tip amount and total bill")
print("- Print both values with descriptive messages")
print("Expected: Tip: $8.19, Total: $53.69")
print()

# Write your code here:
bill_amount = 45.50
tip_pct = 0.18
tip_amount = bill_amount * tip_pct
total_bill = bill_amount + tip_amount
print(f"tip amount: ${tip_amount:.2f}, Total: ${total_bill:.2f}")



print("=" * 30)

# Question 4.3
print("Question 4.3:")
print("Create a student report card:")
print("- Student name: 'Alex Johnson'")
print("- Three test scores: 87, 92, 85")
print("- Calculate the average")
print("- Print a report showing the name, all scores, and average")
print("Format: 'Student: Alex Johnson | Scores: 87, 92, 85 | Average: 88.0'")
print()

# Write your code here:
student_name = "Alex Johnson"
score1 = 87
score2 = 92
score3 = 85
average = (score1 + score2 + score3)/3
print(f"Student: {student_name} | Scores: {score1}, {score2}, {score3} | Average: {average:.1f}")



print("=" * 30)

# Question 4.4
print("Question 4.4:")
print("Create a shopping receipt:")
print("- Item 1: 'Apples' - $3.99")
print("- Item 2: 'Bread' - $2.50")
print("- Item 3: 'Milk' - $4.25")
print("- Calculate subtotal, tax (8.5%), and total")
print("- Print a formatted receipt")
print()

# Write your code here:
item1 = "Apples"
item2 = "Bread"
item3 = "Milk"
price1 = 3.99
price2 = 2.50
price3 = 4.25
subtotal = price1 + price2 + price3
tax = 0.085 * subtotal
total = tax + subtotal
print("------------Receipt----------")
print(f"{item1:<15}${price1:>7.2f}")
print(f"{item2:<15}${price2:>7.2f}")
print(f"{item3:<15}${price3:>7.2f}")
print("-"*27)
print(f"{'Subtotal':<15}${subtotal:>7.2f}")
print(f"{'Tax(8.5%)':<15}${tax:>7.2f}")
print("-"*27)
print(f"{'Total':<15}${total:>7.2f}")


# =============================================================================
# SECTION 5: CHALLENGE QUESTIONS - NOT GRADED (OPTIONAL)
# =============================================================================

print("\n--- SECTION 5: Challenge Questions ---\n")

# Challenge 5.1
print("Challenge 5.1:")
print("Temperature Converter:")
print("Convert 75 degrees Fahrenheit to Celsius using the formula:")
print("Celsius = (Fahrenheit - 32) * 5/9")
print("Print the result with a descriptive message.")
print("Expected: 75°F is equal to 23.89°C")
print()

# Write your code here:
Fahrenheit = 75
Celsius = (Fahrenheit - 32) * 5/9
print(f"{Fahrenheit}°F is equal to {Celsius:.2f}°C")


print("=" * 30)

# Challenge 5.2
print("Challenge 5.2:")
print("Time Calculator:")
print("You have 3847 seconds. Convert this to hours, minutes, and seconds.")
print("Print the result in the format: 'X hours, Y minutes, Z seconds'")
print("Hint: Use integer division (//) and modulus (%) operators")
print("Expected: 1 hours, 4 minutes, 7 seconds")
print()

# Write your code here:

hours = 3847 // 3600
remaining_second = 3847 - hours * 3600
minutes = remaining_second // 60
seconds = remaining_second - minutes * 60
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")


print("=" * 30)

# Challenge 5.3
print("Challenge 5.3:")
print("Create a mad lib story:")
print("Create variables for: adjective, noun, verb, place, number")
print("Use them to create a funny story and print it.")
print("Be creative with your story structure!")
print()

# Write your code here:

adjective = "small"      
noun = "dog"         
verb = "crying"          
place = "Burger King"      
number = 2300              

print(f"Once upon a time, a {adjective} {noun} was {verb} in {place}, then another {number} {noun}s appeared and started singing!")


print("\n" + "=" * 50)
print("END OF PRACTICE QUESTIONS")
print("Great job practicing! Keep coding!")
print("=" * 50)
