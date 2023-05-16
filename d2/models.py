from django.db import models

# Create your models here.


class AddPeople(models.Model):
    number = models.IntegerField()
    senderID = models.AutoField(primary_key=True)
    sms = models.TextField()
    #apiKey = models.BigIntegerField()
    textCode = models.TextField()

class ErrorMessage(models.Model):
    code = models.CharField(max_length=10)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)