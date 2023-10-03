#!/usr/bin/env python
# coding: utf-8

# # Exercise 00
# Write a bit of code that prints _Introduction to Programming_ to the console and execute the cell

# In[74]:


print("Introduction to Programming")


# -----------------------------------------------------------------------------
# # Exercise 01
# Hello World is traditionally the first program anyone writes. It is
# very simple and the only thing it should do is print Hello World! to the
# terminal window.
# Create a file called HelloWorld.py and edit the contents so it prints Hello World! to the terminal and execute it using the command line.

# -----------------------------------------------------------------------------
# # Exercise 02
# Write some code to print your name, email, and age on separate lines. For each element first assign it to a variable and use the variable to print. 
# 
# Bonus: try to create the print statement for all variable in one line of code. (hint: '\n' is the character for a new line)

# In[ ]:


print("ziyu yang" "\n" "ncbvzy@ucl.ac.uk" "\n" "23")


# -----------------------------------------------------------------------------
# # Exercise 03
# Print the numbers 0, 178, -21, 2938 divided by 49, 436 multiplied with 9948 and 12 to the power of 20
# 
# (Hint: Look up the documentation of basic arithmetic operators)

# In[ ]:


a=(0, 178, -21, 2938)
for i in a:
    print(i/b)
print(436*9948)
print(12**20)


# In[99]:


-----------------------------------------------------------------------------
# Exercise 04
Print sin(200), cos(100), tan($\pi$/4)

(Hint: Look up for how to use trigonometric function, and how to get the value of $\pi$.) 


# In[91]:


import math
print(math.sin(200))
print(math.cos(100))
print(math.tan(math.pi/4))


# -----------------------------------------------------------------------------
# # Exercise 05
# Write a program to read your first and last names from the console seperately, and then print them on the console together, separated by a space.

# In[94]:


firstname=input()
lastname=input()
fullname=firstname+" "+lastname
print(fullname)


# -----------------------------------------------------------------------------
# # Exercise 06
# Write a program that determines whether a number given as user input is positive or negative
#  
# You will need to convert the console input from a string to a number first!

# In[106]:


n=input()
if(int(n)>0):
    print("positive number")
elif(int(n)<0):
    print("negative number")
else:
    print("neither positive or negative")


# -----------------------------------------------------------------------------
# # Exercise 07
# Write a program that picks a random number between 1-20 and makes the user guess until they get the number right. Then print a congratulations message
# - (Find out yourself how to generate a random integer)
# - Bonus: make the user choose the range within which they have to guess
# - Bonus: keep track of how many guesses were made and print this at the end

# In[130]:


import random
n1=random.randint(1,20)
while True:
    n2=int(input())
    if (n1==n2):
        print("congrats")
        break
    else:
        print("error")


# -----------------------------------------------------------------------------
# # Exercise 08
# Ask a sentence as input, then print the words in alphabetical order.
# Hint: look up how to split up a string

# In[134]:


sentence=input()
words=sentence.split()
words.sort()
print(words)


# -----------------------------------------------------------------------------
# # Exercise 09
# Write a program using for loops to print a christmas tree of x lines high
# specified by the user.
# (use for loops)
# so for instance, a chrismas tree of 4 high should looks like this:
# 
# ```
# 
#     *
#    ***
#   *****
#  *******
#     |
# 
# ```
# 
# hint: first combine strings into a variable before printing

# In[ ]:





# -----------------------------------------------------------------------------
# # Exercise 10
# Write a piece of code that prints the first $n$ numbers of the padovan sequence

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




