from django.db import models

class staff_model(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField()
    department = models.CharField(max_length=100)
    salary = models.FloatField()
    hire_date = models.DateField()
 
class student_model(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    join_date = models.DateField()

class fee_model(models.Model):
    student_name = models.CharField(max_length=50)
    amount = models.FloatField()
    status = models.CharField(max_length=50)
    payment_date = models.DateField()

