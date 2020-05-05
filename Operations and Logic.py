"""
Section 2: Other Python Operators, Logic, and Conditionals.
------------------------------------------------------

In Section 1, we introduced you to the main python assignement  
operator - the equals sign [=]. In this section, we will introduce you to
the other Python operators as well as Python logic.

First we'll start with Python's arithmetic operators.
"""
#%% Part 1: Python Arithmetic Operators

#As you would expect, addition, subtraction, multiplication, and division
#are all defined in Python
x = 4
y = 2

a = x + y #Addition
b = x - y #Subtraction
c = x * y #Multiplication
d = x / y #Division

print(a, b, c, d)

#Python also includes exponentiation, the mod operator, and floor division
j = 7
k = 3

e = j**k #Exponentiation
f = j%k #Moding (returns the remainder)
g = j//k #Floor division (The quotient rounded down to the nearest integer)

print(e, f, g)

#Python's arithmetic operators are defined for some other variable types,
#such as strings. For example, two or more strings can be concatenated 
#together using the addition (+) operator, as below

hello_world = "Hello" + " " + "World" + "!"

#Strings can even be multiplied!
echo = "Hello..." + " hello..." * 3

#String addition can be combined with the str() function to print non-string
#output. For example,
cents = 500
dollars = cents / 100
print("I have " + str(dollars) + " dollars")

#%% Part 2: Combined Arithmetic and Assignment Operators

#In Python, you can actually combine arithmetic and assignment operators
#to update existing variables with one operation

#Conventional way to increment by one
m = 5
m = m + 1
print(m)

#Other way to increment by one, combine + and = into +=
n = 5
n += 1 
print(n)

#Now you try!
#Combine the exponentiation operator and the equals sign to cube the variable 'rubiks' below

rubiks = 3
#Cube rubiks

print(rubiks)
#Note: These combined operators are defined for all seven arithmetic operators

#%% Part 3: Comparison Operators

#In Python all six typical comparison operators are defined

eq = 5 == 5 #Equals comparison
lt = 5 < 5 #Less than comparison
gt = 5 > 5 #Greater than comparison
lt_or_eq = 5 <= 5 #Less than or equals to comparison
gt_or_eq = 5 >= 5 #Greater than or equals to comparison
not_eq = 5 != 5 #Not equals to comparison

#In the above code, the result of each comparison was assigned to a variable.
#Can you think what variable type those variables might be?
#Lets print some values and types of the variables above to find out.
print("The value of eq is:", eq)
print("The value of lt is:", lt)
print("eq is of type", type(eq))
print("lt is of type", type(lt))

#It looks like the variables created above are all boolean values!
#Remember, from Section 1, boolean variables take the values True or False
#We will discuss these variables in more depth in Part 4 below

#There is one more comparison operator specific to Python, and that's 'is'
#The operator 'is' is a stronger comparison than the == operator. It checks
#whether are not just equal, but are identical in variable type and their
#location in Python memory. See below for an example of where == might be
#true but 'is' would be False. 

check1 = 9 == 9.0
check2 = (9 is 9.0)
print(check1, check2)

#'is' is typically used in conjunction with checking variables types. Such as
check3 = type(9.0) is float
print(check3)

#%% Part 4: Boolean Logic and Logical Operators in Python

#As we saw above, boolean variables take one of two values - True or False
#Combined with Python's logical operators, we can use these values to 
#create complex logical expressions

#The logical operators in Python are 'and', 'or', and 'not'
#We will see how these are defined and applied below

#The 'and' operator checks if two conditions are both True
#If at least one condition is False, the expression evaluates to False 

t_and_t = True and True #Evaluates to True
t_and_f = True and False #Evaluates to False
f_and_f = False and False #Evaluates to False

print(t_and_t, t_and_f, f_and_f)

#The 'or' operator checks if at least one of two conditions is True

t_or_t = True or True #Evaluates to True
t_or_f = True or False #Evaluates to True
f_or_f = False or False #Evaluates to False

print(t_or_t, t_or_f, f_or_f)

#The 'not' operator returns the opposite of the boolean
not_t = not True #Evaluates to False
not_f = not False #Evaluates to True

print(not_t, not_f)

#Logical operators have an associated order of operations
#'not' is evaluated first, then 'and', and then lastly 'or' 

expression1 = True or False and False or False #Evaluates to True.
expression2 = False or False and True or False #Evaluates to False

#But, like arithmetic, expressions in parentheses are always evaluated first
#Below is expression 1, but with parentheses around the first 'or'
expression3 = (True or False) and False or False #Evaluates to False

#Therefore, I reccomend ALWAYS putting logical statments in parentheses
#in the order you wish them to be evaluates. It easier easier for you to
#understand as well as easier for others reading your code to understand

#Now you try! Write a logical expressions that evaluates to True and
# contains the following:
#  4 'False's 
#  1 'True'
#  3 'and's
#  1 'or'

#answer = ...

# %% Part 5: Combining Logical and Comparison Operators

#Rarely will programmers use raw boolean values like True or False as part
#of their expressions. Rather, programmers will use the logical operators
#in coordination with comparison operators to evalute expressions.

#For example, say we had

x = 3
y = 5
z = 1

#Then we might be interested in the following expression:
expression4 = x < y and z > y

#Note that in the order of Python operations, comparison operators like
#less than (<) or greater than (>) are always evaluated before logical operators.

#Now you try! Write an expression that checks if a is not equal to b or 
#a is not less than c

a = 4
b = 2
c = 7

#answer2 = 

#%% Part 6: Conditional statements 

#Knowing if an expression is True or False can be very useful if you'd like 
#to take an action based on the result, such as sending an 
#e-mail only if the e-mail isn't empty or if there is a listed recipient

#This is possible in Python through the use of conditional statements, also
#known as if/then/else statements. See below for an example.

p = 20
q = 5

if q > p:
    print("q is greater than p")
else:
    print("q is less than or equal to p")

#In the above example, the first statement, the 'if' statement, is evaluated first.
#In this case, q > p is False, which causes the 'else' statement to be triggered.

#Conditional statements like 'if' and 'else' end in colons and are then 
#followed by indented text. The indentation exists in order to
#differentiate the code that is part of the conditional from
#the rest of the code in your python file. We will see this structure again
#when we learn about function definitions.

#So what if we have more than one condition we want to test? Say, if we want to
#test if q is greater than p, q is equal to p, or if q is less than p, all separately?
#In that case, we can add additionl 'elif' statements, short for "else if",
#in between the initial 'if' and concluding 'else' statements. 

#For example, we could do the following:
if q > p:
    print("q is greater than p")
elif q == p:
    print("q is equal to p")
else:
    print("q is less than p")

#Now you try! Use Python's len() function to compare the length of the strings below.
#Then, based on the string lengths, print an appropriate statement, 
#such as "string 1 is longer than string 2" if the length of string1 is 
#greater than the length of string2

string1 = "We are the knights who say 'Ni!'" 
string2 = "We demand a sacrifice! We demand... a shrubbery!"

#Fun fact, Python is actually named after the British comedy group Monty Python
#The above quotes are from arguably their most famous movie, Monty Python and the Holy Grail



