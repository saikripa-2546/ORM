from django.db import models

from django.contrib import admin

class ormapp (models.Model):
    loan_id=models.IntegerField(primary_key=True)
    loan_type=models.CharField(max_length=100)
    loan_acc=models.FloatField()
    cust_acno=models.IntegerField()
    cust_name=models.CharField(max_length=100)
 
class ormappAdmin(admin.ModelAdmin):
    list_display=('loan_id', 'loan_type','loan_acc','cust_acno','cust_name')