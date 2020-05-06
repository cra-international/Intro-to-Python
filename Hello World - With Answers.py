"""
Section 1: The print statement and basic Python variable types
------------------------------------------------------

Welcome to Python! Below, we introduce your first two Python concepts - 
print statements and variable assignment

In Python, information can be printed to the console using the print() function.
Below, we print "Hello World!" to the console, the obligitory first step
of learning any programming language.

After that, we introduce variable assignment and explore the basic types of 
variables that can be created in Python.

If you are executing this code in Spyder, you should see that the code below
is separated into parts, with the beginning of each part denoted by #%%.
To execute the code that comprises one part only, click into the part and
press cntrl+Enter. 

To execute only select lines of code, highlight the lines with your cursor
and click F9.

Lines that begin with a number sign (#) are called comments, and will
ignored by Python when the code is executed.
"""
#%% Part 1: The Print Statement

#The print function is a built-in Python function that prints text to the console
#Below, we print "Hello World!" to the console
print("Hello World!")

#Now you try! Replace "<your name here>" with your name and run the code below
print("Hi! My name is Christian!")

#%% Part 2: Variable Assignment

#In Python, values can be stored in variables in order to be referenced later.
#Variables are created using the equals sign (=).
#In the code below, we first store "Hello World!" as a variable called 'hello_world' 
#and then print the variable 'hello_world to the console

hello_world = "Hello World!"
print(hello_world)

#Now you try! Replace "<today's date>" with today's date and then print the 
#'date' variable using the print() statement
date = "March 13, 2020"
print(date)

#We will explore the basic types of Python variables below

#%% Part 3: Basic Variable Types in Python

#In Part 2 above, 'hello_world' is a specific type of variable, in this case a string variable.
#Strings are text variables and can be created in Python  with double or single quotes
#Double quotes can be used if you want to include a single quote in the string 
#and vice versa
str1 = "I'm a string!"
str2 = 'I am also a string!'

#There are 4 other basic data types in Python, many of which you may already 
#be familiar with:
# Integers
# Floats
# Booleans
# Nonetype

#Below, we create variables of each type
integer = 5
floater = 5.5
boolean = True
Nonetype = None

#Note: Boolean variables take two variables - True and False
#We'll encounter these types of variables more later. 

#How do we know that that these variables are the correct types? 
#The type() function is a built-in Python function (like print) which returns 
#the type of a specific variable.
#Below we combine type() and print() to identify the types of each variable
print(type(integer))
print(type(floater))
print(type(boolean))
print(type(Nonetype))

#One of the differences of Python as opposed to programming langauges like Java
#is that in Python, variables can freely switch between types.
#For example, we can change the Nonetype variable to a string
Nonetype = "Nothing to see here"
print(type(Nonetype))

#Now you try! Below is some code that asks for user input. To respond,
#click into the console and type your response. Then press enter. After that,
#write code that checks the type of the variable 'user_input'.
user_input = input("How's your day going? ")
print(type(user_input))

#%% Part 4: Variable Type Conversions

#What if we had a number stored as a string that we wanted to be just a number?
#In that case, we'd use the int() or float() built-in constructor functions to
#convert the string to a number, as below
string_number = "42"
int_number = int(string_number)
float_number = float(string_number)

#If we wanted to convert one of those numbers back to a string? You guessed it, 
#there is a str() function
string_again = str(int_number)

#There's even a bool() function, which converts numbers and strings to True/False
#All non-zero numbers are True, zeroes are False
print(bool(5))
print(bool(0))

#Now you try! Write code below to print the value of "Hello World!" converted
#to a boolean. Can you guess what string value might be False?
print(bool("Hello World!")) #True
print(bool("")) #False

