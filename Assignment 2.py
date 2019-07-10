#!/usr/bin/env python
# coding: utf-8

# In[8]:


def q1(x):
    while x-2!=0:
        a=0
        b=1
        c=0
        for i in range(x-2):
            c=a+b
            a=b
            b=c
        print(c,end=" ")
        x-=1
    print('1 0')
    return
q1(int(input("enter number")))


# In[9]:


def Q2(n):
    a=[]
    s=0
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        c=0
        for j in range(n):
            if i!=j:
                if a[i]==a[j]:
                    c+=1
        if c==0:
            s=s+a[i]
    return s
Q2(int(input("no of values")))


# In[10]:


def Q3(a,b):
    if len(a)<=len(b):
        n=len(a)
        k=len(b)
    else:
        n=len(b)
        k=len(a)
    for i in range(n):
        print(a[i],b[i])
    for j in range(n,k):
        if(len(a)<=len(b)):
            print(b[j],'*')
        else:
            print(a[j],'*')
    return
x=str(input("enter str:"))
x=x.split()
Q3(x[0],x[1])


# In[11]:


def Q4(a,b):
    if len(a)>=len(b):
        print(a.upper())
    else:
        print(b.upper())
    return
x=str(input("enter str:"))
x=x.split()
Q4(x[0],x[1])


# In[12]:


def Q5_1(a):
    a=a.split()
    for i in range (len(a)):
        if a[i].istitle()==True:
            print(a[i].upper(),end= " ")
    return
x=str(input("enter str:"))
Q5_1(x)


# In[13]:


def Q7(n):
    for i in range(len(n)):
        n[i]=int(n[i])
    for i in range(len(n)):
        for j in range(n[i]):
            print("*",end="")
        print("")
    return
x=input("enter num")
Q7(list(x))


# In[31]:


# Q11
def square(n):
    for i in range(n):
        print(2**i,end=" ")
    return
n=int(input("enter a number"))
square(n)


# In[30]:


#  Q9
def comb(a,b):
    c=a+b
    return c 
a=str(input("enter a string "))
b=str(input("enter a string "))
comb(a,b)


# In[32]:


# Q10
def square(n):
    for i in range(n):
        print(3**i,end=" ")
    return
n=int(input("enter a number"))
square(n)


# In[35]:


#Q8
def delete(n,target):
    c=0
    for i in range(len(n)):
        if n[i]==target:
            c+=1
    print(n.replace(target,"",c))
n=str(input("enter a string"))
target=str(input("enter a char"))
delete(n,target)


# In[37]:


#Q14
def fact(a):
    f=1
    for i in range (1,a+1):
        f*=i
    return f   
def series(m):
    s=0
    for x in range (1,n+1):
        s=s+fact(x)
    return s
n=int(input("enter n"))
series(n)


# In[1]:


#Q13
def series(n):
    a=2
    print(a,end=" ")
    for i in range (1,n+1):
        b=a+(13*i)
        print(b,end=" ")
        a=b
    return
n=int(input("enter a number"))
series(n)


# In[2]:





# In[3]:


#Q 6
def findNthTerm(n): 
    if n % 2 == 0: 
        n //= 2
        print(3 ** (n - 1)) 
    else: 
        n = (n // 2) + 1
        print(2 ** (n - 1)) 
if __name__=='__main__': 
    N = 3
    findNthTerm(N) 
    N = 21
    findNthTerm(N)


# In[6]:


# Q15. Series Generations:-  1,9,17, 33,49,73,97
def series(n):
    a=1
    b=8
    print(a,end=" ")
    for i in range (1,n-2):
        c=a+b
        z=c+b
        print(c,z,end=" ")
        b=b*2
        a=z
n=int(input("enter n"))
series(n)


# In[7]:


#Q 12
def series(n):
    a=1
    b=3
    c=a+b
    print(a,b,c,end=" ")
    for i in range (4,n+1):
        d=a+b+c
        a=b
        b=c
        c=d
        print(d,end=" ")
    return
n=int(input("enter a number"))
series(n)


# In[ ]:




