#!/usr/bin/env python
# coding: utf-8

# ### Day objectives
# -python Data structures:
#  > Lists
#  >Tuples
#  >Dictionaries
# -Basic program sets on Data Structures
# -Advanced Problem set
# -Contact Application(Dictionary object)
# 
# Data Structures:
# 
# -To store,search and sort the data
# 

# ### Python Data Structures
# ### Lists
# -It's one of common data structures supports by python,the list items are separated by comma operator and enclosed in square brackets
#     -Example:
#         - list1=[1,6,2,18,9]
#         - list2=["Gitam",10,12,15.5,"Hyderabad"]
#         

# In[10]:


lst =[1,8,16,9,2]  #Creating the list object in python
print(lst)  #Access the entire list
print(lst[0])  #Access the first item list
print(lst[1])  #Access the second item list
print(lst[-1])  #Access the last item list
print(lst[-2])
print(lst[1:])
print(lst[1:4])
print(lst[-1:])


# In[18]:


#Update the list item values using index(Direct referncing)
li=["Gitam","Python",1989,2002]
print(li)
li[2]=2019
print(li)


# In[19]:


# delete the specific item in the list
print(li)
del li[2]
print(li)


# In[20]:


#Basic list Operations
li


# In[25]:


#Basic list Operations
lst1=[1,9,6,18,2]
print(len(lst1))  #len of the list
print(lst1 *2)  #Repetation
print(len(lst1))
print(9 in lst1) #list item is present or not
print(15 in lst1)
#Access the list items using iteration
for x in range(len(lst1)):
    print(lst1[x],end=' ')


# In[29]:


