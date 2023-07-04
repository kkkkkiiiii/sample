from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30, null=False)
    cc=models.DateTimeField(auto_now=True,null=True)


class test(models.Model):
    name=models.CharField(max_length=255, null=False)
    created_at=models.DateTimeField(auto_now=True,null=True)


class POST(models.Model):
    name=models.CharField(max_length=255, null=False)
    

class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)


class User(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
    




# Create your models here.