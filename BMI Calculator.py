#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[17]:


Name = input("Please enter your name: ")

weight = int(input("Enter your weight in Kg: "))

height = int(input("Enter your height in cm: "))

BMI= weight/((height/100)*(height/100))

print("Your BMI is ",BMI)

if BMI>0:
    if (BMI<18.5):
        print(Name," You are Underweight")
    elif (18.5<BMI<24.9):
        print(Name," You are Normal weight")
    elif (25<BMI<29.9):
        print(Name," You are Overweight")
    elif (30<BMI<34.9):
        print(Name," You are Obese, You need to start workout")
    elif (34.9<BMI):
        print(Name," You are Morbid obesity")
    else:
        print("enter Valid data!")
else:
    print("enter Valid data!")


# In[ ]:





# In[ ]:





# In[ ]:


Below 18.5 Underweight
18.5–24.9 Normal weight
25–29.9 Overweight
30–35 Obese
Over 35 Morbid obesity


# In[14]:


if BMI>0:
    if (BMI<18.5):
        print("You are Underweight")
    elif (18.5<BMI<24.9):
        print("Normal weight")
    elif (25<BMI<29.9):
        print("Overweight")
    elif (30<BMI<34.9):
        print("Obese")
    elif (34.9<BMI):
        print("Morbid obesity")
    else:
        print("enter Valid data!")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




