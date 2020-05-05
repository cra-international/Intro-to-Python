"""
Section 4: Functions and Packages
------------------------------------------------------

At the end of section three, we introduced the 'import' function and the 
Python 'random' package. In this section we will explain about Python 
packages and also how to write your own functions.  

"""

#%% Part 1: Packages
#Packages, also known as libraries or modules, are external pre-packaged
#Python scripts that can imported in order to quickly and concisely expand
#Python's functionality. Some packages, such as 'random' and 'math' come
#with your Python installation, while others are written externally and
#need to be downloaded to your computer. For now, we will work with the
#built-in Python packages.

#In section 2, we covered basic mathematical operations in Python. What if,
#however, we wanted to use more complex mathematical functions such as log?
#That function, while not native to Python per se, is part of Python's 'math'
#library, and could be accessed in the following way
import math
log_10 = math.log10(10)

#Note that functions derived from packages follow the following syntax - 
#<package name>.<function name>()

#If you know which function of package you'd like to use and don't want
#to constantly type the package name before each function call, you can also
#import the function directly by typing
from math import log10
log_100 = log10(100)

#How do you learn more about a package? Good package developers provide a 
#multitude of ways for you to learn more about a package or function. 
#The most common way is online documentation. For example, a simple Google
#search of 'math package python' yields the following website 
#https://docs.python.org/3.7/library/math.html
#This website provides a list of all of the functinos assocaited with the
#math package and also explanations of how each function is used. 

#Many package developers include inline documentation as well, which
#is documentation included in the Python source code. You can access this
#documentation in Spyder by simply holding "cntrl" and hovering over the
#package or function of interest.

#Now you try! Go to the documentation website for the random package
#by clicking on this url - https://docs.python.org/3.7/library/random.html
#Then, write code using this package that returns a random number
#between 0 (inclusive) and 1 (not inclusive)

import random

rand_float = random.random()

#%% Writing Your Own Function
#What if rather than import a function from elsewhere, you want to write
#your own function? That is easily done in python with the def command
#For example, we can wrap the while loop we wrote in Section 3 in a 
#function that returns the number of flips it took to get a heads. 

import random

def count_flips():
    heads = False
    flips = 0
    while not heads:
        num = random.randint(0, 1)
        if num == 1:
            heads = True
        flips += 1
    print("It took {} flips to get a heads".format(flips))

num_flips = count_flips()

#Note a couple of things about the above code. Firstly, note that the 
#import statement is outside of the function definition. That is because
#we only need import the random package once, we don't want to import it
#every time we call the function. Next, we define the function by writing
#'def <function name>():'. Defining the function is pretty simple! Note
#that the function name cannot have any spaces. After defining the function,
#we indent the code so that Python knows which code to include in the function.
#(Luckily, most Python IDEs, like Spyder, do this automatically!)
#This is simlar to the if/else statements we encountered in Section 2.
#Finally, at the end of the function, we return a variable using the 
#return statement. This is the Python object or variables that we want to pass
#along to a variable at the end of the function, in this case the number of 
#coin flips it took to get a heads. 

#Does every function have to return something? Nope! In the count_flips() 
#function above, delete the return statement and instead print the number
#of coin flips it took to get a heads to the console. Then, run the code that
#assigns the output of the count_flips() fucntion to the variable num_flips.
#What is the value of num_flips? Did the print statement print?

#One additional thing to note about the above function count_flips() is that
#it has no arguments, meaning the user doesn't provide any inputs to the function.
#How would we define a function with arguments? Below, we define a new function
#called count_tries() which requires one argument (p). This function is nearly 
#identical to the function above, but instead of always having a 50% chance
#of a success, like flipping a heads with a coin, this function requires the 
#user pick the probability of success. 

def count_tries(p):
    success = False
    tries = 0
    while not success:
        success = random.random() <= p
        tries += 1
    return tries

num_tries = count_tries(0.1)

#%% Part3: Variables and Packages as both Python Objects

#We didn't define it explicitly, but in Part 1 we introduced the 
#dot operator, which in the case of "math.log10(x)" is the period in between
#math and log10. The dot operator, more generally, accesses a Python object's
#functions or attributes. We will talk about attributes in Python Part II, but
#below we'll show you that many of the basic Python object we introduced in
#sections 1-3 actually have functions associated with them that can be 
#accessed with the dot operator. 

#For example, string functions have two helpful functions

lower_case_str = "HELLO WORLD!".lower() #Return a lowercase version of the str
upper_case_str = "hello world!".upper() #Return an uppercase version of the str
no_commas = "Hello, World!".replace(",", "") #Replace values 
trimmed_str = " Hello World! ".strip() #Remove leading/trailing spaces

#Now you try! Call the .split() method on "Hello World!" and assign the output
#to the variable split_str. What did this function do?

split_str = "Hello World!".split()

#Lists also have a couple very helpful built-in methods. For example,
#we showed that object can be added to lists by using the addition operator.
#We can also add items to lists using the.append() method. 
letters = ["a", "b", "c"]
letters.append("d")
print(letters)

#You'll notice that he .append() method, however, does NOT return a new 
#Python object. Rather it modifies the object in place. What happens
#then, if we try to assign the output of the .append() method to a variable
numbers = [1, 2, 3]
new_numbers = numbers.append(4)
print(new_numbers)

#In this case, the .append() command returns None, just like when we 
#removed the 'return' statement from the count_flips() function but
#tried to assign the output to a new variable. 

#Lists have a few other functions that can be very helpful, such as .sort() 
#and .remove(), both shown below. Note that these two function also modify
#their associated list in place rather than return a new copy
example_list = ["b", "a", "d", "c", "a", "t"]
example_list.sort()
example_list.remove("a")

#Note that the .sort() function sorts the list based on the type of data in the
#list, in this case character/string data. The .remove() method removes one
#instance of the value passed to the function, even if multiple instances exist

#Now you try! Below, write a function called alt_caps that takes a string
#as an input and returns a string where characters alterate between
#uppercase and lowercase. Hint: Remember that strings are iterables!

def alt_caps(string):
    out_str = ""
    upper = True
    for s in string:
        if upper:
            out_str += s.upper()
            upper = False
        else:
            out_str += s.lower()
            upper = True
    return out_str

cra = "Charles River Associates"
print(alt_caps(cra))
