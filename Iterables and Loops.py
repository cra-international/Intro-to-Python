"""
Section 3: Iterables and Loops
------------------------------------------------------

In section one, we went over the basic Python variables: integers, floats,
booleans, and strings. Now, we'll cover the more complex data types of
lists and dictionaries. We'll also discuss iteration, for and while loops, 
and iterables.
"""
#%% Part 1: Lists

#A list is a ordered and mutable collection of other Python variables
#For example, we may want to make sure a user, when typing in their date of 
#birth, typed in a valid month. If so, we can build a list of months to 
#reference their input against like so

valid_months = ["January", "Febuary", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", 
                "December"]

#Just as double and single-quotes are used to create strings, brackets
#are used to create lists. 

#Lists are indexable, which means individuals elements can be accessed by
#their position in the list. Lists are zero-indexed, meaning the index
#starts at zero rather than one. Therefore, we can assign "January" to
#the variable first_month using indexing as below

first_month = valid_months[0]

#Note that indexing follows a specific structure - the name of the variable
#followed by the index number in brackets

#Additionally, lists are mutable, which mean that we can also use indexing to 
#change values in a list. It looks like "February" is misspelled in the
#valid_months variable. That value can be updated by doing the following - 

valid_months[1] = "February" #Remember, the second position = index 1

#Multiple items in a list can be accessed by including a range of indices,
#where the range is the beginning index, followed by a colon, followed by
#an ending index, not inclusive.
#Below, the fourth, fifth, and sixth items of the list are taken
#and stored (in their old order) into a new list called spring months

spring_months = valid_months[3:6] #Remember, the upper end of the range is not inclusive

#If a number is not specified on right side of the colon, all values from the
#beginning index to the end of the list are accessed. Similarly, if no index
#is specified on the left side of the colon, all values from the beginning of 
#the list to the ending index (not inclusive) are accessed.

early_months = valid_months[:6]
later_months = valid_months[6:]

#Lists also support negative indexing, such as below
non_fall_months = valid_months[:-3]

#Now you try! Below is a list of the top 10 picks of the 2020 NFL draft.
#Use your knowledge of lists to create the variables below.

top_10_players = ["Joe Burrow", "Chase Young", "Jeff Okudah", "Andrew Thomas", 
               "Tua Tagovailoa", "Justin Herbert", "Derrick Brown", 
               "Isaiah Simmons", "C.J. Henderson", "Jedrick Wills"]

#top_pick = 
#picks_3_to_5 = 
#top_5_picks = 
#picks_6_to_10 = 
#first_9_picks = 

#A Few More fun facts on Lists!
#Lists are type agnostic, meaning the variables stored in a list can be of
#any type, even other lists!

random_list = [1, "a", True, 3.5, None, ["a", "b", "c"]]

#Also, addition and multiplication are defined for lists. Addition of 
#two lists is a new list created in left-to-right order and multiplication
#by n is the same as adding the same list to itseld n-1 times

abc = ["a"] + ["b"] + ["c"]
aaa = ["a"] * 3

#%% Part 2: Dictionaries

#As discussed above, lists are mutable and ordered and designed to be used in
#conjunction with positional indexing. Dictionaries, on the other hand,
#are mutable collections of unordered Python key-value pairs and designed 
#to be used in conjunction with key indexing

#Below is a dictionary of the top 10 picks in the NFL draft, where the key
#is the player's name and the value is their college

college_teams = {"Joe Burrow" : "Louisiana State University",
                 "Jeff Okudah" : "Ohio State",
                 "Tua Tagovailoa" : "Alabama",
                 "Chase Young" : "Ohio State",
                 "Andrew Thomas" : "Georgia",
                 "Justin Herbert" : "Oregon",
                 "Derrick Brown" : "Auburn",
                 "Isaiah Simmons" : "Clemson",
                 "C.J. Henderson" : "Florida",
                 "Mekhi Becton" : "Louisville"}

#Dictionaries are created using curly brackets and each entry is a 
#key-value pair where the key is separated from the value by a colon. 
#Key-value pairs are then separated from other pairs with a comma. 

#Note that while keys MUST be unique in dictionaries, values don't have to be

#With a dictionary, we can get a value for a specific key, like below
tua_school = college_teams["Tua Tagovailoa"]

#And like lists, we can modify specific values. For example, let's change
#Joe Burrow's school from Louisiana State University to LSU  
college_teams["Joe Burrow"] = "LSU"

