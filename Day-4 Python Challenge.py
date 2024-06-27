#!/usr/bin/env python
# coding: utf-8

# # Day-4 Python Challenge

# # Control Flow Statement 

# # If-Conditions 

# Write a programe to calculate the percentage of a student in the subjects Maths, Java, Python, C, C++.

# In[1]:


x = input("Enter Your Name: ")
a = int(input("Enter Your Marks Scored in Maths: "))
b = int(input("Enter Your Marks Scored in Java: "))
c = int(input("Enter Your Marks Scored in Python: "))
d = int(input("Enter Your Marks Scored in C: "))
e = int(input("Enter Your Marks Scored in C++: "))
n = ((a+b+c+d+e)/500)*100
print("Your Total Percentage in Current Semester: ",n)


# Write a programe to show the achievement of the student and their marks

# In[2]:


a = int(input("Enter Your Total Percentage of Current Semester: "))

if a>=90:
    print("Congratulations You Achieved A Grade")
if a>=70 and a<=90:
    print("Congratulations You Achieved B Grade")
if a>=60 and a<=70:
    print("Congratulations You Achieved B Grade")
    


# # If-Else Statement

# Write a programe to display the student can seat or not in the final exam.

# In[6]:


a = input("Enter Your Name: ")
x = int(input("Enter Your Total Attendance of this Semester: "))

if x>=75:
    print("Congratulations You Can Seat the Final Exam")
else:
    print("Sorry you Can Not Seat the Final Exam")



# Display the Number is Positive or Negative.

# In[9]:


x = int(input("Enter the Random Number: "))
if x>=0:
    print("The Number is Positive")
else:
    print("The Number is Negative")


# # Search Indian Monument with their City.

# In[16]:


city = input("Enter Your City Name: ")

if city=="Delhi":
    print("The Monument in Delhi is: Lakshmi Narayan Temple.")    
elif city=="Maharashtra":
    print("The Monument in Maharashtra is: Gateway Of India.")
elif city=="Gujarat":
    print("The Monument in Gujrat is: Sabarmati Ashram.")
elif city=="Karnataka":
    print("The Monument in Karnataka is: Gol Gumbaz.")
elif city=="Punjab":
    print("The Monument in Punjab is: Golden Temple.")
else:
    print("No Record Found")
    