#Fuction of the list
lst1
print(min(lst1)) #min item/element of the list
print(max(lst1)) #max element of the list
print(sum(lst1)) #sum of the all elements of the list
print(sum(lst1)//len(lst1))  #Average of list elements
print(sum(lst1[1::2])/len(lst1[1::2])) #Average of all the alternate numbers


# In[56]:


lst1
lst1.append(24) #adding a new element at the end of the list
lst1
lst1.insert(2,56) # adding a element at particular index
lst1
lst1.count(18)  #return the value how many times the object repeated
lst1.index(56)
lst1.sort() # its sort the list in ascending order
lst1
lst1.pop() #remove the last element from the list
lst1
lst1.pop(1)  #Remove an element from a particular index
lst2 =[123,23,45]
lst1.extend(lst2) #merge the list2 into list1
lst1.reverse()
lst1.remove(123)
lst1


# In[52]:


li=[1,9,8,2,6,3]
print(li[-1:2:-2])


# In[53]:


li=[1,9,8,2,6,3]
print(li[-1:0:-2])


# In[66]:


# Function to find the second large item from the list
#i/p: [1,19,6,2,8,18,3]
#o/p: 18

def secondLarge(li):
    li.sort()
    return li[-2]
li=[1,19,6,2,8,18,3]
secondLarge(li)


# In[72]:


def secondLarge(li):
    li.sort()
    return li[-2]
def genericLarge(li,n):
    li.sort()
    return li[-n]
li=[1,19,6,2,8,18,3]
genericLarge(li,4)


# In[73]:


# Function to find the least item from the list
#i/p: [1,19,6,2,8,18,3]
#o/p: 2
def secondLeast(li):
    li.sort()
    return li[1]
def genericLeast(li,n):
    li.sort()
    return li[n-1]
li=[1,19,6,2,8,18,3]
genericLeast(li,4)


# In[ ]:


###Linear Search
- Linear Search Algorithm can be applied on Duplicate and Unique List
  -Unique List: The all item of the list is appeared only one
  -Duplicate List: The items of the list can be appeared more than once
 -Linear search Algorithm can be applied on sorted list or unsorted


# In[76]:


#Function to search the data in a list
#search is found then return the index if not return -1
def linearSearch1(li,tarItem):
    for x in range(len(li)):
        if li[x] ==tarItem:
            return x
    return -1
li =[1,19,6,2,8,18,3]
linearSearch1(li,8)


# In[77]:


# Function
# i/p : [1,5,9,6,5,15,1,2,5],key=5 # Duplicate
# o/p :1 4 8

def linearSearch2(li,tarItem):
    for x in range(len(li)):
        if li[x] == tarItem:
            print(x,end=" ")
    return
li= [1,5,9,6,5,15,1,2,5]
linearSearch2(li,5)


# In[81]:


# Function
# i/p : list
#o/p : seq of characters
# Test case
# [1,5,9,6,5,15,1,2,5],tar=5 --!! !!!!! !!!!!!!!!

def linearSearch3(li,tarItem):
    # Implement the logic
    for x in range(len(li)):
        if li[x] == tarItem:
            j=0
            while j!=x+1:
                print("!",end=" ")
                j=j+1
            print(end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
linearSearch3(li,5)


# In[82]:


# Function
# i/p: List
# o/p: Formatted
# Test case:
# [12,2,45,9,18,15,36] --60
#A list item which is perfectly multiple of 3 and 5

def linearSearch4(li):
    sum=0
    for x in range(len(li)):
        if li[x] %3 ==0 and li[x] % 5==0 :
            sum += li[x] #sum=sum + li[x]
    return sum
li= [12,2,45,9,18,15,36]
linearSearch4(li)
        


# In[83]:


# Function
#i/p:list
#o/p:formatted o/p
#test case
#[1,2,3,4,5] --[1,3,8,15,5]
#[6,5,2,8,2] --[6,12,40,4,2]

#1.print first and last as it is because first number does not have previous and last-
 #-does not have next number
#2. need to multiply the previous and next number

def linearSearch5(li):
    for x in range(len(li)):
        if x ==0 or x == len(li) -1:
            print(li[x],end=" ")
        else:
            print(li[x-1]*li[x+1],end=" ")
    return
li =[1,2,3,4,5]
linearSearch5(li)


# In[4]:


#Function
# i/p: list
#o/p : formatted o/p
# test cases:
#[1,6,9,4,16,19,22] -- 1 9 19 22

#1.first and last element print as it is
#2.Both sides numbers are even then print it

def linearSearch6(li):
    for x in range(len(li)):
        if x ==0 or x == len(li) -1:
            print(li[x],end=" ")
        elif li[x-1]%2==0 and li[x+1]%2==0:
            print(li[x],end=" ")
    return
li =[1,6,9,4,16,19,22]
linearSearch6(li)


# In[6]:


### Number to list

 #.Input as output
 #.Expected output will be lost


# In[7]:


# Function for Conversion -Number to list
#input --Number
#output --list
#Test cases:
#14569 --[1,4,5,6,9]
#1990 --[1,9,9,0]
def numberListConversion(n):
    li =[]
    while n !=0:
        r=n%10
        li.append(r)
        n=n // 10
    li.reverse()
    return li
numberListConversion(14569)


# In[11]:


# Function to count the occurences of a character in a string
# "Python Programming", p-->2
# "Python Programming", m-->2
def countCharOccurances(s,c):
    cnt=0
    for ch in s:
        if ch == c:
            cnt+=1
    return cnt
def countCharOccurances1(s,c): #both functions gives the same output
    return s.count(c)
countCharOccurances("Python Programming",'m')


# In[12]:


#String to list
#input will be string
#.Expected output will be list
# Function to convert string to list
# Test case
# "1 2 3 4 5 6" --[1,2,3,4,5,6]

def strintToListConversion(s):
    li=s.split()
    numberslist =[]
    for i in li:
        numberslist.append(int(i))
    return numberslist
s="1 2 3 4 5 6"
strintToListConversion(s) #[1,2,3,4,5,6]


# # sorting Algorithms
# 
# #.All the sorting algorithms makes the list into ascending order
# #-Bubble sort
# #-Selection sort
# #-Insertion sort

# #Bubble sort 
# #-this algorithm compares the adj elements,if the first element is greater
# #-than second element then its required to swap the elements

# In[13]:


# Function to represent the Bubble sort
def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li
li= [19,1,25,6,18,3]
bubbleSort(li)


# In[ ]:




