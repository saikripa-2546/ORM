# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![Screenshot 2024-11-16 104513](https://github.com/user-attachments/assets/18886006-47da-47f1-9690-abf03d348221)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

from django.db import models
from django.contrib import admin
class loan (models.Model):
    loan_no=models.CharField(max_length=20,help_text="Employee")
    loan_acct=models.CharField(max_length=100)
    loan_amt=models.IntegerField()
    loan_type=models.IntegerField()
    name=models.EmailField()

class loanadmin(loanadmin.ModelAdmin):
    list_display=('','loan_no','loan_acct','loan_amt','loan_type','name')

## OUTPUT
![Screenshot 2024-11-16 103905](https://github.com/user-attachments/assets/8cb63be7-586f-44de-8125-9e017442fcec)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