#We can also create new key-value pairs by using the same syntax. 
#It looks like Henry Ruggs was accidentally added instead of Jedrick Wills,
#So lets add Jedrick Wills' school to the list
college_teams["Jedrick Wills"] = "Alabama"

#We can then delete specific values using Python's del command
del college_teams["Mekhi Becton"]

#Now you try! Use positional indexing and key-value indexing to print 
#the name and school of the 6th pick in the NFL Draft

#name = 
#school = 
#print("Selected with the 6th pick in the NFL Draft is " + name + " from " + school)

#%% Part 3: The For Loop

#Loops are incredibly helpful tools in programming as they allow you to 
#execute code multiple times. For example, say we wanted to simply print
#the names of all 10 of the top 10 players. Without loops, we would have to 
#write out 10 different print statements. That's not too terrible, but imagine 
#doing that for all 255 players in the NFL draft! With loops, we can print the 
#names in just two lines -

for i in range(10):
    print(top_10_players[i])

#Let's break this down. For Loops are constructed using the following syntax:
#"for <variable> in <iterable>:" 
#In the example above, I have called the variable 'i' and the iterable is the 
#range() function, which is every integer from 0 up to the number specified, 
#not inclusive. We can see that fact clearly using the following code
print(list(range(10)))

#In the above example, we looped through the top 10 players list using
#positional indexing. However, lists are themselves iterables, meaning we are 
#also able to directly loop over them! Therefore, we can also do the following
for player in top_10_players:
    print(player)

#Like lists, strings are also iterables in Python!
#For example, we can print every character of a string like so - 
cra = "Charles River Associates"
for s in cra:
    print(s)

#Now you try! Use a For Loop to print the statement from the end of Part 2
#for every player drafted in the top 10. Make sure to include the position 
#in the draft, the player's football position, and the name of the player 
#in the print statement



#%% Part 4: The While Loop

#For loops are very useful when we want to complete a repetitive task of 
#defined length, such as downloading many files from the same website
#or calculating a statistic for years 2000-2019 based on data

#But what if you want to do something for an unknown number of iterations?
#For example, repeat an alarm until the user hits snooze or simulate
#rolling a die until you roll a six?

#These cases would be better served by a while loop. A While Loop is a loop 
#that continues for the time a condition is met. Such as below
num = 3
while num < 100:
    print(num)
    num *= 3

#In the above example, the loop first checks if the number is less than 100.
#If it is and the statement returns the boolean 'True', it prints the 
#number and then multiplies it by 3. It continues to do this until the 
#condition is no longer met, i.e. the number is greater than or equal to 100.

#What happens though if the condition is never met? For example, what if 
#instead of multiple by 3 we multiplied by 1, meaning 'num' would never change?
#In that case, the computer would be stuck in an infinite loop and would never
#move on! If you every find yourself stuck in an infinite loop, use cntrl+c
#to escape the loop.

#Let's try another example. As was said before, While Loops are great 
#at handling instances where we don't know how many iterations a process will
#take. For example, what if we wanted to simulate how many coin flips it takes
#to get a heads? We could do the following, which relies on the 'random'
#package which we will discuss in the next secion. For now, focus just on the 
#loop and know that the 'random.randint(0, 1)' produces 1 or 0 with equal
#likelihood

import random

heads = False
flips = 0
while not heads:
    num = random.randint(0, 1)
    if num == 1:
        heads = True
    flips += 1
    
#In the above example, our condition is 'not heads', or in other words
#while heads is False. In the body of the While Loop, we simulate the coin flip,
#in this instance we say we flip a heads if the 'num 'variable equals 1. 
#If so, we set 'heads' to True so that the While Loop doesn't continue.
#We then add 1 to a 'flips' variable which keeps track of how many flips 
#it took to get a heads.

#Now you try! Imagine you are an alarm app developer and need to write code
#that checks whether the user would like stop the alarm after it goes off.
#Below is commented-out While Loop that prints "Ring!" indefinitely. 
#Add code below the print statement that, asks the user if they'd like to
#stop the alarm and stores the response in a variable. 
#If the user says "Yes", then end the loop. If not, let the alarm continue.

#Note: If you run just the below code after un-commenting it, you'll be stuck
#in an infinite loop! IF that happens, remember to click into the console
#and press cntrl+c

#stop = False
#while not stop:
#    print("Ring!")
