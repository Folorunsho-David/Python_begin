#!/usr/bin/env python
# coding: utf-8

# In[26]:


#List of 5 Different Fruits

fruits = ['apple', 'banana', 'carrot', 'guava', 'pineapple']
fruits


# In[27]:


#Add two more fruits to the list

fruits.append('oranges')
fruits.append('grape')

print(fruits)


# In[28]:


#removing the third item from the list

fruits.pop(2)

fruits


# In[30]:


#Sorting the list in alphabetical order
fruits.sort()
fruits


# In[31]:


#reversing the order of the list
fruits.reverse()
print(f'The list of the reversed fruits: {fruits}')


# Task 2

# In[36]:


#Creating a list of 10 numbers
numbers = list(range(1, 11))
numbers


# In[38]:


#Printing the first, second and last element
first = numbers[0]
second = numbers[1]
last = numbers[-1]

print(first)
print(second)
print(last)
print(f'The first number is : {first}, the second is {second} and the last is: {last}')


# In[39]:


#Printing of every second element in the list

numbers[::2]


# TASK 3

# In[41]:


#Creating a list of five colors

colors = ['red', 'blue', 'green', 'yellow', 'black']
colors


# In[45]:


#replacing the color green with purple

colors[2] = "purple"
colors


# In[46]:


#Inserting the color while into the list

colors.insert(2, "white")
colors


# In[47]:


#Removing the last item in the list

colors.remove('black')
colors


# TASK 4

# In[6]:


numbers = list(range(1, 11))

print(numbers)

for num in numbers:
    print(num*2)


# In[7]:


#using a while loop to print even numbers


i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(numbers[i])
        
    i += 1


# In[8]:


#creating the square of each value using list comprehension

squares = [num ** 2 for num in numbers]
squares


# TASK 5

# In[9]:


#Create a program that removes duplicate from a list

def remove_duplicates(lst):
    return list(set(lst))

num = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

print(f"the list with the removed duplicates: {remove_duplicates(num)}")


# In[10]:


#Creating a nested list of three students

students_list = [["alice", 24, "A"],["beatrice", 20, "B"], ['patrick', 25, "A"]]
students_list[1]


# In[11]:


#Function that returns the minimum and maximum values of a numbers in a list

def max_min_val(lst):
    return max(lst), min(lst)

number = [2, 5, 8, 9, 12, 17, 22, 28, 35, 45]
max_value, min_value = max_min_val(number)
print(f'the maximum value in the list is: {max_value} and the minimum value is: {min_value}')


# In[12]:


#Writing a program to merge two list without using +

def merge_list(list1, list2):
    for items in list2:
        list1.append(items)
    return list1

list1 = [1, 3, 5]
list2 = [2, 7, 9]

print(f'The result of the merger of the two lists is: {merge_list(list1, list2)}')


# In[19]:


#Checking if a given element is in the list, the return the index

def check_element(lst, element):
    if element in lst:
        return lst.index(element)
    return -1

the_list = ['apple', 'cashew', 'guave', 'oranges']
element_to_find = 'cashew'
index = check_element(the_list, element_to_find)
print(f"The index of '{element_to_find}': {index}" if index != -1 else "element not found")


# In[ ]:




