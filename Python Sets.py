#!/usr/bin/env python
# coding: utf-8

# In[2]:


my_fruits = {'banana', 'guava', 'cashew', 'plantain'}
print(my_fruits)


# In[3]:


#To show a set does not print duplicated item
my_fruits = {'banana', 'guava', 'cashew', 'plantain', 'banana'}
print(my_fruits)


# In[4]:


#To confirm the data type
my_set = set(('cherry', 'mango', 'garden egg'))
print(type(my_set))


# In[5]:


#To confirm the data type
my_set = set(['cherry', 'mango', 'garden egg'])
print(type(my_set))


# In[6]:


#To list out the items in the set my_fruits through looping
for i in my_fruits:
    print(i)


# In[7]:


#To check if an item is present in the set
print("banana" in my_fruits)


# In[8]:


#To add the item "Mango" to the set 
my_fruits.add('Mango')
print(my_fruits)


# In[9]:


#Adding of sets using update function
new_set = {'cherry', 'garden egg'}
my_fruits.update(new_set)
print(my_fruits)


# In[10]:


#Removing of an item from the set using the remove function
my_fruits.remove("cashew")
print(my_fruits)


# In[11]:


#Removing of an item from the set using the discard  function as it does not give an error message if the item is not present in the set
my_fruits.discard('water melon')
print(my_fruits)


# In[12]:


#Removing of an item using the pop function. It removes the last item from the set
my_fruits.pop()
print(my_fruits)


# In[13]:


#Using the union function to join two sets together, the union usually produces a new set due to the addition

fresh_set = {'cucumber', 'lemon'}
x = fresh_set.union(my_fruits)
print(x)


# In[14]:


#Using the update function to join two sets together.
fresh_set.update(my_fruits)
print(fresh_set)


# In[15]:


#Using the intersection_update function to print out the duplicates between two sets to be joined
fresh_set = {'cucumber', 'lemon', 'banana', 'garden egg'}
my_fruits.intersection_update(fresh_set)
print(my_fruits)


# In[16]:


#Using the intersection function to print out the duplicates between two sets, it must be assigned a new name
fresh_set = {'cucumber', 'lemon', 'banana', 'garden egg'}
latest_set = my_fruits.intersection(fresh_set)
print(latest_set)


# In[17]:


#using the symmetric_difference_update funtion to keep only the unique values between two sets and leaving out the duplicates
fresh_set = {'cucumber', 'lemon', 'banana', 'garden egg'}
fresh_set.symmetric_difference_update(my_fruits)
print(fresh_set)


# In[19]:


#While the symmetric_difference function allows a new set to be created
fresh_set = {'cucumber', 'lemon', 'banana', 'garden egg'}
latest_set2 = fresh_set.symmetric_difference(my_fruits)
print(latest_set2)


# In[ ]:


#The clear function is used to clear all the items in the set while the del function deletes the whole set

