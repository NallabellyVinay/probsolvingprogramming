#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Data Structures

#.Dictionaries


# ### Dictionaries
# 
# #> it works on the concept of set unique data
# #> Keys,values is the unique identifier for a value
# #> Each key is separated from its values with colon(:)
# #> Each key and vale is separated by comma(,)
# #> Dictionaries enclosed with curly braces({})

# In[3]:


d1 = {"Name":"Gitam","EmailId":"gitam@gmail.com","Address":"Hyderabad"}
print (d1)


# In[4]:


d1["Name"] #Access the specific key


# In[7]:


d1['EmailId'] ='Gitam-Python@gmail.com'  #Update the data


# In[8]:


d1["EmailId"]


# In[9]:


del d1['EmailId']  #Delete the specific key value


# In[10]:


d1["EmailId"]


# In[11]:


d1 # del d1 will delete the entire dict object


# In[12]:


d1.keys()  #returns the list of keys


# In[13]:


d1.values()  #returns the values


# In[14]:


d1.items() #the list of tuples of keys and values

### Tuples
#-t1 parenthesis () li square brackets[]
#-Difference between list and tuples
#>  -list are mutable-can be chanfed/modified
#>   -Used to access modify,add,Delete data
#> -Tuples are immutable-cannot be changed
#>      -Used to data only
# In[15]:


t1=(1,2,3,4,5,6)
t1
type(t1)


# ### Contact
# - Add Contact
# - Search the Contact
# - List all contacts               # Dict and list
#       - name1:phone1
#       - name2:phone2
# - Modify the contact
# - Remove the contact
# - Import the contact

# In[18]:


# Add contact
contacts = {}  # Creating a dict object
def addContact(name,phone):
    if name not in contacts: 
        contacts[name] = phone
        print("Contact  details are added")
    else:
        print("Contact details are already exist")
    return
addContact('Anurag','9030396936')
addContact('Anudeep','9492111956')
addContact('Anurag','9030396936')


# In[22]:


# Search for contact details
def searchContact(name):
    if name in contacts:
        print(name," : ", contacts[name])
    else:
        print("%s does not exist" % name)
    return
searchContact('Anurag')
searchContact('Anil')
searchContact('Anudeep')


# In[23]:


# Import some contacts
# Merge the contact with existing one

def importContact(newContacts):
    contacts.update(newContacts)
    print(len(newContacts.keys()),"Contacts added successfully")
    return
newContacts = {'Vinay':7901086611,'Chetan':9985918274}
importContact(newContacts)


# In[26]:


print(contacts)
print(newContacts)


# In[27]:


contacts


# In[29]:


# Delete a contact
def deleteContact(name):
    if name in contacts:
        del contacts[name]
        print(name,"deleted successfully")
    else:
        print(name,"not exists")
    return
deleteContact('Chetan')


# In[32]:


# Update the contact details
def deleteContact(name,phone):
    if name in contacts:
        contacts[name] = phone
        print(name,"Updated successfully")
    else:
        print(name,"Not exists")
    return
deleteContact('Anurag',7985156781)
deleteContact('Chetan',7864574568)


# In[33]:


#String 

#classical version
li=["Python","Programming"]
print("%s %s"%(li[0],li[1]))


# In[35]:


print("{0} {1}" .format(li[0],li[1]))


# In[40]:


li1 = [1,2,3,4]
print("%d %d %d %d" % (li1[0],li1[1],li1[2],li1[3]))


# In[39]:


print("{0} {1} {2} {3} ".format(li1[0],li1[1],li1[2],li1[3]))


# ### String Functions
# - upper() -- Will convert given string into upper case
# - lower() -- Will convert given string into lower case

# In[41]:


s1='Gitam'
print(s1.upper())
print(s1.lower())


# ### Boolean Functions (True or False)
# 
# - islower() -- True if the string is lower case /False if the string not lower case
# - isupper() -- True if the string in upper case /False if string not in upper case
# - islittle() -- True if the string follows title case / False
# - isalpha() -- True if the string contains only alphabets
# - isnumeric() -- True if the string contains only numbers /False
# - isspace() -- 

# In[42]:


s1='GITAM'
print(s1.islower())
print(s1.isupper())


# In[43]:


s2 = "Python Programming"
s3 = "python Programming"
print(s2.istitle())
print(s3.istitle())


# In[44]:


s2 = "Application1889"
s3 = 'PythonProgramming'
print(s2.isalpha())
print(s3.isalpha())


# In[46]:


s1="1234"
s2="Application1234"
print(s1.isnumeric())
print(s2.isnumeric())


# In[47]:


s1 = " "
s2= "Py th on"
print(s1.isspace())
print(s2.isspace())


# ### String Methods
# - .join() -- Method will concatenate the two strings
# - .split() -- split() returns the list of strings separated by a whitespace(no parameters are given)
# - replace() -- replaces the specific word/character with new word /character

# In[48]:


s1 = 'Python'
print(" ".join(s1))


# In[49]:


s2 = "Python Programming Easy to learn"
print(",".join(s2))


# In[50]:


li = ['Python','Programming','Learn']
print(",".join(li))


# In[51]:


s2 = "Python Programming Easy to learn"
print(s2.split())


# In[52]:


s2 = "Python Programming Easy to learn"
print(s2.split('a'))


# In[53]:


s2 = "Python Programming Easy to learn"
li=s2.split()   #split the string -- List object
print(li)
print(len(li))


# In[54]:


s2 = "Python Programming Easy to learn"
li=list(s2)
print(li)


# In[55]:


s2 = "Python Programming Easy to learn"
print(s2.replace("gra","Application"))


# ### Packages and Modules
# 
# **Packages**
#     - A collection of Modules(Single Python file .py) and subpackages
# ** Module**
#     - A single Python c=file containing set functions
#  
# Packages --> Sub Packages -->Modules -->Functions -->Statements
# 

# In[1]:


# Import the externals packages to python file
import math
math.floor(123.45)


# In[4]:


from math import factorial as fact
fact(5)


# In[5]:


items=[1,5]
print("s",items)


# In[6]:


# Function to generate N random numbers in given range
import random
def randomNNumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
randomNNumbers(10,0,100)


# In[7]:


# Create a Simple Game
# Generate 20 random numbers 0 to 500
#i/p : number
#o/p :congrats
#     Try once again!!!


# In[ ]:


def generateNumbers(n,lb,ub):
    li= []
    for i in range(0,n):
        li.append(random.randint(lb,ub))
    return li
def check(n):
    if n in li:
        return "Congrats!!!"
    else:
        return "Try once again!!!"
    return
check(15)


# In[ ]:




