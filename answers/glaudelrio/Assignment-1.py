
# coding: utf-8

# 1.) Who in the hell is Guido Van Rossum? Have Python print the answer, using jupyter

# In[19]:

guido_van_rossum = "The author of Python programming language"


# In[20]:

print(guido_van_rossum)


# 2.) Explain (what it is) and execute the most famous first programming exercise. Where does this come from? Feel free to just add your answer to the iPython notebook as markdown-formatted text.
# 
# #The most famous first programming exercise is the  "Hello, world!" program, often used to introduce beginning programmers to a programming language. This exercise and the tradition of using it as a first exercise was influenced by an example program in the seminal book The C Programming Language. The example program from that book prints "hello, world" (without capital letters or exclamation mark), and was inherited from a 1974 Bell Laboratories internal memorandum by Brian Kernighan, Programming in C: A Tutorial.

# In[22]:


print("Hello, world!")


# 3.) Produce the sum of the year of your birthday and the year of this class

# In[26]:

1988+2016


# 4.) Divide 3 by 2 and return the expected result. Is this what you expected? Why or why not?
# #Yes, the result is 1.5 as I expected to be.

# In[29]:

3/2


# 5.) Print the numbers 0 to 50 by 5

# In[42]:

for i in range(0,55,5):
    print(i)


# 6.) Draw and print 10 discrete numbers from a uniform distribution spanning the interval [0,1000000]

# In[53]:

import numpy
print(numpy.random.randint(low=0, high=1000000, size=10))


# 7.) Python is what is known as a zero-indexed programming language. Illustrate what this means.

# In[54]:

a = [1,2,3,4,5,6,7,8,9,10]
print(a[0])
print(a[1])


# 8.) import this

# In[55]:

import this

