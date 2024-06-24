from django.db import models

# Create your models here.
class sage(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=55)
    phone=models.CharField(max_length=20)
    message=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class reserve(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=55)
    phone=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    message=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class comment(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=55)
    subject=models.CharField(max_length=55)
    message=models.CharField(max_length=255)



