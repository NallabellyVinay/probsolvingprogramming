#!/usr/bin/env python
# coding: utf-8

# ### Regular Expression
# - Pattern Matching
# - Patterns(re) package
# - [0-9] --> Any digit matching
#              > Two digit number  (^[0-9]{2}$)
#              > Five digit number (^[0-9]{2}$)

# ### Regular Expression for characters
# - [a-z] --> Any lower case characters
# - [A-Z] --> Any upper case characters
# - ^[a-z]{5}$ --> It accepts 5 lower case characters
# - ^[a-zA-Z]{8}$ --> Accept 8 characters can be anything lower and upper
# - ^[[a-zA-Z0-9]{8}$ --> Accept 8 characters can be anything lower,upper and digit

# In[7]:


# Function to test two digit number matching
import re
def twoDigitMatching(n):
    pattern = '^[0-9]{2}$'
    n=str(n)
    if re.match(pattern,n):
        return True
    return False
print(twoDigitMatching(12))   #True
print(twoDigitMatching(123))  #False


# In[10]:


# Function to define to test username having 8 characters
# Upper case and lower
def testUsername(s):
    pattern = '^[a-zA-Z]{8}$'
    if re.match(pattern,s):
        return True
    return False
print(testUsername('GitamHYD'))
print(testUsername('Gitam188'))


# ### Regular Expression to match the Indian Mobile Number
# - 10 Digits
# - (First digit will be [6-9]) and remaining 9 digits will be [0-9]
# - Example:- 7901086614
# - Re - ^[6-9][0-9]{9}$
# - Example:- 09988774455 (Re - Cap[0][6-9][0-9]{9}Dollar)
# - Example:- +919494283478
# - Re-^[+][9][1][6-9][0-9]{9}$

# In[12]:


# Function to validate the Indian Mobile number
def phoneNumberValidation(phone):
    pattern = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    phone = str(phone)
    if re.match(pattern,phone):
        return True
    return False
phoneNumberValidation('+919988774455')


# -- Regular Expression to Validate the RollNumber
#  - Example : 1521A0501
#  - Example : 1521A0109
#  - Example : 1521A0499
# - Regular Expression to validate the password
#  - Parameters : Len min of 6 characters and Max of 15 characters
#  - Accept lower case, upper case, Digits spl char(@,#,!)

# In[24]:


def rollnumbervalidation(rollnumber):
    pattern = '^[1][5][2][1][A][0-9]{4}$'
    rollnumber = str(rollnumber)
    if re.match(pattern,rollnumber):
        return True
    return False
rollnumbervalidation('1521A0501')


# In[22]:


def password(s):
    pattern = '^[!-~]{6,15}$'
    if re.match(pattern,s):
        return True
    return False
print(password("Ap@18151925"))




# ### Email ID validation using Regular Expression
# - Example : Username@DomainName.extension
# - Username :-
#             - Length will be [6-15]
#             - No Spls characters apart from Underscore(_)
#             - Should not begin and ends with Underscore(_)
#             - Characters Set : All digits and lower case
# - DomainName :- 
#              - Length will be [3-18]
#              - No spls characters
#              - Character Set : All digits and lower case
# - Extension :-
#              - Length will be [2-4]
#              - No spl characters
#              - Character Set : Lower case characters

# In[38]:


def emailIdValidation(email):
    pattern = '^[0-9a-z_.][0-9a-z_.]{6,15}[@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False
emailIdValidation('vinay.nallabelly@gmail.com')


# ### Python Turtle
# - Turtle Graphics

# In[1]:


# Step 1 : Make all the turtle package to be imported
import turtle
# Turtle method creates and returns a new object
a1= turtle.Turtle()
# forward() method moves 100 pixels
turtle.forward(250)
#we are done
turtle.done()


# In[1]:


#Line draw in reverse direction
import turtle as tt
a1 = tt.Turtle()
tt.backward(100)
tt.done()


# In[1]:


# Draw square
import turtle as tt
a1 = tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
tt.done


# In[1]:


# Draw square
import turtle as tt
a1 = tt.Turtle()
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
a1.backward(150)
a1.left(90)
tt.done()


# In[ ]:


# Draw pentagon
import turtle as tt
a1 = tt.Turtle()
a1.forward(50)
a1.right(72)
a1.forward(50)
a1.right(72)
a1.forward(50)
a1.right(72)
a1.forward(50)
a1.right(72)
a1.forward(50)
tt.done()


# In[ ]:


# Star
import turtle as t
a1 = t.Turtle()
for i in range(40):
    a1.forward(50)
    a1.right(144)
t.done()


# In[ ]:


# Spiraling Star
import turtle as t
a1 = t.Turtle()
a1.pencolor('blue')
for i in range(40):
    a1.forward(i*10)
    a1.right(144)
t.done()


# In[ ]:


# Square Spiral help of Turtle
import turtle as t
a1= t.Turtle()
for i in range(250):
    a1.forward(i)
    a1.left(91)   
t.done()
 


# In[ ]:


# Hexagon with multi color

from turtle import *
colors= ['blue','green','yellow','orange','purple','red']
for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)


# In[ ]:


# goto function

from turtle import *
goto(50,50)
goto(-50,50)
goto(100,-50)
goto(-50,-50)


# In[4]:


from turtle import *
colors = ['blue','red','purple','orange','black','green']
for angle in range(0,360,15):
         pencolor(colors[angle%6])
         setheading(angle)
         forward(100)
         write(str(angle)+'0')
         backward(100)
    


# In[1]:


# undo() function will undo the turtle last action
from turtle import *
pencolor('blue')
for i in range(15):
    forward(100)
    left(90)
    forward(10)
    left(90)
    forward(100)
    right(90)
    forward(10)
    right(90)
pencolor('red')
for i in range(90):
    undo()


# In[ ]:


from turtle import *
pensize(50)
pencolor("blue")
forward(250)
pencolor(0,1,0,0)
forward(250)
pensize(10)
goto(-400,50)

for red in range(4):
    for green in range(4):
        for blue in range(4):
            pencolor(red/4.0,green/4.0,blue/4.0)
            forward(10)

